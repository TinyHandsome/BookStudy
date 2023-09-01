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
 * @file: Demo01.java
 * @time: 2020/3/10 13:29
 * @desc: |测试使用Object数组来封装一条记录
 * 使用List<Object[]>存储多条记录
 */

public class Demo01 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        List<Object[]> list = new ArrayList<>();
        try {
            conn = JDBCUtil.getMysqlConn();
            ps = conn.prepareStatement("select empname, salary, age from emp where id > ?");
            ps.setObject(1, 0);
            rs = ps.executeQuery();
            while (rs.next()) {
                // System.out.println(rs.getString(1) + "-->" + rs.getDouble(2) + "-->" + rs.getInt(3));
                Object[] objs = new Object[3];
                objs[0] = rs.getObject(1);
                objs[1] = rs.getObject(2);
                objs[2] = rs.getObject(3);

                list.add(objs);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JDBCUtil.close(rs, ps, conn);
        }

        for (Object[] objs : list) {
            System.out.println(objs[0] + "-->" + objs[1] + "-->" + objs[2]);
        }
    }
}
