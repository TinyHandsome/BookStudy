package com.sxt.others;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ThreadLocalTest4.java
 * @time: 2019/11/11 10:25
 * @desc: InheritableThreadLocal：继承上下文环境的数据，拷贝一份给子线程。起点
 */

public class ThreadLocalTest4 {
    private static ThreadLocal<Integer> threadLocal = new InheritableThreadLocal<>();

    public static void main(String[] args) {
        threadLocal.set(2);
        System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());

        // 线程由main线程开辟
        new Thread(() -> {
            System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());
            // 但是既然是拷贝，所以想改还是互不影响的
            threadLocal.set(200);
            System.out.println(Thread.currentThread().getName() + "-->" + threadLocal.get());
        }).start();
    }
}
