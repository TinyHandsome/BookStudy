package com.sxt.state;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Context.java
 * @time: 2020/2/29 18:15
 * @desc: |
 */

public class HomeContext {
    // 当前状态
    private State state;

    public HomeContext(State state) {
        this.state = state;
        this.state.handle();
    }

    // 设置不同状态
    public void setState(State s){
        System.out.println("修改状态！");
        state = s;
        state.handle();
    }
}
