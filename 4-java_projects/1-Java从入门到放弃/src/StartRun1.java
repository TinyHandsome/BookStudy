/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ThreadStudy01.java
 * @time: 2019/10/25 12:37
 * @desc: 进程学习3
 */

public class StartRun1 implements Runnable {

    public void run() {
        for (int i = 0; i < 20; i++) {
            System.out.println("一边听歌一边敲代码。");
        }
    }

    public static void main(String[] args) throws InterruptedException {
        /*
        // 创建实现类对象
        StartRun1 sr = new StartRun1();
        // 创建代理类对象
        Thread t = new Thread(sr);
        // 启动
        t.start();
        // run是普通方法的调用
//        st.run();
        */

        // 利用匿名对象
        new Thread(new StartRun1()).start();

        for (int i = 0; i < 20; i++) {
            System.out.println("coding。");
            Thread.sleep(1);
        }
    }
}
