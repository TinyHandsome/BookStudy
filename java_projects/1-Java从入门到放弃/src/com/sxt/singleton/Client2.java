package com.sxt.singleton;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Constructor;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/3 20:13
 * @desc: 测试反射和反序列化被破解单例模式
 */

public class Client2 {
    public static void main(String[] args) throws Exception {
        // 测试饿汉实现单例
        SingletonDemo06 s1 = SingletonDemo06.getInstance();
        SingletonDemo06 s2 = SingletonDemo06.getInstance();
        System.out.println(s1);
        System.out.println(s2);

        // 通过反射的方式直接调用私有构造器
        Class<SingletonDemo06> clazz = (Class<SingletonDemo06>) Class.forName("com.sxt.singleton.SingletonDemo06");
        Constructor<SingletonDemo06> c = clazz.getDeclaredConstructor(null);
        // 这样设置就可以访问private的构造器了，这种方式则跳过了单例模式的限制
        c.setAccessible(true);

        SingletonDemo06 s3 = c.newInstance();
        SingletonDemo06 s4 = c.newInstance();

        System.out.println(s3);
        System.out.println(s4);

        // 通过反序列化的方式构造多个对象
        FileOutputStream fos = new FileOutputStream("a.txt");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(s1);
        oos.close();
        fos.close();

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("a.txt"));
        SingletonDemo06 s5 = (SingletonDemo06) ois.readObject();
        System.out.println(s5);

    }
}
