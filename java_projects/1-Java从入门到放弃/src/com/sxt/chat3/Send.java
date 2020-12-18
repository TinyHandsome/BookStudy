package com.sxt.chat3;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Send.java
 * @time: 2019/11/25 14:37
 * @desc: 使用多线程封装了发送端
 */

public class Send implements Runnable {
    private BufferedReader console;
    private DataOutputStream dos;
    private Socket client;
    private boolean isRunning;

    public Send(Socket client) {
        this.client = client;
        console = new BufferedReader(new InputStreamReader(System.in));
        try {
            dos = new DataOutputStream(client.getOutputStream());
            isRunning = true;
        } catch (IOException e) {
            this.release();
        }

    }

    @Override
    public void run() {
        while (isRunning) {
            String msg = getStrFromConsole();
            if (!msg.equals("")) {
                send(msg);
            }
        }

    }

    private void send(String msg) {
        try {
            dos.writeUTF(msg);
            dos.flush();
        } catch (IOException e) {
            release();
        }
    }

    private String getStrFromConsole() {
        try {
            return console.readLine();
        } catch (IOException e) {
            release();
        }
        return "";
    }

    // 释放资源
    private void release() {
        this.isRunning = false;
        SxtUtils.close(dos, client);
    }
}
