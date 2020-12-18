package com.sxt.testORM;

import com.sxt.jdbc.JDBCUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: |使用Javabean对象来封装一条记录
 * 使用List<Javabean>存储多条记录
 */

public class Demo03 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        List<Emp> list = new ArrayList<>();
        try {
            conn = JDBCUtil.getMysqlConn();
            ps = conn.prepareStatement("select empname, salary, age from emp where id > ?");
            ps.setObject(1, 0);
            rs = ps.executeQuery();
            while (rs.next()) {
                // System.out.println(rs.getString(1) + "-->" + rs.getDouble(2) + "-->" + rs.getInt(3));
                Emp emp = new Emp(rs.getString(1), rs.getInt(2), rs.getDouble(3));
                list.add(emp);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JDBCUtil.close(rs, ps, conn);
        }

        for (Emp e: list) {
            System.out.println(e);
        }
    }
}
