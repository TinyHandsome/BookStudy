package com.sxt.test.classLoader;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo02.java
 * @time: 2020/1/31 21:17
 * @desc: 测试自定义类加载器FileSystemClassLoader
 */

public class Demo02 {
    public static void main(String[] args) throws ClassNotFoundException {
        FileSystemClassLoader loader1 = new FileSystemClassLoader("F:\\Java WorkSpace");
        FileSystemClassLoader loader2 = new FileSystemClassLoader("F:\\Java WorkSpace");
        System.out.println(loader1 == loader2);


        Class<?> c1 = loader1.loadClass("NewClass");
        Class<?> c2 = loader1.loadClass("NewClass");
        Class<?> c3 = loader2.loadClass("NewClass");
        Class<?> c4 = loader1.loadClass("java.lang.String");
        Class<?> c5 = loader1.loadClass("com.sxt.test.classLoader.Demo01");

        System.out.println(c1);
        System.out.println(c1.hashCode());
        System.out.println(c2);
        System.out.println(c2.hashCode());

        // 注意：被两个类加载器加载的同一个类，JVM不认为是相同的类。
        System.out.println(c3);
        System.out.println(c3.hashCode());

        System.out.println(c4);
        System.out.println(c4.hashCode());

        System.out.println(c1.getClassLoader());
        System.out.println(c2.getClassLoader());
        System.out.println(c3.getClassLoader());    // 自定义的类加载器
        System.out.println(c4.getClassLoader());    // 引导类加载器
        System.out.println(c5.getClassLoader());    // 系统默认的类加载器

    }
}
