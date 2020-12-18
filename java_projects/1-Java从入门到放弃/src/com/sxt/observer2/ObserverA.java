package com.sxt.observer2;

import java.util.Observable;
import java.util.Observer;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ObserverA.java
 * @time: 2020/3/1 14:07
 * @desc: |
 */

public class ObserverA implements Observer {
    private int myState;

    public int getMyState() {
        return myState;
    }

    public void setMyState(int myState) {
        this.myState = myState;
    }

    @Override
    public void update(Observable o, Object arg) {
        myState = ((ConcreteSubject)o).getState();
    }
}
