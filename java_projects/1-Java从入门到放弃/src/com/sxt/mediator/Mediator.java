package com.sxt.mediator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Mediator.java
 * @time: 2020/2/14 19:07
 * @desc: 总经理类的接口
 */

public interface Mediator {
    void regitster(String dname, Department d);
    void command(String dname);
}
