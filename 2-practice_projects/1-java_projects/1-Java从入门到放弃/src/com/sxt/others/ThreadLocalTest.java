package com.sxt.others;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ThreadLocalTest.java
 * @time: 2019/11/11 9:52
 * @desc: ThreadLocal
 */

public class ThreadLocalTest {
    //    private static ThreadLocal<Integer> threadLocal = new ThreadLocal<>();
    // 更改初始值
//    private static ThreadLocal<Integer> threadLocal = new ThreadLocal<Integer>(){
//        @Override
//        protected Integer initialValue() {
//            return 200;
//        }
//    };
    // 简化上面代码
    private static ThreadLocal<Integer> threadLocal = ThreadLocal.withInitial(() -> 200);


    public static void main(String[] args) {
        // 获取值，初始值为null
        System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());
        // 设置值
        threadLocal.set(99);
        System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());

        new Thread(new MyRun()).start();
        new Thread(new MyRun()).start();
    }

    public static class MyRun implements Runnable {
        @Override
        public void run() {
            threadLocal.set((int)(Math.random()*99));
            System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());
        }
    }
}

