import java.io.File;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO3.java
 * @time: 2019/10/11 17:50
 * @desc: 文件夹创建和遍历
 */

public class TestIO3 {
    public static void main(String[] args){
        // mkdir()：确保上级目录存在，不存在则创建失败
        // mkdirs()：上级目录可以不存在，不存在则一同创建
        File dir = new File("D:/");

        boolean flag1 = dir.mkdir();
        boolean flag2 = dir.mkdirs();
        System.out.println(flag1);
        System.out.println(flag2);

        // list()：列出下级名称
        // listFiles()：列出下级File对象
        String[] subNames = dir.list();
        for(String s: subNames){
            System.out.println(s);
        }

        File[] subFiles = dir.listFiles();
        for(File s: subFiles){
            System.out.println(s.getAbsolutePath());
        }

        // listRoots()：列出所有盘符
        File[] roots = dir.listRoots();
        for(File r: roots){
            System.out.println(r.getAbsolutePath());
        }

        // 递归：方法自己调用自己
        // 递归头：何时结束递归
        // 递归体：重复调用
        printName(dir, 0);

    }

    public static void printName(File src, int deep){
        /* 打印子孙级目录和文件的名称 */
        for(int i=0; i<deep; i++){
            System.out.print("-");
        }
        System.out.println(src.getName());
        if(null == src || !src.exists()){
            return;
        } else if(src.isDirectory()){
            for(File s: src.listFiles()){
                printName(s, deep + 1);
            }
        }
    }
}
