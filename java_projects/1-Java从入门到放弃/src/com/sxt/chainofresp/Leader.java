package com.sxt.chainofresp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Leader.java
 * @time: 2020/2/10 18:02
     * @desc: 抽象类 领导
 */

public abstract class Leader {
    protected String name;
        // 领导的下一个责任领导
    protected Leader nextLeader;

    public Leader(String name) {
        this.name = name;
    }

    // 设定责任链上的后继对象
    public void setNextLeader(Leader nextLeader) {
        this.nextLeader = nextLeader;
    }

    // 处理请求的核心业务方法
    public abstract void handleRequest(LeaveRequest request);
}
