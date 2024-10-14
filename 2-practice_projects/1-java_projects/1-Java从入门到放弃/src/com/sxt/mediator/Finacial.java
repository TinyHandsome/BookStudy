package com.sxt.mediator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Finacial.java
 * @time: 2020/2/14 19:11
 * @desc:
 */

public class Finacial implements Department {
    // 持有中介者（总经理）的引用
    private Mediator m;

    public Finacial(Mediator m) {
        this.m = m;
        m.regitster("finacial", this);
    }

    @Override
    public void selfAction() {
        System.out.println("数钱！");
    }

    @Override
    public void outAction() {
        System.out.println("钱太多了啊总经理！怎么花！");
    }
}
