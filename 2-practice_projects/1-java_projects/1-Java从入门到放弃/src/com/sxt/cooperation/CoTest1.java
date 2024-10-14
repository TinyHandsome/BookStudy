package com.sxt.cooperation;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CoTest1.java
 * @time: 2019/11/8 15:36
 * @desc: 协作模型：生产者消费者实现方式1：管程法
 */

public class CoTest1 {
    public static void main(String[] args) {
        SynContainer container = new SynContainer();
        new Productor(container).start();
        new Consumer(container).start();
    }
}

// 生产者
class Productor extends Thread {
    SynContainer container;

    public Productor(SynContainer container) {
        this.container = container;
    }

    @Override
    public void run() {
        // 开始生产
        for (int i = 0; i < 100; i++) {
            System.out.println("生产-->第" + i + "个馒头");
            container.push(new SteamedBun(i));
        }
    }
}

// 消费者
class Consumer extends Thread {
    SynContainer container;

    public Consumer(SynContainer container) {
        this.container = container;
    }

    @Override
    public void run() {
        // 开始消费
        for (int i = 0; i < 1000; i++) {
            System.out.println("消费-->第" + container.pop().id + "个馒头");
        }
    }
}

// 缓冲区
class SynContainer {
    SteamedBun[] buns = new SteamedBun[10];
    int count = 0;

    // 存储：生产
    public synchronized void push(SteamedBun bun) {
        // 何时能生产：容器存在空间
        if (count == buns.length) {
            try {
                // 线程阻塞，消费者通知生产解除
                this.wait();
            } catch (InterruptedException e) {
            }
        }
        // 存在空间，可以生产
        buns[count++] = bun;
        // 存在数据了，可以通知消费了
        this.notifyAll();
    }

    // 获取：消费
    public synchronized SteamedBun pop() {
        // 何时消费：容器中是否存在数据，存在数据则可以消费，没有数据就只能等待
        if (count == 0) {
            try {
                // 线程阻塞：生产者通知消费则接触阻塞
                this.wait();
            } catch (InterruptedException e) {
            }
        }
        SteamedBun bun = buns[--count];
        // 存在空间，可以唤醒对方生产
        this.notifyAll();
        return bun;
    }
}

// 数据。馒头
class SteamedBun {
    int id;

    public SteamedBun(int id) {
        this.id = id;
    }
}