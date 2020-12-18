package com.sxt.singleton;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/3 20:13
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        // 测试饿汉实现单例
        SingletonDemo01 s11 = SingletonDemo01.getInstance();
        SingletonDemo01 s12 = SingletonDemo01.getInstance();
        System.out.println(s11);
        System.out.println(s12);
        // 测试懒汉实现单例
        SingletonDemo02 s21 = SingletonDemo02.getInstance();
        SingletonDemo02 s22 = SingletonDemo02.getInstance();
        System.out.println(s21);
        System.out.println(s22);
        // 测试双重检测锁实现单例
        SingletonDemo03 s31 = SingletonDemo03.getInstance();
        SingletonDemo03 s32 = SingletonDemo03.getInstance();
        System.out.println(s31);
        System.out.println(s32);
        // 测试静态内部类实现单例
        SingletonDemo04 s41 = SingletonDemo04.getInstance();
        SingletonDemo04 s42 = SingletonDemo04.getInstance();
        System.out.println(s41);
        System.out.println(s42);
        // 测试枚举实现单例
        SingletonDemo05 s51 = SingletonDemo05.INSTANCE;
        SingletonDemo05 s52 = SingletonDemo05.INSTANCE;
        System.out.println(s51);
        System.out.println(s52);
    }
}
