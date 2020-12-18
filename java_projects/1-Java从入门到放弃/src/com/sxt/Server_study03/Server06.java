package com.sxt.Server_study03;

import com.sxt.tcp.Server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Server06.java
 * @time: 2019/12/4 9:26
 * @desc: 加入了Servlet解耦了业务代码
 */

public class Server06 {
    private ServerSocket serverSocket;
    public static void main(String[] args) {
        Server06 server = new Server06();
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
            Servlet servlet = null;
            if(request.getUrl().equals("login")){
                servlet = new LoginServlet();
            }else if (request.getUrl().equals("reg")){
                servlet = new RegisterServlet();
            }else {
                // 首页
            }

            servlet.service(request, response);


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
