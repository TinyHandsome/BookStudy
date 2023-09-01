package com.sxt.others;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CASTest.java
 * @time: 2019/11/11 10:51
 * @desc: CAS
 */

public class CASTest {
    // 库存
    private static AtomicInteger stock = new AtomicInteger(3);
    public static void main(String[] args){
        for (int i = 0; i < 5; i++) {
            new Thread(()->{
                // 模拟网络延时
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                Integer left = stock.decrementAndGet();
                if(left<1){
                    System.out.println("抢完了...");
                    return;
                }
                System.out.println(Thread.currentThread().getName() + "抢了一个商品" + "-->还剩" + left);
            }).start();
        }
    }
}
