package com.sxt.testORM;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Dept.java
 * @time: 2020/3/10 14:38
 * @desc: |
 */

public class Dept {
    private Integer id;
    private String dname;
    private String address;

    public Dept() {
    }

    public Dept(String dname, String address) {
        this.dname = dname;
        this.address = address;
    }

    public Dept(Integer id, String dname, String address) {
        this.id = id;
        this.dname = dname;
        this.address = address;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getDname() {
        return dname;
    }

    public void setDname(String dname) {
        this.dname = dname;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
