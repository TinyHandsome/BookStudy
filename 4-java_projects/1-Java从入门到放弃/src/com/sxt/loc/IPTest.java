package com.sxt.loc;

import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: IPTest.java
 * @time: 2019/11/12 10:35
 * @desc: IP
 */

public class IPTest {
    public static void main(String[] args) throws UnknownHostException {
        // 使用getLocalHost方法创建InetAddress对象
        InetAddress addr = InetAddress.getLocalHost();
        System.out.println(addr.getHostAddress());
        System.out.println(addr.getHostName());

        // 根据域名得到InetAddress对象
        addr = InetAddress.getByName("www.163.com");
        System.out.println(addr.getHostAddress());
        System.out.println(addr.getHostName());

        // 根据ip得到InetAddress对象
        addr = InetAddress.getByName("123.56.138.176");
        System.out.println(addr.getHostAddress());
        // 输出i而不是域名。如果这个IP地址不存在或DNS服务器不允许进行IP地址和域名映射，getHostName方法就直接返回这个IP地址。
        System.out.println(addr.getHostName());
    }
}
