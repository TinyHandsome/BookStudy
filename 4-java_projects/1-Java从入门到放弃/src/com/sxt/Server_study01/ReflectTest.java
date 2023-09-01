package com.sxt.Server_study01;

import java.lang.reflect.InvocationTargetException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ReflectTest.java
 * @time: 2019/11/29 14:55
 * @desc:
 */

public class ReflectTest {
    public static void main(String[] args){
        // 1. 对象.getClass() | 买iphone照着做
        Iphone iphone = new Iphone();
        Class clz = iphone.getClass();
        // 2. 类.class()     | 买通工程师给图纸
        clz = Iphone.class;
        // 3. Class.forName("包名.类名")   | 偷图纸
        try {
            clz = Class.forName("com.sxt.Server_study01.Iphone");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        // 创建对象
        try {
            Iphone iphone2 = (Iphone)clz.newInstance();
            System.out.println(iphone2);
        } catch (InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
        }
        // 创建对象推荐方式
        try {
            Iphone iphone3 = (Iphone)clz.getConstructor().newInstance();
            System.out.println(iphone3);
        } catch (InstantiationException | IllegalAccessException | InvocationTargetException | NoSuchMethodException e) {
            e.printStackTrace();
        }
    }
}

class Iphone{
    public Iphone(){
    }
}