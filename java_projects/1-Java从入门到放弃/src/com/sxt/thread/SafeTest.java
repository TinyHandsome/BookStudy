package com.sxt.thread;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: UnsafeTest.java
 * @time: 2019/11/4 13:57
 * @desc: 线程同步
 */

public class SafeTest {
    public static void main(String[] args) {
        // 账户
        Account account = new Account(100, "结婚礼金");
        SafeDrawing you = new SafeDrawing(account, 80, "可悲的你");
        SafeDrawing wife = new SafeDrawing(account, 90, "happy的她");
        you.start();
        wife.start();
    }
}

// 模拟取款
class SafeDrawing extends Thread {
    // 取钱的账户
    Account accout;
    // 取多少钱
    int drawingMoney;
    // 口袋里的总数
    int packetTotal;

    public SafeDrawing(Account accout, int drawingMoney, String name) {
        super(name);
        this.accout = accout;
        this.drawingMoney = drawingMoney;
    }

    @Override
    public void run() {
        test();
    }

    public void test() {
        if (accout.money <= 0) {
            return;
        }
        synchronized (accout) {
            if (accout.money - drawingMoney < 0) {
                return;
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            accout.money -= drawingMoney;
            packetTotal += drawingMoney;
            System.out.println(this.getName() + "-->账户余额为：" + accout.money);
            System.out.println(this.getName() + "-->口袋里的钱为：" + packetTotal);
        }
    }
}