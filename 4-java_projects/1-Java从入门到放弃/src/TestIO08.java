import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO08.java
 * @time: 2019/10/17 18:10
 * @desc: 文件字节输出流
 */

public class TestIO08 {
    public static void main(String[] args){
        // 1. 创建源
        File dest = new File("dest.txt");
        // 2. 选择流
        OutputStream os = null;
        try{
            // true则是增加，false则是不增加
            os = new FileOutputStream(dest, true);
            // 3. 操作（写出）
            String temp = "IO is so easy！";
            byte[] datas = temp.getBytes();
            os.write(datas, 0, datas.length);
            os.flush();
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }finally{
            // 释放资源
            if(null != os){
                try {
                    os.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}
