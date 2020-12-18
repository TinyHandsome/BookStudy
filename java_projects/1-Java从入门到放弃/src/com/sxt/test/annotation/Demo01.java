package com.sxt.test.annotation;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2019/12/16 9:34
 * @desc:
 */

public class Demo01 {
    @Override
    // 重写父类方法
    public String toString() {
        return "";
    }

    @Deprecated
    // 该方法不建议使用
    public static void test1() {
        System.out.println("你大爷");
    }

    @SuppressWarnings("all")
    // 不显示所有警告信息
    public static void test2() {
        List list = new ArrayList();
    }

    @SuppressWarnings(value = {"unchecked", "deprecation"})
    // 不显示某几个警告信息
    public static void main(String[] args) {
        test1();
    }
}
