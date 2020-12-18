package com.sxt.builder;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MyAirShipBuilder.java
 * @time: 2020/2/6 13:55
 * @desc:
 */

public class MyAirShipBuilder implements AirShipBuilder{

    @Override
    public Engine buildEngine() {
        System.out.println("构建发动机！");
        return new Engine("我的发动机");
    }

    @Override
    public OrbitalModule builderOrbitalModule() {
        System.out.println("构建轨道舱！");
        return new OrbitalModule("我的轨道舱");
    }

    @Override
    public EscapeTower buildEscapeTower() {
        System.out.println("构建逃逸塔！");
        return new EscapeTower("我的逃逸塔");
    }
}
