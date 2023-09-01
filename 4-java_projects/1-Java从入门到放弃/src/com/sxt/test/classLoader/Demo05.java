package com.sxt.test.classLoader;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo05.java
 * @time: 2020/2/2 22:51
 * @desc: 线程上下文类加载器测试
 */

public class Demo05 {
    public static void main(String[] args) throws ClassNotFoundException {
        ClassLoader loader = Demo05.class.getClassLoader();
        System.out.println(loader);

        ClassLoader loader2 = Thread.currentThread().getContextClassLoader();
        System.out.println(loader2);

        Thread.currentThread().setContextClassLoader(new FileSystemClassLoader("F:/Java WorkSpace"));
        System.out.println(Thread.currentThread().getContextClassLoader());

        Class<Demo01> c = (Class<Demo01>) Thread.currentThread().getContextClassLoader().loadClass("com.sxt.test.classLoader.Demo01");
        System.out.println(c);
        System.out.println(c.getClassLoader());
    }
}
