package com.sxt.command;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Command.java
 * @time: 2020/2/15 14:29
 * @desc: 命令管理
 */

public interface Command {
    // 这个方法是一个返回结果为空的方法
    // 实际项目中，可以根据需求设计多个不同的方法
    void execute();
}

class ConcreteCommand implements Command{
    // 命令的真正执行者
    private Receiver receiver;

    public ConcreteCommand(Receiver receiver) {
        this.receiver = receiver;
    }

    @Override
    public void execute() {
        // 命令真正执行前或后，执行相关的处理
        receiver.action();
    }
}
