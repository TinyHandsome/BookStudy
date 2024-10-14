package com.sxt.builder;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: AirShipBuilder.java
 * @time: 2020/2/6 13:53
 * @desc:
 */

public interface AirShipBuilder {
    Engine buildEngine();
    OrbitalModule builderOrbitalModule();
    EscapeTower buildEscapeTower();
}
