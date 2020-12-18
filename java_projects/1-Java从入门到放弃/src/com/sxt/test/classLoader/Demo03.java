package com.sxt.test.classLoader;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo03.java
 * @time: 2020/2/1 22:49
 * @desc: 测试简单加密解密（取反）操作
 */

public class Demo03 {
    public static void main(String[] args) throws ClassNotFoundException {
        int a = 3;  // 00000011
        System.out.println(Integer.toBinaryString(a ^ 0xff));

        // 加载这个加密的类会报类格式错误ClassFormatError
        FileSystemClassLoader loader1 = new FileSystemClassLoader("F:/Java WorkSpace");
        Class<?> c1 = loader1.loadClass("NewClass_encrp");
        System.out.println(c1);

        // 使用解密类加载器加载加密后的类
        DecrptClassLoader loader = new DecrptClassLoader("F:/Java WorkSpace/temp");
        Class<?> c = loader.loadClass("NewClass");
        System.out.println(c);
    }
}
