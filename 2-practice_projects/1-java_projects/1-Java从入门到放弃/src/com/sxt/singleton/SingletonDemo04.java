package com.sxt.singleton;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SingletonDemo01.java
 * @time: 2020/2/3 18:41
 * @desc: 测试静态内部类实现单例模式，这种方式线程安全，调用效率高，并且实现了延时加载
 */

public class SingletonDemo04 {
    private static class SingletonClassInstance{
        private static final SingletonDemo04 instance = new SingletonDemo04();
    }
    private SingletonDemo04(){
    }

    // 方法没有同步，调用效率高！
    public static SingletonDemo04 getInstance(){
        return SingletonClassInstance.instance;
    }
}
