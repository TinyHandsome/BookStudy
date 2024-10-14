package com.sxt.test.bean;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: User.java
 * @time: 2019/12/17 19:00
 * @desc:
 */

public class User {
    private int id;
    private int age;
    private String uname;

    // javabean必须要有无参的构造方法！为了反射的方便
    public User(){
    }

    public User(int id, int age, String uname) {
        this.id = id;
        this.age = age;
        this.uname = uname;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getUname() {
        return uname;
    }

    public void setUname(String uname) {
        this.uname = uname;
    }
}
