package com.sxt.adapter;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/7 11:02
 * @desc: 客户类，相当于笔记本，只有USB接口
 */

public class Client {
    public void test1(Target t){
        t.handleReq();
    }

    public static void main(String[] args){
        Client c = new Client();
        Adaptee a = new Adaptee();

        // 方式1：类适配器方式
        Target t1 = new Adapter();
        // 方式2：对象适配器方式
        Target t2 = new Adapter2(a);

        c.test1(t2);
    }
}
