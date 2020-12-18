package com.sxt.prototype;

import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/6 15:57
 * @desc: 测试原型模式(深复制)
 */

public class Client2 {
    public static void main(String[] args) throws CloneNotSupportedException {
        Date d = new Date(3333333333L);
        Sheep2 s1 = new Sheep2("少理", d);
        System.out.println(s1);
        System.out.println(s1.getSname());
        System.out.println(s1.getBirthday());

        // 两个是不同的对象，但是值是一样的！
        Sheep2 s2 = (Sheep2) s1.clone();

        // 修改s1生日
        d.setTime(22222222222L);
        System.out.println("--------------------------");
        System.out.println(s1.getBirthday());

        System.out.println(s2);
        System.out.println(s2.getSname());
        System.out.println(s2.getBirthday());

        // 修改s2的值
        System.out.println("--------------------------");
        s2.setSname("多里");
        System.out.println(s2);
        System.out.println(s2.getSname());
        System.out.println(s2.getBirthday());
    }
}
