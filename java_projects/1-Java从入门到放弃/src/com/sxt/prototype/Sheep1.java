package com.sxt.prototype;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Sheep1.java
 * @time: 2020/2/6 15:53
 * @desc: 测试浅复制
 */

public class Sheep1 implements Cloneable, Serializable {
    private String sname;
    private Date birthday;

    public String getSname() {
        return sname;
    }

    public void setSname(String sname) {
        this.sname = sname;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public Sheep1(String sname, Date birthday) {
        this.sname = sname;
        this.birthday = birthday;
    }

    public Sheep1() {
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        // 直接调用object对象的clone()方法
        Object obj = super.clone();
        return obj;
    }
}
