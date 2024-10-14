package com.sxt.testORM;

import java.sql.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Emp.java
 * @time: 2020/3/10 14:35
 * @desc: |表结构和类对应
 */

public class Emp {
    private Integer id;
    private String empname;
    private Integer age;
    private Double salary;
    private Date birthday;
    private Integer deptId;

    public Emp(String empname, Integer age, Double salary) {
        this.empname = empname;
        this.age = age;
        this.salary = salary;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getEmpname() {
        return empname;
    }

    public void setEmpname(String empname) {
        this.empname = empname;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public Integer getDeptId() {
        return deptId;
    }

    public void setDeptId(Integer deptId) {
        this.deptId = deptId;
    }

    public Emp(String empname, Integer age, Double salary, Date birthday, Integer deptId) {
        this.empname = empname;
        this.age = age;
        this.salary = salary;
        this.birthday = birthday;
        this.deptId = deptId;
    }

    public Emp(Integer id, String empname, Integer age, Double salary, Date birthday, Integer deptId) {
        this.id = id;
        this.empname = empname;
        this.age = age;
        this.salary = salary;
        this.birthday = birthday;
        this.deptId = deptId;
    }

    public Emp() {
    }

    @Override
    public String toString() {
        return empname + "-->" + age + "-->" + salary;
    }
}
