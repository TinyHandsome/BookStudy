package com.sxt.others;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ThreadLocalTest3.java
 * @time: 2019/11/11 10:11
 * @desc: 分析上下文环境
 */

public class ThreadLocalTest3 {
    private static ThreadLocal<Integer> threadLocal = ThreadLocal.withInitial(() -> 1);

    public static void main(String[] args) {
        new Thread(new MyRun()).start();
        new Thread(new MyRun()).start();
    }

    public static class MyRun implements Runnable {
        public MyRun() {
            // 属于main线程
            threadLocal.set(-100);
            System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());
        }

        @Override
        public void run() {
            // 属于其他线程
            System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());
        }
    }
}

