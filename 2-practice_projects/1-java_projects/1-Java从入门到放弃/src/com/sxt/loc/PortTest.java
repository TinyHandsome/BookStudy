package com.sxt.loc;

import java.net.InetSocketAddress;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: PortTest.java
 * @time: 2019/11/12 14:24
 * @desc: 端口
 */

public class PortTest {
    public static void main(String[] args){
        // 包含端口
        InetSocketAddress socketAddress1 = new InetSocketAddress("127.0.0.1", 8080);
        InetSocketAddress socketAddress2 = new InetSocketAddress("localhost", 9000);
        System.out.println(socketAddress1.getHostName());
        System.out.println(socketAddress1.getAddress());
        System.out.println(socketAddress1.getPort());
        System.out.println(socketAddress2.getHostName());
        System.out.println(socketAddress2.getAddress());
        System.out.println(socketAddress2.getPort());
    }
}
