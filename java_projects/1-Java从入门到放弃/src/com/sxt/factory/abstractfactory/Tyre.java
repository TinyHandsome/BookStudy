package com.sxt.factory.abstractfactory;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Tyre.java
 * @time: 2020/2/6 12:43
 * @desc:
 */

public interface Tyre {
    void revolve();
}

class LuxuryTyre implements Tyre{

    @Override
    public void revolve() {
        System.out.println("磨损慢！");
    }
}
class LowerTyre implements Tyre{

    @Override
    public void revolve() {
        System.out.println("磨损快！");
    }
}
