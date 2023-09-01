package com.sxt.state;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @time: 2020/2/29 18:11
 * @desc: |已入住状态
 */

public class CheckedState implements State{

    @Override
    public void handle() {
        System.out.println("房间已入住！");
    }
}
