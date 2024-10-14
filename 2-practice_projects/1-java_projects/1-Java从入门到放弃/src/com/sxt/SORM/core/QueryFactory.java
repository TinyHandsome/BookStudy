package com.sxt.SORM.core;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: QueryFactory.java
 * @time: 2020/3/11 13:33
 * @desc: |创建Query对象的工厂类：单例+克隆+工厂
 */

public class QueryFactory {
    private static QueryFactory factory = new QueryFactory();
    // 原型对象
    private static Query prototypeObj;

    static{
        try {
            // 加载指定的Query类
            Class c = Class.forName(DBManager.getConf().getQueryClass());
            prototypeObj = (Query) c.newInstance();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 私有构造器
    private QueryFactory(){}

    public static Query createQuery(){
        try {
            return (Query) prototypeObj.clone();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
