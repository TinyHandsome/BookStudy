package com.sxt.state;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @time: 2020/2/29 18:11
 * @desc: |空闲状态
 */

public class FreeState implements State{

    @Override
    public void handle() {
        System.out.println("房间空闲！没人住！");
    }
}
