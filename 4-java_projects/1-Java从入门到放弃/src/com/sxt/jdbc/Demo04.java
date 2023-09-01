package com.sxt.jdbc;

import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试ResultSet结果集的用法
 * 记得要关闭打开的接口
 */

public class Demo04 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            // ?是占位符
            String sql = "select id, username, pwd from t_user where id>?";
            ps = conn.prepareStatement(sql);
            // 把id>2的记录都取出来
            ps.setObject(1, 2);
            rs = ps.executeQuery();

            while (rs.next()) {
                // 数字代表哪一列
                System.out.println(rs.getInt(1) + "-->" + rs.getString(2) + "-->" + rs.getString(3));
            }

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            // 一定要将三个try catch分开写
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (ps != null) {
                try {
                    ps.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
