package com.sxt.memento;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CareTaker.java
 * @time: 2020/3/1 14:58
 * @desc: |负责人类：管理备忘录对象
 */

public class CareTaker {
    private EmpMemento memento;

    public EmpMemento getMemento() {
        return memento;
    }

    public void setMemento(EmpMemento memento) {
        this.memento = memento;
    }
}
