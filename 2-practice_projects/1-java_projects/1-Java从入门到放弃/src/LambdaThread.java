/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LambdaThread.java
 * @time: 2019/10/30 16:00
 * @desc: Lambda表达式 简化线程（用一次）的使用
 */

public class LambdaThread {
    // 类中类：静态内部类
    static class Test implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < 10; i++) {
                System.out.println("一边听歌");
            }
        }
    }

    public static void main(String[] args) {
        new Thread(new Test()).start();

        // 方法中类：局部内部类
        class Test2 implements Runnable {
            @Override
            public void run() {
                for (int i = 0; i < 10; i++) {
                    System.out.println("一边听歌");
                }
            }
        }
        new Thread(new Test2()).start();

        // 参数中类：匿名内部类
        new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 20; i++) {
                    System.out.println("一边听歌");
                }
            }
        }).start();

        // jdk8简化匿名内部类，lambda
        new Thread(
                () -> {
                    for (int i = 0; i < 20; i++) {
                        System.out.println("一边听歌");
                    }
                }
        ).start();
    }
}
