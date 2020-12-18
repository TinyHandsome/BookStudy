package com.sxt.strategy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @time: 2020/2/29 16:37
 * @desc: 普通客户大批量购买
 */

public class NewCustomerManyStrategy implements Strategy{

    @Override
    public double getPrice(double standarPrice) {
        System.out.println("打九折！");
        return standarPrice*0.9;
    }
}
