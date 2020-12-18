import java.io.File;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO1.java
 * @time: 2019/10/9 17:19
 * @desc: IO学习1
 */

public class TestIO1 {
    public static void main(String[] args){

        // 输出文件分隔符
        System.out.println(File.separator);

        // 1. 构建File对象
        String path = "F:/BookStudy/else/Java知识点思维导图.png";
        File src = new File(path);

        // 输出文件大小
        System.out.println(src.length());

        // 2. 第二种构建File对象的方法
        File src2 = new File("F:/BookStudy/else", "Java知识点思维导图.png");
        System.out.println(src2.length());

        // 3. 第三种构建File对象的方法
        File src3 = new File(new File("F:/BookStudy/else"), "Java知识点思维导图.png");
        System.out.println(src3.length());

        // 相对路径的源路径
        System.out.println(System.getProperty("user.dir"));

        // 绝对路径
        System.out.println(src3.getAbsolutePath());

        // 构建一个不存在的对象
        File src4 = new File("aaa/asdf.jpg");
        System.out.println(src4.getAbsolutePath());

    }
}
