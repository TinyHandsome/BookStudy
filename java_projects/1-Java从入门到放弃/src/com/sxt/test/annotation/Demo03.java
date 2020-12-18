package com.sxt.test.annotation;

import java.lang.annotation.Annotation;
import java.lang.reflect.Field;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo03.java
 * @time: 2019/12/16 12:49
 * @desc: 使用反射读取注解的信息，模拟处理注解信息的流程
 */

public class Demo03 {
    public static void main(String[] args) {
        try {
            Class clazz = Class.forName("com.sxt.test.annotation.Student");

            // 获得类的所有有效注解
            Annotation[] annotations = clazz.getAnnotations();
            for (Annotation a : annotations) {
                System.out.println(a);
            }

            // 获得类的指定的注解
            LTTable st = (LTTable) clazz.getAnnotation(LTTable.class);
            System.out.println(st.value());

            // 获得类的属性的注解
            Field f = clazz.getDeclaredField("studentName");
            LTField ltField = f.getAnnotation(LTField.class);
            System.out.println(ltField.columnName()+"-->"+ltField.type()+"-->"+ltField.length());

            // 根据获得的表明、字段的信息，拼出DDL语句，然后使用JDBC执行这个SQL，在数据库中生成相关的表
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
