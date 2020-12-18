import java.io.File;
import java.io.IOException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO2.java
 * @time: 2019/10/11 17:31
 * @desc: IO操作api
 */

public class TestIO2 {
    public static void main(String[] args) throws IOException {
        File src = new File("F:/BookStudy/else/Java知识点思维导图.png");

        // 基本信息
        System.out.println("名称：" + src.getName());
        System.out.println("路径：" + src.getPath());
        System.out.println("绝对路径：" + src.getAbsolutePath());
        System.out.println("父路径：" + src.getParent());
        System.out.println("父对象：" + src.getParentFile().getName());

        // 文件状态
        System.out.println("是否存在：" + src.exists());
        System.out.println("是否文件：" + src.isFile());
        System.out.println("是否文件夹：" + src.isDirectory());

        // 获取文件的字节数，如果是文件夹，则为0。
        System.out.println("长度：" + src.length());

        // 创建文件：不存在才创建，返回true，不然返回false；不带后缀只是文件名，不是文件夹
        boolean flag = src.createNewFile();
        System.out.println(flag);

        // 文件的删除：删除已经存在的文件
        flag = src.delete();
        System.out.println(flag);

    }
}
