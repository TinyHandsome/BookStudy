package com.sxt.test.reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo02.java
 * @time: 2020/1/7 14:33
 * @desc: 应用反射的API获取类的信息（类的名字、属性、方法、构造器等）
 */

public class Demo02 {
    public static void main(String[] args) {
        String path = "com.sxt.test.bean.User";
        try {
            Class clazz = Class.forName(path);

            // 获取类的全名
            System.out.println(clazz.getName());
            // 获取类的包名+全名
            System.out.println(clazz.getSimpleName());

            // 获取属性信息
            // 只能获得public的field
            // Field[] fields = clazz.getFields();
            // 返回所有的field
            Field[] fields = clazz.getDeclaredFields();
            System.out.println(fields.length);
            for(Field temp: fields){
                System.out.println("属性：" + temp);
            }

            // 通过名称获取属性
            Field f = clazz.getDeclaredField("uname");
            System.out.println(f);

            // 获取方法信息
            Method[] methods = clazz.getDeclaredMethods();
            Method m1 = clazz.getDeclaredMethod("getUname");
            Method m2 = clazz.getDeclaredMethod("setUname", String.class);
            for(Method temp: methods){
                System.out.println("方法：" + temp);
            }

            // 获取构造器信息
            Constructor[] constructors = clazz.getDeclaredConstructors();
            for(Constructor temp: constructors){
                System.out.println("构造器：" + temp);
            }
            // 获取某个特定的构造器
            Constructor c1 = clazz.getDeclaredConstructor();
            System.out.println("无参构造器：" + c1);
            Constructor c2 = clazz.getDeclaredConstructor(int.class, int.class, String.class);
            System.out.println("有参构造器：" + c2);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
