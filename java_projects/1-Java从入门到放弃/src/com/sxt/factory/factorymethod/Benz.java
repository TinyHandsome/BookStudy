package com.sxt.factory.factorymethod;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Benz.java
 * @time: 2020/2/5 19:45
 * @desc:
 */

public class Benz extends BenzFactory implements Car {
    @Override
    public void run() {
        System.out.println("奔驰在跑！");
    }
}