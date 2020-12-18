package com.sxt.strategy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/29 16:56
 * @desc: |
 */

public class Client {
    public static void main(String[] args){
        Strategy s1 = new OldCustomerManyStrategy();
        Context ctx = new Context(s1);
        ctx.printPrice(998);
    }
}
