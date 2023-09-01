package com.sxt.test.testJavassist;

import javassist.*;

import java.lang.reflect.Method;
import java.util.Arrays;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo2.java
 * @time: 2020/1/14 10:45
 * @desc: 测试javassist的API
 */

public class Demo2 {
    /*
      处理类的基本用法
     */
    public static void test1() throws Exception {
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.get("com.sxt.test.testJavassist.Emp");

        byte[] bytes = cc.toBytecode();
        System.out.println(Arrays.toString(bytes));

        // 获取类名
        System.out.println(cc.getName());
        // 获取简要类名
        System.out.println(cc.getSimpleName());
        // 获得父类
        System.out.println(cc.getSuperclass());
        // 获得接口
        System.out.println(cc.getInterfaces());
    }

    public static void test2() throws Exception {
        /*
        测试产生新的方法
         */
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.get("com.sxt.test.testJavassist.Emp");

        // 新建方法1
        CtMethod m1 = CtNewMethod.make("public int add(int a, int b){return a+b;}", cc);
        // 新建方法2
        CtMethod m2 = new CtMethod(CtClass.intType, "add", new CtClass[]{CtClass.intType, CtClass.intType}, cc);
        // 设置权限
        m2.setModifiers(Modifier.PUBLIC);
        // 设置方法体 $1等等代表的是形参的占位符
        m2.setBody("{System.out.println(\"冲冲冲！\"); return $1+$2;}");

        cc.addMethod(m2);

        // 通过反射调用新生成的方法
        Class clazz = cc.toClass();
        // 通过调用Emp无参构造器，创建新的Emp对象
        Object obj = clazz.newInstance();
        Method method = clazz.getDeclaredMethod("add", int.class, int.class);
        Object result = method.invoke(obj, 200, 300);
        System.out.println(result);
    }

    public static void test3() throws Exception {
        /*
        对已有的方法进行修改
         */
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.get("com.sxt.test.testJavassist.Emp");

        CtMethod cm = cc.getDeclaredMethod("sayHello", new CtClass[]{CtClass.intType});
        cm.insertBefore("System.out.println($1);System.out.println(\"start!!!\");");
        cm.insertAfter("System.out.println(\"end!!!\");");
        // 在某一行前面加代码，从1开始计数，不存在迭代效应，也就是改行代码的行数不会因加入了新的代码而改变
        cm.insertAt(41, "System.out.println(\"???\");");
        cm.insertAt(42, "System.out.println(\"!!!\");");

        // 通过反射调用新生成的方法
        Class clazz = cc.toClass();
        Object obj = clazz.newInstance();
        Method method = clazz.getDeclaredMethod("sayHello", int.class);
        Object result = method.invoke(obj, 200);
        System.out.println(result);

    }

    public static void test4() throws Exception {
        /*
        对已有的属性进行修改
         */
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.get("com.sxt.test.testJavassist.Emp");

        // CtField f1 = CtField.make("private int empno;", cc);
        CtField f1 = new CtField(CtClass.intType, "salary", cc);
        f1.setModifiers(Modifier.PRIVATE);
        // 后面的参数是默认值，如果不写的话，就没有默认值
        cc.addField(f1, "1000");
        // 获取指定的属性
        cc.getDeclaredField("salary");

        // 除了直接通过增加方法的方式提供getter和setter方法，还可以通过以下方式
        cc.addMethod(CtNewMethod.getter("getSalary", f1));
        cc.addMethod(CtNewMethod.setter("setSalary", f1));
    }

    public static void test5() throws Exception {
        /*
        查看已有构造方法，并进行修改
         */
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.get("com.sxt.test.testJavassist.Emp");

        CtConstructor[] cs = cc.getConstructors();
        for (CtConstructor c : cs) {
            System.out.println(c.getLongName());
            c.insertBefore("System.out.println(\"what？\");");
        }
        // 通过反射调用新生成的方法
        Class clazz = cc.toClass();
        Object obj = clazz.newInstance();
    }

    public static void test6() throws Exception {
        /*
        注解
         */
        ClassPool pool = ClassPool.getDefault();
        CtClass cc = pool.get("com.sxt.test.testJavassist.Emp");
        Object[] all = cc.getAnnotations();
        Author a = (Author) all[0];
        String name = a.name();
        int year = a.year();
        System.out.println("name: " + name + "year: " + year);
    }

    public static void main(String[] args) throws Exception {
        test6();
    }
}
