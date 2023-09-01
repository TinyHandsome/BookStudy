package com.sxt.prototype;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/6 15:57
 * @desc: 测试原型模式(深复制)，使用序列化和反序列化的方式实现深复制
 */

public class Client3 {
    public static void main(String[] args) throws Exception {
        Date d = new Date(3333333333L);
        Sheep1 s1 = new Sheep1("少理", d);
        System.out.println(s1);
        System.out.println(s1.getSname());
        System.out.println(s1.getBirthday());

        // 两个是不同的对象，但是值是一样的！
        // Sheep1 s2 = (Sheep1) s1.clone();
        // 这里用序列化和反序列化实现深复制，所以用的是Sheep1，即浅复制的类
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);
        oos.writeObject(s1);
        byte[] bytes = bos.toByteArray();

        ByteArrayInputStream bis = new ByteArrayInputStream(bytes);
        ObjectInputStream ois = new ObjectInputStream(bis);
        Sheep1 s2 = (Sheep1) ois.readObject();

        // 修改s1生日
        d.setTime(22222222222L);
        System.out.println("--------------------------");
        System.out.println(s1.getBirthday());

        System.out.println(s2);
        System.out.println(s2.getSname());
        System.out.println(s2.getBirthday());
    }
}
