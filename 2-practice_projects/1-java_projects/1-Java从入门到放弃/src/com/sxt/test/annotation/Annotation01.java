package com.sxt.test.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Annotation01.java
 * @time: 2019/12/16 9:52
 * @desc: 自定义注解
 */

// 表示这个类只能修饰方法和类
@Target(value = {ElementType.METHOD, ElementType.TYPE})
// 表示这个类运行时有效，可以被反射读取
@Retention(RetentionPolicy.RUNTIME)
public @interface Annotation01 {
    String studentName() default "";
    int age() default 0;
    int id() default -1;

    String[] schools() default {"1", "2"};
}
