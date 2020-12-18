package com.sxt.singleton;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SingletonDemo01.java
 * @time: 2020/2/3 18:41
 * @desc: 测试懒汉式单例模式
 */

public class SingletonDemo02 {
    // 类初始化时，不初始化这个对象。（延时加载，真正用的时候再创建）
    private static SingletonDemo02 instance;

    private SingletonDemo02() {
    }

    // 方法同步，调用效率低！
    public static synchronized SingletonDemo02 getInstance() {
        if (instance == null){
            instance = new SingletonDemo02();
        }
        return instance;
    }
}
