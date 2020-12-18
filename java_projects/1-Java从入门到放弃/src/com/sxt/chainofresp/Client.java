package com.sxt.chainofresp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/10 18:11
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        Leader a = new Director("张三");
        Leader b = new Manager("李四");
        Leader c = new GeneralManager("王五");

        // 组织责任链对象关系
        a.setNextLeader(b);
        b.setNextLeader(c);

        // 开始请假操作
        LeaveRequest req1 = new LeaveRequest("Tom", 10, "回家睡觉！");
        a.handleRequest(req1);
    }
}
