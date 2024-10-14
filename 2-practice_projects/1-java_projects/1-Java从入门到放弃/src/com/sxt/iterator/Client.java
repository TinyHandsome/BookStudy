package com.sxt.iterator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/14 18:53
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        ConcreteMyAggregate cma = new ConcreteMyAggregate();
        cma.addObject("aa");
        cma.addObject("bb");
        cma.addObject("cc");

        MyIterator iter = cma.createIterator();
        while(iter.hasNext()){
            System.out.println(iter.getCurrentObj());
            iter.next();
        }
    }
}
