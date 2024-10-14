package com.sxt.chat1;

import java.io.*;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MultiClient.java
 * @time: 2019/11/19 14:57
 * @desc: 在线聊天室：客户端
 * 目标：实现一个客户可以正常收发多条信息
 */

public class MultiClient {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Client-----");
        //  1. 建立连接：使用Socket创建客户端 + 服务的地址和端口
        Socket client = new Socket("localhost", 8888);
        //  2. 客户端发送消息
        BufferedReader console = new BufferedReader(new InputStreamReader((System.in)));
        DataOutputStream dos = new DataOutputStream(client.getOutputStream());
        DataInputStream dis = new DataInputStream(client.getInputStream());
        boolean isRunning = true;
        while (isRunning) {
            String msg = console.readLine();
            dos.writeUTF(msg);
            dos.flush();
            //  3. 获取消息
            msg = dis.readUTF();
            System.out.println(msg);
        }
        //  4. 释放资源
        dos.close();
        dis.close();
        client.close();
    }
}
