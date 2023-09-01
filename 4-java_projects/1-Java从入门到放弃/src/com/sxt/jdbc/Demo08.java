package com.sxt.jdbc;

import java.sql.*;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试时间处理，取出指定时间段的数据
 */

public class Demo08 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc?serverTimezone=UTC", "root", "123456");

            // 选择满足regTime条件的记录，Timestamp格式同理，把java.sql.Date改成java.sql.Timestamp即可getDate改成getTimestamp
            ps = conn.prepareStatement("select * from t_user where regTime>? and regTime<?");
            java.sql.Date start = new java.sql.Date(str2Date("2020-3-1 10:23:45"));
            java.sql.Date end = new java.sql.Date(str2Date("2020-3-3 10:23:45"));
            ps.setObject(1, start);
            ps.setObject(2, end);
            rs = ps.executeQuery();
            while(rs.next()){
                System.out.println(rs.getInt("id") + "-->" + rs.getString("username") + "-->" + rs.getDate("regTime"));
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

    public static long str2Date(String dateStr){
        /*将字符串代表的日期转为long数字（格式：yyyy-MM-dd hh:mm:ss）*/
        DateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        try {
            return format.parse(dateStr).getTime();
        } catch (ParseException e) {
            e.printStackTrace();
            return 0;
        }
    }
}
