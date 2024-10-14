package com.sxt.memento;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: EmpMemento.java
 * @time: 2020/3/1 14:54
 * @desc: |备忘录类
 */

public class EmpMemento {
    private String name;
    private int age;
    private double salary;

    public EmpMemento(Emp e){
        this.name = e.getName();
        this.age = e.getAge();
        this.salary = e.getSalary();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }
}
