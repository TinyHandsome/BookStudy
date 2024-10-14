package com.sxt.chat3;

import java.io.*;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MultiClient.java
 * @time: 2019/11/19 14:57
 * @desc: 在线聊天室：客户端
 * 目标：封装：使用多线程实现多个客户可以正常收发多条信息
 */

public class MultiClient {
    public static void main(String[] args) throws IOException {
        System.out.println("-----Client-----");
        //  1. 建立连接：使用Socket创建客户端 + 服务的地址和端口
        Socket client = new Socket("localhost", 8888);
        //  2. 客户端发送消息
        new Thread(new Send(client)).start();
        new Thread(new Receive(client)).start();
    }
}
