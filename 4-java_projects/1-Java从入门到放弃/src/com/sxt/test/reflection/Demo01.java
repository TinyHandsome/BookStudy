package com.sxt.test.reflection;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2019/12/17 18:59
 * @desc: 测试各种类型对应的java.lang.Class对象的获取方式
 */

public class Demo01 {
    public static void main(String[] args) {
        String path = "com.sxt.test.bean.User";
        try {
            Class clazz = Class.forName(path);
            // 对象是表示或封装一些数据。一个类被加载后，JVM会创建一个对应该类的Class对象，
            // 类的整个结构信息会放到对应的Class对象中。这个Class对象就像一面镜子一样，
            // 通过这面镜子我们可以看到对应类的全部信息。
            System.out.println(clazz);
            System.out.println(clazz.hashCode());

            // 一个类只对应一个Class对象
            Class clazz2 = Class.forName(path);
            System.out.println(clazz2.hashCode());

            Class strClazz = String.class;
            Class strClazz2 = path.getClass();
            // 获得的都是String的Class对象
            System.out.println(strClazz==strClazz2);

            Class intClazz = int.class;
            System.out.println(intClazz.hashCode());

            // 数组跟维度、类型都有关
            int[] arr01 = new int[10];
            int[] arr02 = new int[30];
            int[][] arr03 = new int[10][10];
            double[] arr04 = new double[10];
            System.out.println(arr01.getClass().hashCode() == arr02.getClass().hashCode());
            System.out.println(arr01.getClass().hashCode() == arr03.getClass().hashCode());
            System.out.println(arr01.getClass().hashCode() == arr04.getClass().hashCode());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
