package com.sxt.observer;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ObserverA.java
 * @time: 2020/3/1 13:43
 * @desc: |
 */

public class ObserverA implements Observer {
    // myState需要跟目标对象的值保持一致
    private int myState;

    public int getMyState() {
        return myState;
    }

    public void setMyState(int myState) {
        this.myState = myState;
    }

    @Override
    public void update(Subject subject) {
        myState = ((ConcreteSubject)subject).getState();
    }
}
