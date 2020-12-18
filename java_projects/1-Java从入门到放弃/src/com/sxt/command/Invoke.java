package com.sxt.command;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Invoke.java
 * @time: 2020/2/15 14:34
 * @desc: 命令的调用者和发起者
 */

public class Invoke {
    // 也可以通过容器放很多很多命令，进行批处理。比如数据库底层的事务管理
    private Command command;

    public Invoke(Command command) {
        this.command = command;
    }

    // 业务方法，用于调用命令类的方法
    public void call(){
        command.execute();
    }
}
