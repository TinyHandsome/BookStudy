package com.sxt.memento;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/3/1 14:58
 * @desc: |
 */

public class Client {
    public static void main(String[] args) {
        CareTaker taker = new CareTaker();
        Emp emp = new Emp("李英俊", 18, 900);
        System.out.println("第一次创建对象：" + emp.getName() + emp.getAge() + emp.getSalary());

        // 进行一次备份
        taker.setMemento(emp.memento());

        emp.setAge(38);
        emp.setName("哈哈");
        emp.setSalary(10);
        System.out.println("第二次创建对象：" + emp.getName() + emp.getAge() + emp.getSalary());

        // 恢复到备忘录对象保存的状态
        emp.recovery(taker.getMemento());
        System.out.println("第三次创建对象：" + emp.getName() + emp.getAge() + emp.getSalary());
    }
}
