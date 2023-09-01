package com.sxt.testORM;

import com.sxt.jdbc.JDBCUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: |测试使用Map来封装一条记录
 * 使用List<Map>存储多条记录（也可用Map<Map>）
 */

public class Demo02 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        // 使用一个Map封装一条记录
        List<Map<String, Object>> list = new ArrayList<>();
        try {
            conn = JDBCUtil.getMysqlConn();
            ps = conn.prepareStatement("select empname, salary, age from emp where id > ?");
            ps.setObject(1, 0);
            rs = ps.executeQuery();
            while (rs.next()) {
                // System.out.println(rs.getString(1) + "-->" + rs.getDouble(2) + "-->" + rs.getInt(3));
                Map<String, Object> row = new HashMap<>();
                row.put("empname", rs.getString(1));
                row.put("salary", rs.getString(2));
                row.put("age", rs.getString(3));
                list.add(row);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JDBCUtil.close(rs, ps, conn);
        }

        // 遍历List和Map
        for (Map<String, Object> row : list) {
            for (String key : row.keySet()) {
                System.out.print(key + "-->" + row.get(key) + "\t\t");
            }
            System.out.println();
        }
    }
}
