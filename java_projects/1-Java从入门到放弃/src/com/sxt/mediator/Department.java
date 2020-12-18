package com.sxt.mediator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Department.java
 * @time: 2020/2/14 19:08
 * @desc: 同事类的接口
 */

public interface Department {
    // 做本部门的事情
    void selfAction();
    // 向总经理发出申请
    void outAction();
}
