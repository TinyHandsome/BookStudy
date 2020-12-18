/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LambdaTest1.java
 * @time: 2019/10/31 15:18
 * @desc: lambda推导实现线程
 */

public class LambdaTest4 {
    public static void main(String[] args) {
        new Thread(() -> {
            System.out.println("一边学习lambda");
        }).start();

        // 简化：花括号可以不要
        new Thread(() -> System.out.println("一边泪流满面")).start();

        // 如果是多个语句，就不能省略
        new Thread(() -> {
            for (int i = 0; i < 20; i++) {
                System.out.println("我疯了，你呢？");
            }
        }).start();
    }
}
