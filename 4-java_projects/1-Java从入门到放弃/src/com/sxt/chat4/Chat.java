package com.sxt.chat4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MultiChat.java
 * @time: 2019/11/19 14:57
 * @desc: 在线聊天室：服务端
 * 目标：加入容器实现群聊
 */

public class Chat {
    private static CopyOnWriteArrayList<Channel> all = new CopyOnWriteArrayList<>();

    public static void main(String[] args) throws IOException {
        System.out.println("-----Server-----");
        //  1. 指定端口，使用ServerSocket创建服务器
        ServerSocket server = new ServerSocket(8888);
        //  2. 阻塞式等待连接 accept
        while (true) {
            Socket client = server.accept();
            System.out.println("一个客户端建立了连接...");
            Channel c = new Channel(client);
            // 管理所有的成员
            all.add(c);
            new Thread(c).start();

        }
    }

    // 一个客户代表一个Channel
    static class Channel implements Runnable {
        private DataInputStream dis;
        private DataOutputStream dos;
        private Socket client;
        private boolean isRunning;
        private String name;

        public Channel(Socket client) {
            this.client = client;
            try {
                dis = new DataInputStream(client.getInputStream());
                dos = new DataOutputStream(client.getOutputStream());
                isRunning = true;
                // 获取名称
                this.name = receive();
                // 欢迎你的到来
                this.send("欢迎你的到来");
                sendOthers(this.name + "来了shsxt聊天室", true);
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

        // 群聊
        private void sendOthers(String msg, boolean isSys) {
            boolean isPrivate = msg.startsWith("@");
            if(isPrivate){
                // 私聊
                int idx = msg.indexOf(":");
                // 获取目标和数据
                String targetName = msg.substring(1, idx);
                msg = msg.substring(idx+1);
                for(Channel other: all){
                    if(other.name.equals(targetName)){
                        other.send(this.name + "悄悄的对你说：" + msg);
                        break;
                    }
                }
            }else{
                for(Channel other: all){
                    if(other == this){  // 自己
                        continue;
                    }
                    if(!isSys) {
                        // 群聊消息
                        other.send(this.name + "说：" + msg);
                    }else{
                        // 系统消息
                        other.send(msg);
                    }
                }
            }
        }

        // 释放资源
        private void release() {
            this.isRunning = false;
            SxtUtils.close(dis, dos, client);
            // 退出
            all.remove(this);
            sendOthers(this.name + "离开了...", true);
        }

        @Override
        public void run() {
            while (isRunning) {
                String msg = receive();
                if (!msg.equals("")) {
                    // send(msg);
                    sendOthers(msg, false);
                }
            }
        }
    }
}
