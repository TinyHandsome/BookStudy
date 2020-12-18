package com.sxt.decorator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/9 18:13
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        Car car = new Car();
        car.move();

        System.out.println("增加新的功能，飞行！");
        FlyCar flyCar = new FlyCar(car);
        flyCar.move();

        System.out.println("增加新的功能，游泳！");
        WaterCar waterCar = new WaterCar(car);
        waterCar.move();

        System.out.println("增加新的功能，飞行和游泳！");
        WaterCar car2 = new WaterCar(new FlyCar(car));
        car2.move();
    }
}
