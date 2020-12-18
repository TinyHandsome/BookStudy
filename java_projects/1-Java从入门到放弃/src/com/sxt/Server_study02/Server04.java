package com.sxt.Server_study02;

import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Server04.java
 * @time: 2019/12/4 9:26
 * @desc: 封装请求协议：获取method uri以及请求参数
 */

public class Server04 {
    private ServerSocket serverSocket;
    public static void main(String[] args) {
        Server04 server = new Server04();
        server.start();
    }

    // 启动服务
    public void start() {
        try {
            serverSocket = new ServerSocket(8888);
            receive();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("服务器启动失败...");
        }
    }

    // 接受连接处理
    public void receive() {
        try {
            Socket client = serverSocket.accept();
            System.out.println("一个客户端建立了连接...");
            // 获取请求协议
            Request request = new Request(client);

            Response response = new Response(client);

            // 关注了内容
            response.print("<html>");
            response.print("<head>");
            response.print("<title>");
            response.print("服务器响应成功");
            response.print("</title>");
            response.print("</head>");
            response.print("<body>");
            response.print("终于回来了...");
            response.print("</body>");
            response.print("</html>");

            // 关注了状态码
            response.pushToBrowser(200);

        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("客户端错误...");
        }
    }

    // 停止服务
    public void stop() {

    }
}
