package com.sxt.flyweight;


import java.util.HashMap;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ChessFlyWeightFactory.java
 * @time: 2020/2/10 12:43
 * @desc: 享元工厂类
 */

public class ChessFlyWeightFactory {
    // 享元池
    private static Map<String, ChessFlyWeight> map = new HashMap<>();
    public static ChessFlyWeight getChess(String color){
        if(map.get(color) != null){
            return map.get(color);
        }else{
            ChessFlyWeight cfw = new ConcreteChess(color);
            map.put(color, cfw);
            return cfw;
        }
    }

}
