package com.sxt.jdbc;

import java.io.IOException;
import java.sql.*;
import java.util.Properties;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: JDBCUTIL.java
 * @time: 2020/3/8 19:43
 * @desc: |JDBC工具类
 */

public class JDBCUtil {
    // 可以帮助我们读取和处理资源文件中的信息
    private static Properties pros = null;
    static {
        /*静态代码块：只有在加载JDBCUtil类的时候调用一次*/
        pros = new Properties();
        try {
            pros.load(Thread.currentThread().getContextClassLoader().getResourceAsStream("com/sxt/jdbc/db.properties"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static Connection getMysqlConn() {
        /*获取数据库(mysql)驱动连接*/
        // 加载驱动类
        try {
            Class.forName(pros.getProperty("mysqlDriver"));
            return DriverManager.getConnection(
                    pros.getProperty("mysqlURL"),
                    pros.getProperty("mysqlUser"),
                    pros.getProperty("mysqlPwd"));
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static Connection getOracleConn() {
        /*获取数据库(oracle)驱动连接*/
        // 加载驱动类
        try {
            Class.forName(pros.getProperty("oracleDriver"));
            return DriverManager.getConnection(
                    pros.getProperty("oracleURL"),
                    pros.getProperty("oracleUser"),
                    pros.getProperty("oraclePwd"));
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void close(ResultSet rs, Statement ps, Connection conn){
        /*关闭接口方法*/
        try {
            if (rs != null){
                rs.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            if (ps != null){
                ps.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            if (conn != null){
                conn.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void close(Statement ps, Connection conn){
        /*关闭接口方法，重载*/
        try {
            if (ps != null){
                ps.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            if (conn != null){
                conn.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void close(Connection conn){
        /*关闭接口方法，重载*/
        try {
            if (conn != null){
                conn.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
