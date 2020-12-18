package com.sxt.prototype;

import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Sheep2.java
 * @time: 2020/2/6 15:53
 * @desc: 测试深复制
 */

public class Sheep2 implements Cloneable{
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

    public Sheep2(String sname, Date birthday) {
        this.sname = sname;
        this.birthday = birthday;
    }

    public Sheep2() {
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        // 直接调用object对象的clone()方法
        Object obj = super.clone();

        // 添加如下代码实现深复制
        Sheep2 s = (Sheep2) obj;
        // 把属性也进行克隆
        s.birthday = (Date) this.birthday.clone();

        return obj;
    }
}
