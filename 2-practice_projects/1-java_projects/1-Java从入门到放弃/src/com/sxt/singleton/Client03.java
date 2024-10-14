package com.sxt.singleton;

import java.util.concurrent.CountDownLatch;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/3 20:13
 * @desc: 测试五种创建单例模式的效率
 */

public class Client03 {
    public static void main(String[] args) throws Exception {

        long start = System.currentTimeMillis();
        int threadNum = 10;
        final CountDownLatch countDownLatch = new CountDownLatch(threadNum);
        for (int i = 0; i < threadNum; i++) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    for (int i = 0; i < 100000; i++) {
//                        Object o = SingletonDemo04.getInstance();
                        Object o = SingletonDemo05.INSTANCE;
                    }
                    countDownLatch.countDown();
                }
            }).start();
        }
        // main线程阻塞，直到计数器变为0，才会继续往下执行！
        countDownLatch.await();
        long end = System.currentTimeMillis();
        System.out.println("总耗时：" + (end - start));
    }
}
