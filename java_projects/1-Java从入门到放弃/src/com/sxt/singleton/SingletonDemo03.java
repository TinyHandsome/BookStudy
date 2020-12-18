package com.sxt.singleton;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SingletonDemo01.java
 * @time: 2020/2/3 18:41
 * @desc: 测试双重检测锁实现单例模式
 */

public class SingletonDemo03 {
    private static SingletonDemo03 instance = null;

    private SingletonDemo03() {
    }

    public static SingletonDemo03 getInstance() {
        if (instance == null){
            SingletonDemo03 sc;
            synchronized (SingletonDemo03.class){
                sc = instance;
                if(sc == null){
                    synchronized (SingletonDemo03.class){
                        if(sc == null){
                            sc = new SingletonDemo03();
                        }
                    }
                    instance = sc;
                }
            }
        }
        return instance;
    }
}
