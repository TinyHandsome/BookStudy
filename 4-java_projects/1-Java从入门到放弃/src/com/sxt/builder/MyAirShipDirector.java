package com.sxt.builder;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MyAirShipDirector.java
 * @time: 2020/2/6 13:59
 * @desc:
 */

public class MyAirShipDirector implements AirShipDirector{

    private AirShipBuilder builder;

    public MyAirShipDirector(AirShipBuilder builder) {
        this.builder = builder;
    }

    @Override
    public AirShip directAirShip() {
        // 从构建者获取组件
        Engine e = builder.buildEngine();
        OrbitalModule o = builder.builderOrbitalModule();
        EscapeTower es = builder.buildEscapeTower();

        // 进行组装
        AirShip ship = new AirShip();
        ship.setEngine(e);
        ship.setOrbitalModule(o);
        ship.setEscapeTower(es);

        return ship;
    }
}
