import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO05.java
 * @time: 2019/10/17 16:39
 * @desc: 理解操作步骤
 */

public class TestIO05 {
    public static void main(String[] args){
        // 1. 创建源
        File src = new File("abc.txt");
        // 2. 选择流
        try{
            InputStream is = new FileInputStream(src);
            System.out.println(src.getAbsolutePath());
            // 3. 操作（读取）
            int data1 = is.read();      // 第1个数据
            int data2 = is.read();      // 第2个数据
            int data3 = is.read();      // 第3个数据
            System.out.println((char)data1);
            System.out.println((char)data2);
            System.out.println((char)data3);
            // 4. 释放资源
            is.close();
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
