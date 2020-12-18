import org.omg.PortableServer.THREAD_POLICY_ID;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: YieldDemo1.java
 * @time: 2019/11/1 14:55
 * @desc: yield礼让线程，暂停线程，直接进入就绪状态不是阻塞状态
 */

public class YieldDemo1 {
    public static void main(String[] args) {
        MyYield my = new MyYield();
        new Thread(my, "a").start();
        new Thread(my, "b").start();

        // lambda实现
        new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                System.out.println("lambda..." + i);
            }
        }).start();
        for (int i = 0; i < 100; i++) {
            if (i % 20 == 0) {
                Thread.yield();     // main礼让
            }
            System.out.println("main..." + i);
        }
    }
}

class MyYield implements Runnable {
    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + "-->start");
        Thread.yield();     // 礼让
        System.out.println(Thread.currentThread().getName() + "-->end");
    }
}