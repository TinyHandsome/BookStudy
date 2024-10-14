package com.sxt.test.reflection;

import com.sxt.test.bean.User;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo3.java
 * @time: 2020/1/8 17:03
 * @desc: 通过反射API动态的操作：构造器、方法、属性
 */

public class Demo3 {
    public static void main(String[] args) {
        String path = "com.sxt.test.bean.User";
        try {
            Class<User> clazz = (Class<User>) Class.forName(path);

            // 通过反射API调用构造方法，构造对象
            // 其实是调用了User的无参构造方法
            User u = clazz.newInstance();
            System.out.println(u);

            // 指定构造器的调用
            Constructor<User> c = clazz.getDeclaredConstructor(int.class, int.class, String.class);
            User u2 = c.newInstance(1001, 18, "李英俊");
            System.out.println(u2.getUname());

            // 通过反射API调用普通方法
            User u3 = clazz.newInstance();
            u3.setUname("李不羁");
            // 上一句用反射来写如下
            Method method = clazz.getDeclaredMethod("setUname", String.class);
            method.invoke(u3, "李不羁");
            System.out.println(u3.getUname());

            // 通过反射API操作属性
            User u4 = clazz.newInstance();
            Field f = clazz.getDeclaredField("uname");
            // 这个属性不需要做安全检查了，可以直接访问
            f.setAccessible(true);
            // 通过反射直接写属性
            f.set(u4, "李傻瓜");
            System.out.println(u4.getUname());
            // 通过反射直接读属性的值
            System.out.println(f.get(u4));


        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
