package com.sxt.tcp;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LoginMultiServer.java
 * @time: 2019/11/19 9:18
 * @desc:
 */

public class LoginMultiServer {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Server-----");
        //  1. 指定端口，使用ServerSocket创建服务器
        ServerSocket server = new ServerSocket(8888);
        boolean isRunning = true;
        while (isRunning) {
            //  2. 阻塞式等待连接 accept
            Socket client = server.accept();
            System.out.println("一个客户端建立了连接...");
            new Thread(new Channel(client)).start();
        }
        //  关闭服务器的话
        server.close();
    }

    static class Channel implements Runnable {
        private Socket client;
        // 输入流封装
        private DataInputStream dis;
        // 输出流封装
        private DataOutputStream dos;

        public Channel(Socket client) {
            this.client = client;
            try {
                dis = new DataInputStream(client.getInputStream());
                dos = new DataOutputStream(client.getOutputStream());
            } catch (IOException e) {
                release();
            }
        }

        @Override
        public void run() {
            //  3. 操作：输入输出流操作
            String uname = "";
            String upwd = "";
            //  分析
            String datas = receive();
            String[] dataArray = datas.split("&");
            for (String info : dataArray) {
                String[] userInfo = info.split("=");
                if (userInfo[0].equals("uname")) {
                    System.out.println("你的用户名为：" + userInfo[1]);
                    uname = userInfo[1];
                } else if (userInfo[0].equals("upwd")) {
                    System.out.println("你的密码为：" + userInfo[1]);
                    upwd = userInfo[1];
                }
            }
            if (uname.equals("litian") && upwd.equals("123")) {
                send("登陆成功，欢迎回来！");
            } else {
                send("登陆失败，用户名或密码错误！");
            }

            release();
        }

        // 接受数据
        private String receive() {
            String datas = "";
            try {
                datas = dis.readUTF();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return datas;
        }

        // 发送数据
        private void send(String msg) {
            try {
                dos.writeUTF(msg);
                dos.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        // 释放资源
        private void release() {
            //  4. 释放资源
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
        }
    }
}
