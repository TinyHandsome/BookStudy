package com.sxt.observer;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ConcreteSubject.java
 * @time: 2020/3/1 13:41
 * @desc: |
 */

public class ConcreteSubject extends Subject {
    private int state;

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
        // 主题对象/目标对象的值发生了变化，请通知所有的观察者
        this.notifyAllObservers();
    }
}
