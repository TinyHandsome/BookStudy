package com.sxt.test.annotation;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Student.java
 * @time: 2019/12/16 12:43
 * @desc:
 */

@LTTable("tb_student")
public class Student {

    @LTField(columnName = "id", type = "int", length = 10)
    private int id;
    @LTField(columnName = "sname", type = "varchar", length = 10)
    private String studentName;
    @LTField(columnName = "age", type = "int", length = 3)
    private int age;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
