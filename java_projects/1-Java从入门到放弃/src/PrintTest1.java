import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: PrintTest1.java
 * @time: 2019/10/20 15:43
 * @desc: 打印流
 */

public class PrintTest1 {
    public static void main(String[] args) throws FileNotFoundException {
        // 打印流System.out
        PrintStream ps = System.out;
        ps.println("打印流");
        ps.println(true);

        ps = new PrintStream(
                new BufferedOutputStream(
                        new FileOutputStream("print.txt")
                ), true
        );
        ps.println("打印流");
        ps.println(true);
        ps.close();

        // 重定向输出端
        System.setOut(ps);
        System.out.println("change");
        // 重定向回控制台
        System.setOut(
                new PrintStream(
                        new BufferedOutputStream(
                                new FileOutputStream(FileDescriptor.out)
                        ), true
                )
        );
        System.out.println("i am backing...");
    }
}
