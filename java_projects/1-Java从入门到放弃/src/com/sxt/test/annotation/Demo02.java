package com.sxt.test.annotation;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo02.java
 * @time: 2019/12/16 9:56
 * @desc:
 */

public class Demo02 {
    @Annotation01(age = 19, studentName = "我", id=1001, schools = {"1", "2"})
    public void test() {
    }
}
