#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: main.py
@time: 2022/7/11 10:16
@desc:
        1. 参考链接：https://zhuanlan.zhihu.com/p/161872496
"""
import time

from ple.games.flappybird import FlappyBird
from ple import PLE
import parl
from parl import layers

import paddle.fluid as fluid
import numpy as np
import os
from parl.utils import logger
from parl.algorithms import DQN
import random
import collections
import warnings
warnings.filterwarnings('ignore')

# 训练频率，不需要每一个step都learn，攒一些新增经验后再learn，提高效率
LEARN_FREQ = 5
# replay memory的大小，越大越占用内存
MEMORY_SIZE = 80000
# replay_memory 里需要预存一些经验数据，再从里面sample一个batch的经验让agent去learn
MEMORY_WARMUP_SIZE = 2048
# 每次给agent learn的数据数量，从replay memory随机里sample一批数据出来
BATCH_SIZE = 1024
# reward 的衰减因子，一般取 0.9 到 0.999 不等
GAMMA = 0.99
# 学习率
LEARNING_RATE = 0.01


class Model(parl.Model):
    """Model用来定义前向(Forward)网络，用户可以自由的定制自己的网络结构。"""

    def __init__(self, act_dim):
        hid1_size = 128
        hid2_size = 128
        # 3层全连接网络
        self.fc1 = layers.fc(size=hid1_size, act='relu')
        self.fc2 = layers.fc(size=hid2_size, act='relu')
        self.fc3 = layers.fc(size=act_dim, act=None)

    def value(self, obs):
        """定义网络
        输入state，输出所有action对应的Q，[Q(s,a1), Q(s,a2), Q(s,a3)...]
        """
        h1 = self.fc1(obs)
        h2 = self.fc2(h1)
        Q = self.fc3(h2)

        return Q


class Agent(parl.Agent):
    """Agent负责算法与环境的交互，在交互过程中把生成的数据提供给Algorithm来更新模型(Model)，数据的预处理流程也一般定义在这里"""

    def __init__(self, algorithm, obs_dim, act_dim, e_greed=0.1, e_greed_decrement=0.0):
        assert isinstance(obs_dim, int)
        assert isinstance(act_dim, int)
        self.obs_dim = obs_dim
        self.act_dim = act_dim
        super(Agent, self).__init__(algorithm)

        self.global_step = 0
        # 每隔200个training steps再把model的参数复制到target_model中
        self.update_target_steps = 200

        # 有一定概率随机选取动作，探索
        self.e_greed = e_greed
        # 随着训练逐步收敛，探索的程度慢慢降低
        self.e_greed_decrement = e_greed_decrement

    def build_program(self):
        self.pred_program = fluid.Program()
        self.learn_program = fluid.Program()

        # 搭建计算图用于 预测动作，定义输入输出变量
        with fluid.program_guard(self.pred_program):
            obs = layers.data(name='obs', shape=[self.obs_dim], dtype='float32')
            self.value = self.alg.predict(obs)

        # 搭建计算图用于 更新Q网络，定义输入输出变量
        with fluid.program_guard(self.learn_program):
            obs = layers.data(name='obs', shape=[self.obs_dim], dtype='float32')
            action = layers.data(name='act', shape=[1], dtype='int32')
            reward = layers.data(name='reward', shape=[], dtype='float32')
            next_obs = layers.data(name='next_obs', shape=[self.obs_dim], dtype='float32')
            terminal = layers.data(name='terminal', shape=[], dtype='bool')
            self.cost = self.alg.learn(obs, action, reward, next_obs, terminal)

    def sample(self, obs):
        sample = np.random.rand()
        if sample < self.e_greed:
            # 探索：每个动作都有概率被选择
            act = np.random.randint(self.act_dim)
        else:
            # 选择最优动作
            act = self.predict(obs)

        # 随着训练逐步收敛，探索的程度慢慢降低
        self.e_greed = max(0.01, self.e_greed - self.e_greed_decrement)
        return act

    def predict(self, obs):
        """选择最优动作"""
        obs = np.expand_dims(obs, axis=0)
        pred_Q = self.fluid_executor.run(
            self.pred_program,
            feed={'obs': obs.astype('float32')},
            fetch_list=[self.value]
        )[0]

        # 删除数组维度
        pred_Q = np.squeeze(pred_Q, axis=0)
        # 选择Q最大的下标，即对应的动作
        act = np.argmax(pred_Q)
        return act

    def learn(self, obs, act, reward, next_obs, terminal):
        """每隔200个training steps同步一次model和target_model的参数"""
        if self.global_step % self.update_target_steps == 0:
            self.alg.sync_target()
        self.global_step += 1

        act = np.expand_dims(act, -1)

        # 【重要 by 李英俊】 如果这里act是nan，传过来会被转为-2147483648，从而报错
        # print("act: ", act)
        feed = {
            'obs': obs.astype('float32'),
            'act': act.astype('int32'),
            'reward': reward,
            'next_obs': next_obs.astype('float32'),
            'terminal': terminal
        }

        # 训练一次网络
        # print("raw feed", feed)
        cost = self.fluid_executor.run(self.learn_program, feed=feed, fetch_list=[self.cost])[0]
        return cost


class ReplayMemory(object):
    """经验池：用于存储多条经验，实现 经验回放。"""

    def __init__(self, max_size):
        self.buffer = collections.deque(maxlen=max_size)

    def append(self, exp):
        """增加一条经验到经验池中"""
        self.buffer.append(exp)

    def sample(self, batch_size):
        """从经验池中选取N条经验出来"""
        mini_batch = random.sample(self.buffer, batch_size)
        obs_batch, action_batch, reward_batch, next_obs_batch, done_batch = [], [], [], [], []

        for experience in mini_batch:
            s, a, r, s_p, done = experience
            obs_batch.append(s)
            action_batch.append(a)
            reward_batch.append(r)
            next_obs_batch.append(s_p)
            done_batch.append(done)

        return np.array(obs_batch).astype('float32'), np.array(action_batch).astype('float32'), np.array(
            reward_batch).astype('float32'), np.array(next_obs_batch).astype('float32'), np.array(done_batch).astype(
            'float32')

    def __len__(self):
        return len(self.buffer)


def run_episode(p, agent, rpm):
    """训练一个episode"""
    total_reward = 0
    p.reset_game()
    obs = list(p.getGameState().values())
    step = 0
    while True:
        step += 1
        # print("obs:", obs, end=' ')
        action_index = agent.sample(obs)
        # 采样动作，所有动作都有概率被尝试到
        action = p.getActionSet()[action_index]
        # print("act_dim:", agent.act_dim, "action_index:", action_index, "getActionSet:", p.getActionSet(), "action:", action, end=' ')

        # 行动
        next_obs, reward, done = list(p.getGameState().values()), p.act(action), p.game_over()

        # TODO
        rpm.append((obs, action_index, reward, next_obs, done))

        # print("step:", step, "action:", action, "done:", done, end=' ')

        # 训练模型
        if (len(rpm) > MEMORY_WARMUP_SIZE) and (step % LEARN_FREQ == 0):
            s = rpm.sample(BATCH_SIZE)
            # print(s, end=' ')
            train_loss = agent.learn(*s)

        total_reward += reward
        obs = next_obs
        if done:
            # print("[finsh episode]")
            break

        # print("[finsh episode]")
        time.sleep(0.01)

    return total_reward


def evaluate(p, agent, render=False):
    """评估 agent, 跑 5 个episode，总reward求平均"""
    eval_reward = []
    for i in range(5):
        obs = list(p.getGameState().values())
        episode_reward = 0
        while True:
            action_index = agent.sample(obs)
            # 采样动作，所有动作都有概率被尝试到
            action = p.getActionSet()[action_index]

            # 行动
            next_obs, reward = list(p.getGameState().values()), p.act(action)
            episode_reward += reward

            if render:
                p.getScreenRGB()
            if p.game_over():
                break

        eval_reward.append(episode_reward)
    return np.mean(eval_reward)


# 创建环境
env = FlappyBird()
p = PLE(env, fps=30, display_screen=True, force_fps=True)
action_dim = len(p.getActionSet())
obs_shape = len(p.getGameState())

# 创建经验池
rpm = ReplayMemory(MEMORY_SIZE)

# 根据parl框架构建agent
model = Model(act_dim=action_dim)
algorithm = DQN(model, act_dim=action_dim, gamma=GAMMA, lr=LEARNING_RATE)
agent = Agent(
    algorithm,
    obs_dim=obs_shape,
    act_dim=action_dim,
    e_greed=0.001,
    e_greed_decrement=1e-6
)

# 加载模型
# save_path = 'model_dir/steps_5000.ckpt'
# agent.restore(save_path)

# 先往经验池里存一些数据，避免最开始训练的时候样本丰富度不够
warmup_count = 0
while len(rpm) < MEMORY_WARMUP_SIZE:
    r = run_episode(p, agent, rpm)
    # print("warmup_count:{}, r:{}".format(warmup_count, r))
    warmup_count += 1
# print('Finish Warmup')

max_episode = 50000

# 开始训练
episode = 0
# 训练max_episode个回合，test部分不计算入episode数量
while episode < max_episode:
    # train part
    for i in range(0, 50):
        total_reward = run_episode(p, agent, rpm)
        episode += 1

    # test part
    eval_reward = evaluate(p, agent, render=True)
    logger.info('episode: {}, e_greed: {}, test_reward: {}'.format(episode, agent.e_greed, eval_reward))

    # 训练结束，保存模型
    ckpt = 'model_dir/steps_{}.ckpt'.format(episode)
    agent.save(ckpt)
