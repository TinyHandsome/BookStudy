package com.sxt.chat2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MultiChat.java
 * @time: 2019/11/19 14:57
 * @desc: 在线聊天室：服务端
 * 目标：使用多线程实现多个客户可以正常收发多人信息
 */

public class MultiChat {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Server-----");
        //  1. 指定端口，使用ServerSocket创建服务器
        ServerSocket server = new ServerSocket(8888);
        //  2. 阻塞式等待连接 accept
        while (true) {
            Socket client = server.accept();
            System.out.println("一个客户端建立了连接...");

            new Thread(() -> {
                DataInputStream dis = null;
                DataOutputStream dos = null;
                try {
                    dis = new DataInputStream(client.getInputStream());
                    dos = new DataOutputStream(client.getOutputStream());
                } catch (IOException e) {
                    e.printStackTrace();
                }
                boolean isRunning = true;
                while (isRunning) {
                    //  3. 接收消息
                    String msg = null;
                    try {
                        msg = dis.readUTF();
                        //  4. 返回消息
                        dos.writeUTF(msg);
                        dos.flush();
                    } catch (IOException e) {
                        e.printStackTrace();
                        isRunning = false;
                    }
                }
                //  5. 释放资源
                try {
                    if (null != dos) {
                        dos.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
                try {
                    if (null != dis) {
                        dis.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
                try {
                    if (null != client) {
                        client.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }
}
