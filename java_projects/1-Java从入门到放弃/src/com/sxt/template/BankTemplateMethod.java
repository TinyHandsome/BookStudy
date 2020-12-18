package com.sxt.template;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: BankTemplateMethod.java
 * @time: 2020/2/29 17:10
 * @desc: |
 */

public abstract class BankTemplateMethod {
    // 具体方法
    public void takeNumber(){
        System.out.println("取号排队！");
    }

    // 办理具体的业务，钩子方法
    public abstract void transact();

    public void evaluate(){
        System.out.println("反馈评分！");
    }

    // 模板方法
    public final void process(){
        this.takeNumber();
        this.transact();
        this.evaluate();
    }
}
