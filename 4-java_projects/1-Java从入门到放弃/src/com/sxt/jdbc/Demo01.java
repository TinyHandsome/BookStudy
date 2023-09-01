package com.sxt.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2020/3/5 12:48
 * @desc: | 测试跟数据库建立连接
 * 如果报错：参考连接：https://www.cnblogs.com/cn-chy-com/p/10145690.html
 */

public class Demo01 {
    public static void main(String[] args) {
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            long start = System.currentTimeMillis();
            // 建立连接（连接对象内部其实包含了Socket对象，是一个远程的连接。比较耗时！这是Connection对象管理的一个要点！）
            // 真正开发中，为了提高效率，都会使用连接池来管理连接对象！
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");
            long end = System.currentTimeMillis();
            System.out.println(conn);
            System.out.println("建立连接耗时：" + (end - start) + "ms毫秒");

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}
