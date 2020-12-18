package com.sxt.jdbc;

import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 批处理
 */

public class Demo05 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");
            // 设为手动提交
            conn.setAutoCommit(false);
            long start = System.currentTimeMillis();
            stmt = conn.createStatement();
            for (int i = 0; i < 20000; i++) {
                stmt.addBatch("insert into t_user (username, pwd, regTime) values ('li'" + ", 666666, now())");
                stmt.executeBatch();
            }
            // 提交事务
            conn.commit();
            long  end = System.currentTimeMillis();
            System.out.println("插入20000条数据，耗时（毫秒）：" + (end - start));
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
            if (stmt != null) {
                try {
                    stmt.close();
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
