package com.sxt.test.reflection;

import com.sxt.test.bean.User;

import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo4.java
 * @time: 2020/1/9 10:44
 * @desc: 操作泛型
 */

public class Demo4 {
    public void test01(Map<String, User> map, List<User> list){
        System.out.println("Demo04.test01()");
    }

    public Map<Integer, User> test02(){
        System.out.println("Demo04.test02()");
        return null;
    }

    public static void main(String[] args){
        try{
            // 获得指定方法参数泛型信息
            Method m = Demo4.class.getMethod("test01", Map.class, List.class);
            Type[] t = m.getGenericParameterTypes();
            for (Type paramType: t){
                System.out.println("#" + paramType);
                if(paramType instanceof ParameterizedType){
                    Type[] genericTypes = ((ParameterizedType) paramType).getActualTypeArguments();
                    for (Type genericType: genericTypes){
                        System.out.println("泛型类型：" + genericType);
                    }
                }
            }

            // 获得指定方法返回值泛型信息
            Method m2 = Demo4.class.getMethod("test02");
            Type returnType = m2.getGenericReturnType();
            if(returnType instanceof ParameterizedType){
                Type[] genericTypes = ((ParameterizedType) returnType).getActualTypeArguments();

                for (Type genericType: genericTypes){
                        System.out.println("返回值，泛型类型：" + genericType);
                    }
            }
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        }
    }
}
