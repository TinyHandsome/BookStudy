/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ThreadStudy01.java
 * @time: 2019/10/25 12:37
 * @desc: 进程学习1
 */

public class StartThread1 extends Thread{

    public void run(){
        for (int i = 0; i < 20; i++) {
            System.out.println("一边听歌一边敲代码。");
        }
    }

    public static void main(String[] args) throws InterruptedException {
        // 创建子类对象
        StartThread1 st = new StartThread1();
        // 启动
        st.start();
        // run是普通方法的调用
//        st.run();
        for (int i = 0; i < 20; i++) {
            System.out.println("coding。");
            Thread.sleep(1);
        }
    }
}
