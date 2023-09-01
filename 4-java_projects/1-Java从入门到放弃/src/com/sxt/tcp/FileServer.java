package com.sxt.tcp;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: FileServer.java
 * @time: 2019/11/18 15:32
 * @desc: 服务器：存储文件
 */

public class FileServer {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Server-----");
        //  1. 指定端口，使用ServerSocket创建服务器
        ServerSocket server = new ServerSocket(8888);
        //  2. 阻塞式等待连接 accept
        Socket client = server.accept();
        System.out.println("一个客户端建立了连接...");
        //  3. 操作：文件拷贝 存储
        InputStream is = new BufferedInputStream(client.getInputStream());
        OutputStream os = new BufferedOutputStream(new FileOutputStream("./快乐保存.jpg"));
        byte[] flush = new byte[1024];
        int len = -1;
        while ((len = is.read(flush)) != -1) {
            os.write(flush, 0, len);
        }
        //  4. 释放资源
        os.close();
        is.close();
        client.close();
        //  关闭服务器的话
        server.close();
    }
}
