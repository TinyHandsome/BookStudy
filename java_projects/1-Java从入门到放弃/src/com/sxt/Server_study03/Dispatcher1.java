package com.sxt.Server_study03;

import java.io.IOException;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Dispatcher.java
 * @time: 2019/12/12 16:36
 * @desc: 分发器
 */

public class Dispatcher1 implements Runnable {
    private Socket client;
    private Request request;
    private Response response;

    public Dispatcher1(Socket client) {
        this.client = client;
        try {
            // 获取请求和响应
            request = new Request(client);
            response = new Response(client);
        } catch (IOException e) {
            e.printStackTrace();
            this.release();
        }
    }

    @Override
    public void run() {
        try {
            Servlet servlet = WebApp.getServletFromUrl(request.getUrl());
            if (null != servlet) {
                servlet.service(request, response);
                // 关注了状态码
                response.pushToBrowser(200);
            } else {
                // 错误页面...
                response.pushToBrowser(404);
            }
        }catch (Exception e){
            try {
                response.pushToBrowser(500);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
        release();
    }

    // 释放资源
    private void release() {
        try {
            client.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}