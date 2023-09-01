package com.sxt.jdbc;

import java.sql.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试使用JDBCUtil工具类来简化JDBC开发
 */

public class Demo11 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;

        try {
            conn = JDBCUtil.getMysqlConn();
            ps = conn.prepareStatement("insert into t_user (username) values (?)");
            ps.setString(1, "hehe");
            ps.execute();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            JDBCUtil.close(rs, ps, conn);
        }
    }
}
