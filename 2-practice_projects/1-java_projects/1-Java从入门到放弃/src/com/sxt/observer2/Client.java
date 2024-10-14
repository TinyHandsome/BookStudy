package com.sxt.observer2;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/3/1 14:09
 * @desc: |
 */

public class Client {
    public static void main(String[] args){
        // 创建目标对象Observable
        ConcreteSubject subject = new ConcreteSubject();

        // 创建观察者
        ObserverA obs1 = new ObserverA();
        ObserverA obs2 = new ObserverA();
        ObserverA obs3 = new ObserverA();

        // 将上面三个观察者对象加到目标对象subject的观察者容器中
        subject.addObserver(obs1);
        subject.addObserver(obs2);
        subject.addObserver(obs3);

        // 改变subject对象的状态
        subject.set(300);

        // 看看观察者的状态发生变化了没
        System.out.println(obs1.getMyState());
        System.out.println(obs2.getMyState());
        System.out.println(obs3.getMyState());
    }
}
