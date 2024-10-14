package com.sxt.test.testJavassist;

import javassist.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo1.java
 * @time: 2020/1/14 9:21
 * @desc: 测试使用javassist生成一个新的类
 */

public class Demo1 {
    public static void main(String[] args) throws Exception {
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.makeClass("com.sxt.test.testJavassist.EmpTest");

        // 创建属性
        CtField f1 = CtField.make("private int empno;", cc);
        CtField f2 = CtField.make("private String ename;", cc);
        cc.addField(f1);
        cc.addField(f2);

        // 创建方法
        CtMethod m1 = CtMethod.make("public int getEmpno(){return empno;}", cc);
        CtMethod m2 = CtMethod.make("public void setEmpno(int empno){this.empno=empno;}", cc);
        cc.addMethod(m1);
        cc.addMethod(m2);

        // 添加构造器
        CtConstructor constructor = new CtConstructor(new CtClass[]{CtClass.intType, pool.get("java.lang.String")}, cc);
        constructor.setBody("{this.empno = empno; this.ename = ename;}");
        cc.addConstructor(constructor);

        // 将上面构造好的类写入到下面的工作空间下面
        cc.writeFile("D:\\java_test");
        System.out.println("生成类，成功！");

    }
}
