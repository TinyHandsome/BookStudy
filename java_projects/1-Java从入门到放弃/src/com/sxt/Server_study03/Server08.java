package com.sxt.Server_study03;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Server08.java
 * @time: 2019/12/4 9:26
 * @desc: 多线程处理，加入分发器
 */

public class Server08 {
    private ServerSocket serverSocket;
    private boolean isRunning;

    public static void main(String[] args) {
        Server08 server = new Server08();
        server.start();
    }

    // 启动服务
    public void start() {
        try {
            serverSocket = new ServerSocket(8888);
            isRunning = true;
            receive();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("服务器启动失败...");
            stop();
        }
    }

    // 接受连接处理
    public void receive() {
        while (isRunning) {
            try {
                Socket client = serverSocket.accept();
                System.out.println("一个客户端建立了连接...");
                // 多线程处理
                new Thread(new Dispatcher(client)).start();
            } catch (IOException e) {
                e.printStackTrace();
                System.out.println("客户端错误...");
            }
        }
    }

    // 停止服务
    public void stop() {
        isRunning = false;
        try {
            this.serverSocket.close();
            System.out.println("服务器已停止...");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
