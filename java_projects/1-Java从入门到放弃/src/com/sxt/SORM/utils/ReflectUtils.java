package com.sxt.SORM.utils;

import java.lang.reflect.Method;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ReflectUtils.java
 * @time: 2020/3/11 13:44
 * @desc: | 封装了反射的常用操作
 */

public class ReflectUtils {
    /**
     * 调用obj对象对应属性fieldName的get方法
     *
     * @param fieldName 属性名
     * @param obj       Object对象
     * @return
     */
    public static Object invokeGet(String fieldName, Object obj) {
        // 通过反射机制，调用属性对应的get方法或set方法
        try {
            Class c = obj.getClass();
            Method m = c.getDeclaredMethod("get" + StringUtils.firstChar2UpperCase(fieldName), null);
            return m.invoke(obj, null);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void invokeSet(Object obj, String columnName, Object columnValue) {
        try {
            if (columnValue != null) {
                Method m = obj.getClass().getDeclaredMethod("set" + StringUtils.firstChar2UpperCase(columnName),
                        columnValue.getClass());
                m.invoke(obj, columnValue);
            }
        } catch (Exception e) {
            e.printStackTrace();

        }
    }
}
