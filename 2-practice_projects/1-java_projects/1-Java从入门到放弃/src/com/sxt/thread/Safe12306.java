package com.sxt.thread;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Web12306.java
 * @time: 2019/10/30 12:36
 * @desc: 线程安全买票
 */

public class Safe12306 implements Runnable {
    // 票数
    private int ticketNums = 10;
    private boolean flag = true;

    @Override
    public void run() {
        while (flag) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            test();
        }
    }

    private void test() {
        if (ticketNums <= 0) {  // 考虑的是没有票的情况
            flag = false;
            return;
        }
        synchronized (this) {
            if (ticketNums <= 0) {  // 考虑的是最后一张票的情况
                flag = false;
                return;
            }
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "-->" + ticketNums--);
        }
    }

    public static void main(String[] args) {
        // 一份资源
        Safe12306 web = new Safe12306();
        // 多个代理
        new Thread(web, "张三").start();
        new Thread(web, "李四").start();
        new Thread(web, "王五").start();
    }
}
