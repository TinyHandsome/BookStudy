package com.sxt.SORM.utils;

import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: JDBCUtils.java
 * @time: 2020/3/11 13:43
 * @desc: | 封装了JDBC查询常用的操作
 */

public class JDBCUtils {
    /**
     * 给sql设置参数，就是？位置的参数
     * @param ps 预编译sql语句对象
     * @param params 参数
     */
    public static void handleParams(PreparedStatement ps, Object[] params) {
        if (params != null) {
            for (int i = 0; i < params.length; i++) {
                try {
                    ps.setObject(1 + i, params[i]);
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
