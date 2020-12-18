package com.sxt.jdbc;

import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2020/3/5 12:48
 * @desc: | 测试PreparedStatement的基本用法
 */

public class Demo03 {
    public static void main(String[] args) {
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            // ?是占位符
            String sql = "insert into t_user (username, pwd, regTime) values (?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(sql);
            // 参数索引是从1开始计算，而不是0
            // ps.setString(1, "傻瓜");
            // ps.setString(2, "12345");

            // 还可以不管类型直接setObject
            // ps.setObject(1, "傻瓜2");
            // ps.setObject(2, "12344");

            // 设置时间：注意该时间的格式应该是java.sql.Date
            ps.setObject(1, "傻瓜3");
            ps.setObject(2, "12343");
            ps.setObject(3, new java.sql.Date(System.currentTimeMillis()));

            System.out.println("插入一行记录");
            // 返回是否有结果集
            // ps.execute();
            // 返回更新的行数
            int count = ps.executeUpdate();
            System.out.println(count);

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}
