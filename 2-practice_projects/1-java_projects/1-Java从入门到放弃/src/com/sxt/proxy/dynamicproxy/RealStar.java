package com.sxt.proxy.dynamicproxy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: RealStar.java
 * @time: 2020/2/7 13:53
 * @desc:
 */

public class RealStar implements Star {

    private String name = "真实明星";
    @Override
    public void confer() {
        System.out.println(name + "面谈！");
    }

    @Override
    public void signContract() {
        System.out.println(name + "签合同");
    }

    @Override
    public void bookTicket() {
        System.out.println(name + "订票");
    }

    @Override
    public void sing() {
        System.out.println(name + "唱歌");
    }

    @Override
    public void collectMoney() {
        System.out.println(name + "收钱");
    }
}
