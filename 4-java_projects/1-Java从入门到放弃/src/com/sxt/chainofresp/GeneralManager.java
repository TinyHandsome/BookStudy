package com.sxt.chainofresp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Manager.java
 * @time: 2020/2/10 18:06
 * @desc: 总经理
 */

public class GeneralManager extends Leader {

    public GeneralManager(String name) {
        super(name);
    }

    @Override
    public void handleRequest(LeaveRequest request) {
        if(request.getLeaveDays() < 30){
            System.out.println("员工：" + request.getEmpName() + "请假：" + request.getLeaveDays() + "天，理由是：" + request.getReason());
            System.out.println("总经理：" + this.name + "审批通过！");
        }else{
            System.out.println("莫非" + request.getEmpName() + "想辞职！竟然请假" + request.getLeaveDays() + "天！");
        }
    }
}
