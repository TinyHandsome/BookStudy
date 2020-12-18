package com.sxt.proxy.staticproxy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ProxyStar.java
 * @time: 2020/2/7 13:55
 * @desc:
 */

public class ProxyStar implements Star {
    private String name = "经纪人";
    private Star star;

    public ProxyStar(Star star) {
        this.star = star;
    }

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
        star.sing();
    }

    @Override
    public void collectMoney() {
        System.out.println(name + "收钱");
    }
}
