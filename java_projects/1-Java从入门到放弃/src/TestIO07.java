import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO07.java
 * @time: 2019/10/17 16:39
 * @desc: 读入字符数组
 */

public class TestIO07 {
    public static void main(String[] args){
        // 1. 创建源
        File src = new File("abc.txt");
        // 2. 选择流
        InputStream is = null;
        try{
            is = new FileInputStream(src);
            // 3. 操作（读取）
            // 缓冲容器，这里设为3个字节
            byte[] car = new byte[3];
            // 接受长度
            int len = -1;
            while((len=is.read(car)) != -1){
                // 字节数组 --> 字符串（解码）
                String str = new String(car, 0, len);
                System.out.println(str);
            }
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }finally{
            // 4. 释放资源
            if (null != is) {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
