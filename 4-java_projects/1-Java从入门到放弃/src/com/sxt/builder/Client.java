package com.sxt.builder;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/6 14:02
 * @desc:
 */

public class Client {
    public static void main(String[] args) {
        AirShipDirector director = new MyAirShipDirector(new MyAirShipBuilder());

        AirShip ship = director.directAirShip();

        ship.launch();
    }
}
