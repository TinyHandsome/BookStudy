package com.sxt.others;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DoubleCheckedLocking.java
 * @time: 2019/11/11 9:34
 * @desc: 单例模式
 */

public class DoubleCheckedLocking {
    // 2. 提供私有的静态属性
    // 没有volatile其他线程可能访问一个没有初始化的对象
    private static volatile DoubleCheckedLocking instance;

    // 1. 构造器私有化
    private DoubleCheckedLocking() {

    }

    // 3. 提供公共的静态方法 --> 获取属性
    public static DoubleCheckedLocking getInstance() {
        // 再次检测，避免不必要的同步，已经存在对象
        if (null != instance) {
            return instance;
        }
        synchronized (DoubleCheckedLocking.class) {
            if (null == instance) {
                instance = new DoubleCheckedLocking();
                // new一个对象的时候，要做的三件事情
                // 开辟空间；初始化对象信息；返回对象的地址给引用
                // 所以这里可能出现指令重排
            }
            return instance;
        }
    }

    public static void main(String[] args) {
        Thread t = new Thread(() -> {
            System.out.println(DoubleCheckedLocking.getInstance());
        });
        t.start();
        System.out.println(DoubleCheckedLocking.getInstance());
    }
}
