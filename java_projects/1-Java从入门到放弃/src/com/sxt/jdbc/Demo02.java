package com.sxt.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2020/3/5 12:48
 * @desc: | 测试Statement接口的用法，执行sql语句以及sql注入问题
 */

public class Demo02 {
    public static void main(String[] args) {
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            // 建立连接（连接对象内部其实包含了Socket对象，是一个远程的连接。比较耗时！这是Connection对象管理的一个要点！）
            // 真正开发中，为了提高效率，都会使用连接池来管理连接对象！
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");
            Statement stmt = conn.createStatement();
            String sql = "insert into t_user (username, pwd, regTime) values ('赵六', 6666, now())";
            stmt.execute(sql);

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}
