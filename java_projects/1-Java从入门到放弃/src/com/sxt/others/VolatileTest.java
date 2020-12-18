package com.sxt.others;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: VolatileTest.java
 * @time: 2019/11/11 9:29
 * @desc: volatile测试
 * 不加volatile则程序不会停，加了之后会停
 */

public class VolatileTest {
    private volatile static int num = 0;
    public static void main(String[] args) throws InterruptedException {
        new Thread(() -> {
            while(num == 0){
                // 此处不要编写代码，这是为了让系统没有时间更新数据
            }
        }).start();

        Thread.sleep(1000);
        num = 1;
    }
}
