package com.sxt.factory.abstractfactory;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Engine.java
 * @time: 2020/2/6 12:40
 * @desc:
 */

public interface Engine {
    void run();
    void start();
}

class LuxuryEngine implements Engine{

    @Override
    public void run() {
        System.out.println("转得快！");
    }

    @Override
    public void start() {
        System.out.println("启动快！可以自动启停！");
    }
}
class LowerEngine implements Engine{

    @Override
    public void run() {
        System.out.println("转得慢！");
    }

    @Override
    public void start() {
        System.out.println("启动慢！可以自动启停！");
    }
}
