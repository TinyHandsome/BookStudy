package com.sxt.factory.simplefactor;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CarFactory.java
 * @time: 2020/2/5 16:04
 * @desc: 简单工厂类2
 */

public class CarFactory2 {
    public static Car createAudi() {
        return new Audi();
    }

    public static Car createByd() {
        return new Byd();
    }
}

