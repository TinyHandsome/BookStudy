package com.sxt.adapter;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Adapter2.java
 * @time: 2020/2/7 11:07
 * @desc: 【对象组合的方式，对象适配器方式】适配器
 */

public class Adapter2 implements Target{
    // 我的理解：把原来不兼容的键盘接口变成Target（即USB接口）

    private Adaptee adaptee;

    @Override
    public void handleReq() {
        adaptee.request();
    }

    public Adapter2(Adaptee adaptee) {
        this.adaptee = adaptee;
    }
}
