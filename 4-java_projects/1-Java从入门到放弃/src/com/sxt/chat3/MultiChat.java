package com.sxt.chat3;

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
 * 目标：封装：使用多线程实现多个客户可以正常收发多人信息
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
            new Thread(new Channel(client)).start();

        }
    }

    // 一个客户代表一个Channel
    static class Channel implements Runnable {
        private DataInputStream dis;
        private DataOutputStream dos;
        private Socket client;
        private boolean isRunning;

        public Channel(Socket client) {
            this.client = client;
            try {
                dis = new DataInputStream(client.getInputStream());
                dos = new DataOutputStream(client.getOutputStream());
                isRunning = true;
            } catch (IOException e) {
                release();
            }
        }

        // 接受消息
        private String receive() {
            String msg = "";
            try {
                msg = dis.readUTF();
            } catch (IOException e) {
                release();
            }
            return msg;
        }

        // 发送消息
        private void send(String msg) {
            try {
                dos.writeUTF(msg);
                dos.flush();
            } catch (IOException e) {
                release();
            }
        }

        // 释放资源
        private void release() {
            this.isRunning = false;
            SxtUtils.close(dis, dos, client);
        }

        @Override
        public void run() {
            while(isRunning){
                String msg = receive();
                if(!msg.equals("")){
                    send(msg);
                }
            }
        }
    }
}
