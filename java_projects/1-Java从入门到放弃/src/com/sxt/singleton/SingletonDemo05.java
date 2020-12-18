package com.sxt.singleton;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SingletonDemo01.java
 * @time: 2020/2/3 18:41
 * @desc: 测试枚举实现单例模式（没有延时加载）
 */

public enum  SingletonDemo05 {
    // 这个枚举元素，本身就是单例对象！
    INSTANCE;

    // 添加自己需要的操作！
    public void singletonOperation(){

    }
}
