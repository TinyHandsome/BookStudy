package com.sxt.factory.factorymethod;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: BydFactory.java
 * @time: 2020/2/5 19:43
 * @desc:
 */

public class BydFactory extends Byd implements CarFactory {
    @Override
    public Car createCar() {
        return new Byd();
    }
}
