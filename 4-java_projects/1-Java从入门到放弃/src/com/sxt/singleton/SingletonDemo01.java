package com.sxt.singleton;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SingletonDemo01.java
 * @time: 2020/2/3 18:41
 * @desc: 测试饿汉式单例模式
 */

public class SingletonDemo01 {
    // 上来就把这个对象先new了，不管后面你使不使用它。所以叫做饿汉式。
    // 类初始化时，立即加载这个对象。（所以不能延时加载）
    // 由于加载类时，天然的是线程安全的！
    private static SingletonDemo01 instance = new SingletonDemo01();
    private SingletonDemo01(){
    }

    // 方法没有同步，调用效率高！
    public static SingletonDemo01 getInstance(){
        return instance;
    }
}
