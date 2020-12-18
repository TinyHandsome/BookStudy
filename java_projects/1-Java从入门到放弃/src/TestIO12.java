import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO08.java
 * @time: 2019/10/17 18:10
 * @desc: 字节数组输出流
 */

public class TestIO12 {
    public static void main(String[] args){
        // 1. 创建源：不用创建源
        byte[] dest = null;
        // 2. 选择流：新增方法
        ByteArrayOutputStream baos = null;
        try{
            // true则是增加，false则是不增加
            baos = new ByteArrayOutputStream();
            // 3. 操作（写出）
            String temp = "show me the code bie bibi";
            byte[] datas = temp.getBytes();
            baos.write(datas, 0, datas.length);
            baos.flush();
            // 获取数据
            dest = baos.toByteArray();
            System.out.println(dest.length + "-->" + new String(dest, 0, baos.size()));
        } catch(IOException e){
            e.printStackTrace();
        } finally{
            // 释放资源
            if(null != baos){
                try {
                    baos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}
