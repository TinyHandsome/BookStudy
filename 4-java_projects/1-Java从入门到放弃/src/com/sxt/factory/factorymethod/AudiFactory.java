package com.sxt.factory.factorymethod;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: AudiFactory.java
 * @time: 2020/2/5 19:42
 * @desc:
 */

public class AudiFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new Audi();
    }
}
