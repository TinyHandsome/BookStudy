package com.sxt.jdbc;

import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试事务的基本用法
 */

public class Demo06 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps1 = null;
        PreparedStatement ps2 = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            // JDBC默认是自动提交
            conn.setAutoCommit(false);

            ps1 = conn.prepareStatement("insert into t_user (username, pwd) values (?, ?)");
            ps1.setObject(1, "狗子");
            ps1.setObject(2, "111");
            ps1.execute();
            System.out.println("插入一个用户1");
            Thread.sleep(6000);

            ps2 = conn.prepareStatement("insert into t_user (username, pwd) values (?, ?, ?)");
            ps2.setObject(1, "狗子2");
            ps2.setObject(2, "111");
            ps2.execute();
            System.out.println("插入一个用户2");

            conn.commit();

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
            try {
                conn.rollback();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            // 一定要将三个try catch分开写
            if (ps1 != null) {
                try {
                    ps1.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (ps2 != null) {
                try {
                    ps2.close();
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
