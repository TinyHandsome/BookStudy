package com.sxt.chainofresp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Director.java
 * @time: 2020/2/10 18:06
 * @desc:
 */

public class Director extends Leader {

    public Director(String name) {
        super(name);
    }

    @Override
    public void handleRequest(LeaveRequest request) {
        if(request.getLeaveDays() < 3){
            System.out.println("员工：" + request.getEmpName() + "请假：" + request.getLeaveDays() + "天，理由是：" + request.getReason());
            System.out.println("主任：" + this.name + "审批通过！");
        }else{
            if(this.nextLeader != null){
                this.nextLeader.handleRequest(request);
            }
        }
    }
}
