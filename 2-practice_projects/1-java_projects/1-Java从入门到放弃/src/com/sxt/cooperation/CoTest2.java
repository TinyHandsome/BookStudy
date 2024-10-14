package com.sxt.cooperation;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CoTest2.java
 * @time: 2019/11/8 16:38
 * @desc: 信号灯法
 */

public class CoTest2 {
    public static void main(String[] args) {
        Tv tv = new Tv();
        new Player(tv).start();
        new Watcher(tv).start();
    }
}

// 生产者：演员
class Player extends Thread {
    Tv tv;

    public Player(Tv tv) {
        this.tv = tv;
    }

    @Override
    public void run() {
        for (int i = 0; i < 20; i++) {
            if (i % 2 == 0) {
                this.tv.play("奇葩说");
            } else {
                this.tv.play("倚天屠龙记");
            }
        }
    }
}

// 消费者：观众
class Watcher extends Thread {
    Tv tv;

    public Watcher(Tv tv) {
        this.tv = tv;
    }

    @Override
    public void run() {
        for (int i = 0; i < 20; i++) {
            tv.watch();
        }
    }
}

// 同一个资源：电视
class Tv {
    String voice;
    // T：演员表演，观众等待；F：观众观看，演员等待
    boolean flag = true;

    // 表演
    public synchronized void play(String voice) {
        // 演员等待
        if (!flag) {
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("表演了" + voice);
        this.voice = voice;
        // 唤醒
        this.notifyAll();
        this.flag = !this.flag;
    }

    // 观看
    public synchronized void watch() {
        // 观众等待
        if (flag) {
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("听到了" + voice);
        // 唤醒
        this.notifyAll();
        this.flag = !this.flag;
    }
}