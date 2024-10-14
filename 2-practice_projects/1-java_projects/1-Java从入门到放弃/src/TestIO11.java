import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO07.java
 * @time: 2019/10/17 16:39
 * @desc: 字节数组输入流
 */

public class TestIO11 {
    public static void main(String[] args){
        // 1. 创建源
        byte[] src = "talk is cheap show me the code. ".getBytes();
        // 2. 选择流
        InputStream is = null;
        try{
            is = new ByteArrayInputStream(src);
            // 3. 操作（读取）
            // 缓冲容器，这里设为5个字节
            byte[] car = new byte[5];
            // 接受长度
            int len = -1;
            while((len=is.read(car)) != -1){
                // 字节数组 --> 字符串（解码）
                String str = new String(car, 0, len);
                System.out.println(str);
            }
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
