import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: PrintTest2.java
 * @time: 2019/10/20 15:43
 * @desc: 打印流
 */

public class PrintTest2 {
    public static void main(String[] args) throws FileNotFoundException {

        PrintWriter pw = new PrintWriter(
                new BufferedOutputStream(
                        new FileOutputStream("print.txt")
                ), true
        );
        pw.println("打印流");
        pw.println(true);
        pw.close();
    }
}
