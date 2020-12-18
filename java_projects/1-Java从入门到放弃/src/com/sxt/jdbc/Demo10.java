package com.sxt.jdbc;

import java.io.*;
import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试BLOB二进制大对象的使用
 */

public class Demo10 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            // ps = conn.prepareStatement("insert into t_user2 (username, headImg) values (?, ?)");
            // ps.setString(1, "狗子2");
            // 将图片文件的内容直接输入到数据库中
            // ps.setBlob(2, new FileInputStream("test.png"));
            // ps.executeUpdate();

            // 读取Blob字段
            ps = conn.prepareStatement("select * from t_user2 where username=?");
            ps.setObject(1, "狗子2");
            rs = ps.executeQuery();
            while (rs.next()) {
                Blob b = rs.getBlob("headImg");
                InputStream is = b.getBinaryStream();
                OutputStream os = new FileOutputStream("a1_input.png");
                int temp = 0;
                while((temp = is.read()) != -1){
                    os.write(temp);
                }
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
