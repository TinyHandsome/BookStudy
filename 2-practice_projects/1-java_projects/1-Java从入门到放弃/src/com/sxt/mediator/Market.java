package com.sxt.mediator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Market.java
 * @time: 2020/2/14 19:13
 * @desc:
 */

public class Market implements Department {
    // 持有中介者（总经理）的引用
    private Mediator m;

    public Market(Mediator m) {
        this.m = m;
        m.regitster("market", this);
    }

    @Override
    public void selfAction() {
        System.out.println("跑去接项目！");
    }

    @Override
    public void outAction() {
        System.out.println("承接项目的进度！需要资金支持！");
        m.command("finacial");
    }
}
