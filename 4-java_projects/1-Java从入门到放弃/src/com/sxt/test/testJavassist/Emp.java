package com.sxt.test.testJavassist;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Emp.java
 * @time: 2020/1/14 9:28
 * @desc:
 */

@Author(name="litian", year=2020)
public class Emp {
    private int empno;
    private String name;

    public int getEmpno() {
        return empno;
    }

    public void setEmpno(int empno) {
        this.empno = empno;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Emp() {
    }

    public Emp(int empno, String name) {
        this.empno = empno;
        this.name = name;
    }

    public void sayHello(int a){
        System.out.println("Hello!: " + a);
    }
}
