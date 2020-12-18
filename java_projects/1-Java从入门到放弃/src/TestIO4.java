import java.io.File;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO4.java
 * @time: 2019/10/15 15:20
 * @desc: 统计文件夹的大小
 */

public class TestIO4 {
    public static void main(String[] args){
        File src = new File("F:\\BookStudy");
        count(src);
        System.out.println(LEN);
    }

    private static long LEN = 0;
    public static void count(File src){
        // 获取大小
        if(null != src && src.exists()){
            if(src.isFile()){
                LEN += src.length();
            }else{
                for(File s: src.listFiles()){
                    count(s);
                }
            }
        }
    }
}
