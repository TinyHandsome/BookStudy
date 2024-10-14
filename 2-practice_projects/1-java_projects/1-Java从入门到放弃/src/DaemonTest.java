import org.omg.PortableServer.THREAD_POLICY_ID;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DaemonTest.java
 * @time: 2019/11/4 13:35
 * @desc: 守护线程学习
 */

public class DaemonTest {
    public static void main(String[] args) {
        Thread t1 = new Thread(new You1());
        t1.run();
        Thread t2 = new Thread(new God1());
        // 将用户线程调整为守护线程
        t2.setDaemon(true);
        t2.start();
    }
}

class You1 extends Thread {
    @Override
    public void run() {
        for (int i = 0; i < 365 * 100; i++) {
            System.out.println("happy life!");
        }
        System.out.println("ooo...");
    }
}

class God1 extends Thread {
    @Override
    public void run() {
        for (;true;) {
            System.out.println("bless you!");
        }
    }
}

