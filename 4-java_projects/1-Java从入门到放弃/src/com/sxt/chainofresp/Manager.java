package com.sxt.chainofresp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Manager.java
 * @time: 2020/2/10 18:06
 * @desc: 经理
 */

public class Manager extends Leader {

    public Manager(String name) {
        super(name);
    }

    @Override
    public void handleRequest(LeaveRequest request) {
        if(request.getLeaveDays() < 10){
            System.out.println("员工：" + request.getEmpName() + "请假：" + request.getLeaveDays() + "天，理由是：" + request.getReason());
            System.out.println("经理：" + this.name + "审批通过！");
        }else{
            if(this.nextLeader != null){
                this.nextLeader.handleRequest(request);
            }
        }
    }
}
