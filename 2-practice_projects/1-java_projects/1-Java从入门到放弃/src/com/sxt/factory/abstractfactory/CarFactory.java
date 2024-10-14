package com.sxt.factory.abstractfactory;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CarFactory.java
 * @time: 2020/2/6 12:44
 * @desc:
 */

public interface CarFactory {
    Engine createEngine();
    Seat createSeat();;
    Tyre createTyre();
}
