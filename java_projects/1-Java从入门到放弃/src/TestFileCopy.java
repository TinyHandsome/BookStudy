import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestFileCopy.java
 * @time: 2019/10/17 18:22
 * @desc: 文件的拷贝
 */

public class TestFileCopy {
    public static void main(String[] args) {
        copy("test.png", "copy_test.png");
    }

    public static void copy(String srcPath, String destPath){
        // 1. 创建源
        // 源头
        File src = new File(srcPath);
        File dest = new File(destPath);
        // 2. 选择流
        InputStream is = null;
        OutputStream os = null;
        try{
            is = new FileInputStream(src);
            os = new FileOutputStream(dest, true);
            // 3. 操作（分段读取）
            // 缓冲容器
            byte[] flush = new byte[1024];
            // 接受长度
            int len = -1;
            while((len=is.read(flush)) != -1){
                // 字节数组 --> 字符串（解码）
                String str = new String(flush, 0, len);
                os.write(flush, 0, len);
            }
            os.flush();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // 释放资源 先打开的后关闭
            try{
                if(null != os){
                    os.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

            try{
                if(null != is){
                    is.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
