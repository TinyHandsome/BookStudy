#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: attention_train.py
@time: 2019/4/29 16:14
@desc: 注意力机制需要修改训练中的代码
"""

import tensorflow as tf
from statistic_word3 import MakeSrcTrgDataset


root_path = "D:/Python3Space/Seq2SeqLearning/"
# 输入数据已经转换成了单词编号的格式。
# 源语言输入文件
SRC_TRAIN_DATA = root_path + "en.number"
# 目标语言输入文件
TRG_TRAIN_DATA = root_path + "zh.number"
# checkpoint保存路径
CHECKPOINT_PATH = root_path + "attention_ckpt"
# LSTM的隐藏层规模
HIDDEN_SIZE = 1024
# 深层循环神经网络中LSTM结构的层数
NUM_LAYERS = 2
# 源语言词汇表大小
SRC_VOCAB_SIZE = 10000
# 目标语言词汇表大小
TRG_VOCAB_SIZE = 4000
# 训练数据batch的大小
BATCH_SIZE = 100
# 使用训练数据的轮数
NUM_EPOCH = 5
# 节点不被dropout的概率
KEEP_PROB = 0.8
# 用于控制梯度膨胀的梯度大小上限
MAX_GRAD_NROM = 5
# 在Softmax层和词向量层之间共享参数
SHARE_EMB_AND_SOFTMAX = True


# 定义NMTModel类来描述模型，attention模型中 编码器双向循环，解码器单向循环
class NMTModel(object):
    # 在模型的初始化函数中定义模型要用到的变量
    def __init__(self):
        # 定义编码器和解码器所使用的LSTM结构
        # 前向
        self.enc_cell_fw = tf.nn.rnn_cell.LSTMCell(HIDDEN_SIZE)
        # 反向
        self.enc_cell_bw = tf.nn.rnn_cell.LSTMCell(HIDDEN_SIZE)

        self.dec_cell = tf.nn.rnn_cell.MultiRNNCell([tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE) for _ in range(NUM_LAYERS)])

        # 为源语言和目标语言分别定义词向量
        self.src_embedding = tf.get_variable("src_emb", [SRC_VOCAB_SIZE, HIDDEN_SIZE])
        self.trg_embedding = tf.get_variable("trg_emb", [TRG_VOCAB_SIZE, HIDDEN_SIZE])

        # 定义softmax层的变量，只有解码器需要用到softmax
        if SHARE_EMB_AND_SOFTMAX:
            self.softmax_weight = tf.transpose(self.trg_embedding)
        else:
            self.softmax_weight = tf.get_variable("weight", [HIDDEN_SIZE, TRG_VOCAB_SIZE])
        self.softmax_bias = tf.get_variable("softmax_bias", [TRG_VOCAB_SIZE])

    # 在forward函数中定义模型的前向计算图
    # src_input, src_size, trg_input, trg_label, trg_size分别是上面MakeSrcTrgDataset函数产生的五种张量
    def forward(self, src_input, src_size, trg_input, trg_label, trg_size):
        batch_size = tf.shape(src_input)[0]

        # 将输入和输出单词编号转为词向量
        src_emb = tf.nn.embedding_lookup(self.src_embedding, src_input)
        trg_emb = tf.nn.embedding_lookup(self.trg_embedding, trg_input)

        # 在词向量上进行dropout
        src_emb = tf.nn.dropout(src_emb, KEEP_PROB)
        trg_emb = tf.nn.dropout(trg_emb, KEEP_PROB)

        # 使用dynamic构造编码器
        # 编码器读取源句子每个位置的词向量，输出最后一步的隐藏状态enc_state
        # 因为编码器是一个双层LSTM，因此enc_state是一个包含两个LSTMStateTuple类的tuple，每个LSTMStateTuple对应编码器中一层的状态。
        # enc_outputs是顶层LSTM在每一步的输出，它的维度是[batch_size, max_time, HIDDEN_SIZE]。
        # Seq2Seq模型中不需要用到enc_outputs，而在后面介绍的attention模型中会用到它。
        with tf.variable_scope("encoder"):
            # 构造编码器时，使用bidirectional_dynamic_rnn构造双向循环网络。
            # 双向循环网络的顶层输出enc_outputs是一个包含两个张量的tuple，每个张量的
            # 维度都是[batch_size, max_time, HIDDEN_SIZE]，代表两个LSTM在每一步的输出。
            enc_outputs, enc_state = tf.nn.bidirectional_dynamic_rnn(self.enc_cell_fw, self.enc_cell_bw, src_emb, src_size, dtype=tf.float32)
            # 将两个LSTM的输出拼接为一个张量。
            enc_outputs = tf.concat([enc_outputs[0], enc_outputs[1]], -1)

        # 使用dynamic_rnn构造解码器
        # 解码器读取目标句子每个位置的词向量，输出的dec_outputs为每一步顶层LSTM的输出。
        # dec_outputs的维度是[batch_size, max_time, HIDDEN_SIZE]
        # initial_state=enc_state表示用编码器的输出来初始化第一步的隐藏状态。
        with tf.variable_scope("decoder"):
            # 选择注意力权重的计算模型。BahdanauAttention是使用一个隐藏层的前馈网络。
            # memory_sequence_length是一个维度为[batch_size]的张量，代表batch
            # 中每个句子的长度，Attention需要根据这个信息把填充位置的注意力权重设置为0。
            attention_mechanism = tf.contrib.seq2seq.BahdanauAttention(HIDDEN_SIZE, enc_outputs, memory_sequence_length=src_size)

            # 将解码器的循环神经网络self.dec_cell和注意力一起封装成更高层的循环神经网络。
            attention_cell = tf.contrib.seq2seq.AttentionWrapper(self.dec_cell, attention_mechanism, attention_layer_size=HIDDEN_SIZE)

            # 使用attention_cell和dynamic_rnn构造编码器。
            # 这里没有指定init_state，也就是没有使用编码器的输出来初始化输入，而完全依赖注意力作为信息来源。
            dec_outputs, _ = tf.nn.dynamic_rnn(attention_cell, trg_emb, trg_size, dtype=tf.float32)

        # 计算解码器每一步的log perplexity。这一步与语言模型的代码相同。
        output = tf.reshape(dec_outputs, [-1, HIDDEN_SIZE])
        logits = tf.matmul(output, self.softmax_weight) + self.softmax_bias
        loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.reshape(trg_label, [-1]), logits=logits)

        # 在计算平均损失时，需要将填充位置的权重设置为0，以避免无效位置的预测干扰模型的训练。
        label_weights = tf.sequence_mask(trg_size, maxlen=tf.shape(trg_label)[1], dtype=tf.float32)
        label_weights = tf.reshape(label_weights, [-1])
        cost = tf.reduce_sum(loss * label_weights)
        cost_per_token = cost / tf.reduce_sum(label_weights)

        # 定义反向传播操作。反向操作的实现与语言模型代码相同。
        trainable_variables = tf.trainable_variables()

        # 控制梯度大小，定义优化方法和训练步骤。
        grads = tf.gradients(cost / tf.to_float(batch_size), trainable_variables)
        grads, _ = tf.clip_by_global_norm(grads, MAX_GRAD_NROM)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0)
        train_op = optimizer.apply_gradients(zip(grads, trainable_variables))
        return cost_per_token, train_op


# 使用给定的模型model上训练一个epoch，并返回全局步数
# 每训练200步便保存一个checkpoint
def run_epoch(session, cost_op, train_op, saver, step):
    # 训练一个epoch
    # 重复训练步骤直至遍历完Dataset中所有数据。
    while True:
        try:
            # 运行train_op并计算损失值。训练数据在main()函数中以Dataset方式提供
            cost, _ = session.run([cost_op, train_op])
            if step % 10 == 0:
                print("After %d steps, per token cost is %.3f" % (step, cost))
            # 每200步保存一个checkoutpoint
            if step % 200 == 0:
                saver.save(session, CHECKPOINT_PATH, global_step=step)
            step += 1
        except tf.errors.OutOfRangeError:
            break
    return step


def main():
    # 定义初始化函数
    initializer = tf.random_uniform_initializer(-0.05, 0.05)

    # 定义训练用的循环神经网络模型
    with tf.variable_scope("nmt_model", reuse=None, initializer=initializer):
        train_model = NMTModel()

    # 定义输入数据
    data = MakeSrcTrgDataset(SRC_TRAIN_DATA, TRG_TRAIN_DATA, BATCH_SIZE)
    iterator = data.make_initializable_iterator()
    (src, src_size), (trg_input, trg_label, trg_size) = iterator.get_next()

    # 定义前向计算图。输入数据以张量形式提供给forward函数。
    cost_op, train_op = train_model.forward(src, src_size, trg_input, trg_label, trg_size)

    # 训练模型
    saver = tf.train.Saver()
    step = 0
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        for i in range(NUM_EPOCH):
            print("In iteration: %d" % (i + 1))
            sess.run(iterator.initializer)
            step = run_epoch(sess, cost_op, train_op, saver, step)


if __name__ == "__main__":
    main()