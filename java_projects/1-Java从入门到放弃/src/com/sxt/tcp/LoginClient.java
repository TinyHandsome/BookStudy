package com.sxt.tcp;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LoginClient.java
 * @time: 2019/11/18 15:13
 * @desc: 模拟登陆 单向 客户端
 */

public class LoginClient {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Client-----");
        BufferedReader console = new BufferedReader(new InputStreamReader((System.in)));
        System.out.println("请输入用户名：");
        String uname = console.readLine();
        System.out.println("请输入密码：");
        String upwd = console.readLine();
        //  1. 建立连接：使用Socket创建客户端 + 服务的地址和端口
        Socket client = new Socket("localhost", 8888);
        //  2. 操作：输入输出流操作
        DataOutputStream dos = new DataOutputStream(client.getOutputStream());
        dos.writeUTF("uname=" + uname + "&upwd=" + upwd);
        dos.flush();
        //  3. 释放资源
        dos.close();
        client.close();
    }
}
