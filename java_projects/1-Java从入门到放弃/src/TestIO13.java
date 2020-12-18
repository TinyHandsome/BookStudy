import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO08.java
 * @time: 2019/10/17 18:10
 * @desc: 图片读取到字节数组，字节数组写出到文件
 */

public class TestIO13 {
    public static void main(String[] args){
        byte[] datas = fileToByteArray("test.png");
        System.out.println(datas.length);
        byteArrayToFile(datas, "p-byte.png");
    }

    public static byte[] fileToByteArray(String filePath){
        /*
          1. 图片读取到字节数组中
          1). 图片到程序：FileInputStream
          2). 程序到字节数组：ByteArrayOutputStream
         */

        // 1. 创建源与目的地
        File src = new File(filePath);
        byte[] dest = null;
        // 2. 选择流
        InputStream is = null;
        ByteArrayOutputStream baos = null;
        try{
            is = new FileInputStream(src);
            baos = new ByteArrayOutputStream();
            // 3. 操作：分段读取
            byte[] flush = new byte[1024*10];
            int len = -1;
            while((len = is.read(flush)) != -1){
                baos.write(flush, 0, len);      // 写出到字节数组中
            }
            baos.flush();
            return baos.toByteArray();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            // 4. 释放资源
            try{
                if(null != is){
                    is.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return null;
    }

    public static void byteArrayToFile(byte[] src, String filePath){
        /*
        2. 字节数组写出到文件
        1). 字节数组到程序：ByteArrayInputStream
        2). 程序写出到文件：FileOutputStream
         */
        // 1. 创建源
        File dest = new File(filePath);
        // 2. 选择流
        InputStream is = null;
        OutputStream os = null;
        try{
            is = new ByteArrayInputStream(src);
            os = new FileOutputStream(dest, false);
            // 3. 操作：分段读取
            byte[] flush = new byte[5];     // 缓冲容器
            int len = -1;
            while((len = is.read(flush)) != 1){
                os.write(flush, 0, len);
            }
            os.flush();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // 4. 释放资源
            try {
                if (null != os) {
                    os.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
