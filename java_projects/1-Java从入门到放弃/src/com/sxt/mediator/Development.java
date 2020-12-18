package com.sxt.mediator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Development.java
 * @time: 2020/2/14 19:09
 * @desc:
 */

public class Development implements Department {
    // 持有中介者（总经理）的引用
    private Mediator m;

    public Development(Mediator m) {
        this.m = m;
        m.regitster("development", this);
    }

    @Override
    public void selfAction() {
        System.out.println("专心搞科研！");
    }

    @Override
    public void outAction() {
        System.out.println("向总经理汇报工作！需要资金支持！");
    }
}
