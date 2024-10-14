import java.io.File;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: pycharm
 * @file: FileTest1.java
 * @time: 2019/9/22 15:09
 * @desc: File类的常见构造方法
 */

public class FileTest1{
    public static void main(String[] args) throws Exception{
        test2();
    }

    public static void test1() throws Exception{
        System.out.println(System.getProperty("user.dir"));

        // 相对路径，默认放到user.dir目录下
        File f = new File("a.txt");
        // 创建文件
        f.createNewFile();
        // 绝对路径
        File f2 = new File("D:\\李添的数据哦！！！\\BookStudy\\else\\JavaWorkSpace\\b.txt");
        f2.createNewFile();
    }

    public static void test2() throws Exception{
        File f = new File("d:/c.txt");
        f.createNewFile(); // 会在d盘下面生成c.txt文件
        f.delete(); // 将该文件或目录从硬盘上删除
        File f2 = new File("d:/电影/华语/大陆");
        boolean flag = f2.mkdir(); //目录结构中有一个不存在，则不会创建整个目录树
        System.out.println(flag);//创建失败
    }

}
