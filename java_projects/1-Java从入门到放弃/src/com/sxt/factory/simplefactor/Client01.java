package com.sxt.factory.simplefactor;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client01.java
 * @time: 2020/2/5 16:02
 * @desc: 测试在没有工厂模式的情况下
 */

public class Client01 { // 调用者
    public static void main(String[] args){
        Car c1 = new Audi();
        Car c2 = new Byd();
        c1.run();
        c2.run();
    }
}
