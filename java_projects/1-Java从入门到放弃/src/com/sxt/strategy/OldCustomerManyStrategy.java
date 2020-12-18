package com.sxt.strategy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @time: 2020/2/29 16:37
 * @desc: 老客户大批量购买
 */

public class OldCustomerManyStrategy implements Strategy{

    @Override
    public double getPrice(double standarPrice) {
        System.out.println("打八折！");
        return standarPrice*0.8;
    }
}
