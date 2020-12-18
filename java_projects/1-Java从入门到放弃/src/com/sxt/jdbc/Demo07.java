package com.sxt.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Random;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试时间处理（java.sql.Date, java.sql.Time, java.sql.Timestamp）
 */

public class Demo07 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps1 = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            for (int i = 0; i < 1000; i++) {
                ps1 = conn.prepareStatement("insert into t_user (username, pwd, regTime, lastLoginTime) values (?, ?, ?, ?)");
                ps1.setObject(1, "狗子" + i);
                ps1.setObject(2, "111");

                // 定义随机数
                int rand = 10000000 + new Random().nextInt(1000000000);

                java.sql.Date date = new java.sql.Date(System.currentTimeMillis() - rand);
                ps1.setDate(3, date);

                // 如果需要插入制定日期，可以使用Calendar或DateFormat
                java.sql.Timestamp stamp = new java.sql.Timestamp(System.currentTimeMillis());
                ps1.setTimestamp(4, stamp);

                ps1.execute();
            }

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
            try {
                conn.rollback();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        } finally {
            // 一定要将三个try catch分开写
            if (ps1 != null) {
                try {
                    ps1.close();
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
