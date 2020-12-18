package com.sxt.factory.factorymethod;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/5 19:44
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        Car c1 = new AudiFactory().createCar();
        Car c2 = new BydFactory().createCar();
        Car c3 = new BenzFactory().createCar();

        c1.run();
        c2.run();
        c3.run();
    }
}
