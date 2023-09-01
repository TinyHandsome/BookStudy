package com.sxt.template;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/29 17:11
 * @desc: |
 */

public class Client {
    public static void main(String[] args){
        BankTemplateMethod btm = new DrawMoney();
        btm.process();

        // 通常采用匿名内部类
        BankTemplateMethod btm2 = new BankTemplateMethod() {
            @Override
            public void transact() {
                // 存钱
                System.out.println("我要存钱");
            }
        };
        btm2.process();
    }
}

// 取款
class DrawMoney extends BankTemplateMethod{

    @Override
    public void transact() {
        System.out.println("我要取款！");
    }
}
