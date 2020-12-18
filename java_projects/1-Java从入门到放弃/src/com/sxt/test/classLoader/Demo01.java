package com.sxt.test.classLoader;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2020/1/30 21:40
 * @desc:
 */

public class Demo01 {
    public static void main(String[] args){
        // 应用加载器
        System.out.println(ClassLoader.getSystemClassLoader());
        // 扩展加载器（上一个的父类）
        System.out.println(ClassLoader.getSystemClassLoader().getParent());
        // 引导加载器，但是是C写的，所以为null（上一个的父类）
        System.out.println(ClassLoader.getSystemClassLoader().getParent().getParent());

        // 系统中类的路径
        System.out.println(System.getProperty("java.class.path"));
    }
}
