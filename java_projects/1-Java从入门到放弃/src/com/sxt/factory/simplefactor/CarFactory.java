package com.sxt.factory.simplefactor;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CarFactory.java
 * @time: 2020/2/5 16:04
 * @desc:
 */

public class CarFactory {
    public static Car createCar(String type){
        if("奥迪".equals(type)){
            return new Audi();
        }else if("比亚迪".equals(type)){
            return new Byd();
        }else{
            // 简单工厂还是有点小问题的，这里如果要加新的车辆的话，就需要改代码，违反了开闭原则OCP
            return null;
        }
    }
}
