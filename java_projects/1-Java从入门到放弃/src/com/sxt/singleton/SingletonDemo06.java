package com.sxt.singleton;

import java.io.Serializable;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SingletonDemo01.java
 * @time: 2020/2/3 18:41
 * @desc: 测试懒汉式单例模式（如何防止反射和反序列化）
 */

public class SingletonDemo06 implements Serializable {
    // 类初始化时，不初始化这个对象。（延时加载，真正用的时候再创建）
    private static SingletonDemo06 instance;

    private SingletonDemo06() {
        // 通过检查是否已经创建对象了，如果有了，则抛出异常
        if (instance != null) {
            throw new RuntimeException();
        }
    }

    // 方法同步，调用效率低！
    public static synchronized SingletonDemo06 getInstance() {
        if (instance == null) {
            instance = new SingletonDemo06();
        }
        return instance;
    }

    // 反序列化时，如果定了readResolve方法，则直接返回此方法指定的对象，而不需要单独再创建新对象！
    private Object readResolve() throws Exception{
        return instance;
    }
}
