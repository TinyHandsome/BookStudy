/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: InfoTest.java
 * @time: 2019/11/4 13:46
 * @desc: 获取线程基本信息的方法
 */

public class InfoTest {
    public static void main(String[] args) throws InterruptedException {
        // 线程是否活着
        System.out.println(Thread.currentThread().isAlive());
        // 设置名称：真是角色+代理角色
        MyInfo info = new MyInfo("战斗机");
        Thread t = new Thread(info);
        t.setName("公鸡");
        t.start();
        Thread.sleep(1000);
        System.out.println(t.isAlive());
    }
}

class MyInfo implements Runnable{
    private String name;
    public MyInfo(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + "-->" + name);
    }
}