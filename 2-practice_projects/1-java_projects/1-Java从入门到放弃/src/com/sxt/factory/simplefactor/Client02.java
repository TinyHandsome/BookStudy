package com.sxt.factory.simplefactor;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client01.java
 * @time: 2020/2/5 16:02
 * @desc: 测试在简单工厂模式的情况下
 */

public class Client02 { // 调用者
    public static void main(String[] args){
        Car c1 = CarFactory.createCar("奥迪");
        Car c2 = CarFactory.createCar("比亚迪");
        c1.run();
        c2.run();
    }
}
