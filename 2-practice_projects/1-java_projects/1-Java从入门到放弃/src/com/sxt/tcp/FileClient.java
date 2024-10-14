package com.sxt.tcp;

import java.io.*;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: FileClient.java
 * @time: 2019/11/18 15:32
 * @desc: 客户端：上传文件
 */

public class FileClient {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Client-----");
        //  1. 建立连接：使用Socket创建客户端 + 服务的地址和端口
        Socket client = new Socket("localhost", 8888);
        //  2. 操作：文件拷贝 上传
        InputStream is = new BufferedInputStream(new FileInputStream("./快乐.jpg"));
        OutputStream os = new BufferedOutputStream(client.getOutputStream());
        byte[] flush = new byte[1024];
        int len = -1;
        while ((len = is.read(flush)) != -1) {
            os.write(flush, 0, len);
        }
        //  3. 释放资源
        os.close();
        is.close();
        client.close();
    }
}
