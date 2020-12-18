package com.sxt.factory.factorymethod;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Audi.java
 * @time: 2020/2/5 16:00
 * @desc:
 */

public class Audi extends AudiFactory implements Car {
    @Override
    public void run() {
        System.out.println("奥迪在跑！");
    }
}
