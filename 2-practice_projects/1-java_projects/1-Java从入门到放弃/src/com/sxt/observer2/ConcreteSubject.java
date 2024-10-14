package com.sxt.observer2;

import java.util.Observable;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ConcreteSubject.java
 * @time: 2020/3/1 14:05
 * @desc: |
 */

public class ConcreteSubject extends Observable {
    private int state;

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }

    public void set(int s){
        // 目标对象的状态发生了改变
        state = s;
        // 表示目标对象已经发生了更改
        setChanged();
        // 通知所有的观察者
        notifyObservers(state);
    }
}
