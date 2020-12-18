package com.sxt.proxy.dynamicproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: StarHandler.java
 * @time: 2020/2/7 16:19
 * @desc:
 */

public class StarHandler implements InvocationHandler {

    Star realStar;

    public StarHandler(Star realStar) {
        this.realStar = realStar;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        Object obj = null;
        System.out.println("真正的方法执行前！");
        System.out.println("面谈，签合同等。。。");
        if (method.getName().equals("sing")) {
            obj = method.invoke(realStar, args);
        }
        System.out.println("真正的方法执行后！");
        System.out.println("收钱！");

        return obj;
    }
}
