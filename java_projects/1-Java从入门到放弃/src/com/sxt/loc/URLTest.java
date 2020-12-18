package com.sxt.loc;

import java.net.MalformedURLException;
import java.net.URL;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: URLTest.java
 * @time: 2019/11/14 9:27
 * @desc: URL练习
 */

public class URLTest {
    public static void main(String[] args) throws MalformedURLException {
        URL url = new URL("http://www.baidu.com:80/index.html?uname=shsxt&age=18#a");
        // 获取四个值
        System.out.println("协议：" + url.getProtocol());
        System.out.println("域名|ip：" + url.getHost());
        System.out.println("端口：" + url.getPort());
        System.out.println("请求资源1：" + url.getFile());
        System.out.println("请求资源2：" + url.getPath());

        // 参数
        System.out.println("参数：" + url.getQuery());
        // 锚点
        System.out.println("锚点：" + url.getRef());
    }
}
