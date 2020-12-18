import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO08.java
 * @time: 2019/10/17 18:10
 * @desc: 文件字符输出流
 */

public class TestIO10 {
    public static void main(String[] args){
        // 1. 创建源
        File dest = new File("dest.txt");
        // 2. 选择流
        Writer writer = null;
        try{
            // true则是增加，false则是不增加
            writer = new FileWriter(dest, false);
            // 3. 操作（写出）

            // 写法1
//            String temp = "IO is so easy！我是你大爷";
//            char[] datas = temp.toCharArray();
//            writer.write(datas, 0, datas.length);
//            writer.flush();

            // 写法2
//            String temp = "IO is so easy！我是你大爷";
//            writer.write(temp);
//            writer.flush();

            // 写法3
            writer.append("IO is so easy！").append("我是你大爷");
            writer.flush();

        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }finally{
            // 释放资源
            if(null != writer){
                try {
                    writer.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}
