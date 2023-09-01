package com.sxt.chat3;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Receive.java
 * @time: 2019/11/25 14:37
 * @desc: 使用多线程封装了接收端
 */

public class Receive implements Runnable {
    private Socket client;
    private boolean isRunning;
    private DataInputStream dis;

    public Receive(Socket client) {
        this.client = client;
        try {
            dis = new DataInputStream(client.getInputStream());
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

    @Override
    public void run() {
        while (isRunning) {
            String msg = receive();
            if (!msg.equals("")) {
                System.out.println(msg);
            }
        }
    }

    // 释放资源
    private void release() {
        this.isRunning = false;
        SxtUtils.close(dis, client);
    }
}
