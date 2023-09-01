package com.sxt.tcp;

import java.io.*;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LoginMultiClient.java
 * @time: 2019/11/19 9:18
 * @desc:
 */

public class LoginMultiClient {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Client-----");
        //  1. 建立连接：使用Socket创建客户端 + 服务的地址和端口
        Socket client = new Socket("localhost", 8888);
        //  2. 操作：输入输出流操作
        new Send(client).send();
        new Receive(client).receive();
        //  3. 释放资源
        client.close();
    }

    static class Send {
        private Socket client;
        private DataOutputStream dos;
        private BufferedReader console;
        private String msg;

        public Send(Socket client) {
            console = new BufferedReader(new InputStreamReader((System.in)));
            this.client = client;
            this.msg = init();
            try {
                dos = new DataOutputStream(client.getOutputStream());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        private String init() {
            try {
                System.out.println("请输入用户名：");
                String uname = console.readLine();
                System.out.println("请输入密码：");
                String upwd = console.readLine();
                return "uname=" + uname + "&upwd=" + upwd;
            } catch (IOException e) {
                e.printStackTrace();
                return "???";
            }
        }

        public void send() {
            try {
                dos.writeUTF(msg);
                dos.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    static class Receive {
        private Socket client;
        private DataInputStream dis;

        public Receive(Socket client) {
            this.client = client;
            try {
                dis = new DataInputStream(client.getInputStream());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public void receive() {
            String result = null;
            try {
                result = dis.readUTF();
                System.out.println(result);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
