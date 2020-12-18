package com.sxt.Server_study03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Dispatcher.java
 * @time: 2019/12/12 16:36
 * @desc: 分发器
 */

public class Dispatcher implements Runnable {
    private Socket client;
    private Request request;
    private Response response;

    public Dispatcher(Socket client) {
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
            if (null == request.getUrl() || request.getUrl().equals("")) {
                InputStream is = Thread.currentThread().getContextClassLoader().getResourceAsStream("index.html");
                BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                String line = null;
                while((line = br.readLine()) != null){
                    response.println(line);
                }
                br.close();
                response.pushToBrowser(200);
                return;
            }
            Servlet servlet = WebApp.getServletFromUrl(request.getUrl());
            if (null != servlet) {
                servlet.service(request, response);
                // 关注了状态码
                response.pushToBrowser(200);
            } else {
                InputStream is = Thread.currentThread().getContextClassLoader().getResourceAsStream("error.html");
                System.out.println(is);
                BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                String line = null;
                while((line = br.readLine()) != null){
                    response.println(line);
                }
                br.close();
                response.pushToBrowser(404);
            }
        } catch (Exception e) {
            e.printStackTrace();
            try {
                response.print("你好我不好，我会马上好");
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
