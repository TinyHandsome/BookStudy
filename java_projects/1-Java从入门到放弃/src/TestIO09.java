import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO07.java
 * @time: 2019/10/17 16:39
 * @desc: 文件字符输入流
 */

public class TestIO09 {
    public static void main(String[] args){
        // 1. 创建源
        File src = new File("abc.txt");
        // 2. 选择流
        Reader reader = null;
        try{
            reader = new FileReader(src);
            // 3. 操作（读取）
            char[] flush = new char[1024];
            // 接受长度
            int len = -1;
            while((len=reader.read(flush)) != -1){
                String str = new String(flush, 0, len);
                System.out.println(str);
            }
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }finally{
            // 4. 释放资源
            if (null != reader) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
