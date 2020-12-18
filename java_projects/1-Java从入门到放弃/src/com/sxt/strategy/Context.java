package com.sxt.strategy;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Context.java
 * @time: 2020/2/29 16:40
 * @desc: 负责和具体的策略类交互，这样的话，具体的算法和直接的客户端调用分类了，使得算法可以独立于客户端独立的变化。
 *        如果使用Spring的依赖注入功能，还可以通过配置文件，动态的注入不同策略对象，动态的切换不同的算法。
 */

public class Context {
    // 当前采用的算法对象
    private Strategy strategy;

    // 可以通过构造器来注入
    public Context(Strategy strategy) {
        this.strategy = strategy;
    }

    // 或者通过加一个set方法来注入
    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }

    public void printPrice(double s){
        System.out.println("您的报价："  + strategy.getPrice(s));
    }
}
