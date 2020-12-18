package com.sxt.observer;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/3/1 13:45
 * @desc: |
 */

public class Client {
    public static void main(String[] args){
        // 创建目标对象
        ConcreteSubject subject = new ConcreteSubject();
        // 创建多个观察者
        ObserverA obs1 = new ObserverA();
        ObserverA obs3 = new ObserverA();
        ObserverA obs2 = new ObserverA();

        // 让这三个观察者添加到subject对象的观察者队伍中
        subject.registerObserver(obs1);
        subject.registerObserver(obs2);
        subject.registerObserver(obs3);

        // 改变subject的状态
        subject.setState(3000);
        // 查看观察者的状态
        System.out.println(obs1.getMyState());
        System.out.println(obs2.getMyState());
        System.out.println(obs3.getMyState());
    }
}
