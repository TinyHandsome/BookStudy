package com.sxt.jdbc;

import java.io.*;
import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试CLOB文本大对象的使用
 * 包含：将字符串、文件内容插入数据库中的CLOB字段，将CLOB字段值取出来操作
 */

public class Demo09 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            ps = conn.prepareStatement("insert into t_user2 (username, myInfo) values (?, ?)");
            ps.setString(1, "狗子");
            // 将文本文件的内容直接输入到数据库中
            // ps.setClob(2, new FileReader(new File("a1.txt")));
            // 通过流的操作写入字符串内容
            // ps.setClob(2, new BufferedReader(new InputStreamReader(new ByteArrayInputStream("aaaabbbb".getBytes()))));
            // ps.executeUpdate();

            // 读取Clob字段
            ps = conn.prepareStatement("select * from t_user2 where username=?");
            ps.setObject(1, "狗子");
            rs = ps.executeQuery();
            while (rs.next()) {
                Clob c = rs.getClob("myInfo");
                Reader r = c.getCharacterStream();
                int temp = 0;
                while((temp = r.read()) != -1){
                    System.out.print((char)temp);
                }
                System.out.println();
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
            try {
                conn.rollback();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        } catch (IOException e) {
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
