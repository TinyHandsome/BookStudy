package com.sxt.others;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ThreadLocalTest2.java
 * @time: 2019/11/11 10:06
 * @desc: 取数据
 */

public class ThreadLocalTest2 {
    private static ThreadLocal<Integer> threadLocal = ThreadLocal.withInitial(() -> 1);

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            new Thread(new MyRun()).start();
        }
    }

    public static class MyRun implements Runnable {
        @Override
        public void run() {
            Integer left = threadLocal.get();
            System.out.println(Thread.currentThread().getName() + "得到了-->" + left);
            threadLocal.set(left - 1);
            System.out.println(Thread.currentThread().getName() + "还剩下-->" + threadLocal.get());
        }
    }
}
