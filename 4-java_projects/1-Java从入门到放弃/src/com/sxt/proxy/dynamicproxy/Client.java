package com.sxt.proxy.dynamicproxy;

import java.lang.reflect.Proxy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/7 16:22
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        Star realStar = new RealStar();
        StarHandler handler = new StarHandler(realStar);

        Star proxy = (Star) Proxy.newProxyInstance(ClassLoader.getSystemClassLoader(), new Class[]{Star.class}, handler);

        proxy.sing();

    }
}
