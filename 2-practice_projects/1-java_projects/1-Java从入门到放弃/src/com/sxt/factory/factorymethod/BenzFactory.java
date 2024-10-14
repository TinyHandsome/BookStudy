package com.sxt.factory.factorymethod;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: BenzFactory.java
 * @time: 2020/2/5 19:46
 * @desc:
 */

public class BenzFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new Benz();
    }
}
