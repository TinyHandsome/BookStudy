import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO07.java
 * @time: 2019/10/17 16:39
 * @desc: 加入缓冲流
 */

public class BufferedTest01 {
    public static void main(String[] args){
        // 1. 创建源
        File src = new File("abc.txt");
        // 2. 选择流
        InputStream is = null;
        BufferedInputStream bis = null;
        try{
            is = new FileInputStream(src);
            bis = new BufferedInputStream(is);
            // 3. 操作（读取）
            byte[] flush = new byte[1024];
            // 接受长度
            int len = -1;
            while((len=is.read(flush)) != -1){
                // 字节数组 --> 字符串（解码）
                String str = new String(flush, 0, len);
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
            if (null != bis) {
                try {
                    bis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
