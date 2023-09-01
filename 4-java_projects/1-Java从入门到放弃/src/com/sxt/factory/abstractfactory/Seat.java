package com.sxt.factory.abstractfactory;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Seat.java
 * @time: 2020/2/6 12:42
 * @desc:
 */

public interface Seat {
    void massage();
}

class LuxurySeat implements Seat{

    @Override
    public void massage() {
        System.out.println("可以按摩！");
    }
}
class LowerSeat implements Seat{

    @Override
    public void massage() {
        System.out.println("不可以按摩！");
    }
}
