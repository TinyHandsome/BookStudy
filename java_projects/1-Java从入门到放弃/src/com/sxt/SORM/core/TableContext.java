package com.sxt.SORM.core;

import com.sxt.SORM.bean.ColumnInfo;
import com.sxt.SORM.bean.TableInfo;
import com.sxt.SORM.utils.JavaFileUtils;
import com.sxt.SORM.utils.StringUtils;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;


/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TableContext.java
 * @time: 2020/3/11 13:42
 * @desc: |负责获取管理数据库所有表结构和类结构的关系，并可以根据表结构生成类结结构
 */

public class TableContext {
    // 表名为key，表信息对象为value
    public static Map<String, TableInfo> tables = new HashMap<>();
    // 将po的calss对象和表信息对象关联起来，便于重用。
    public static Map<Class, TableInfo> poClassTableMap = new HashMap<>();

    private TableContext() {
    }

    static {
        try {
            // 初始化获得的表信息
            Connection conn = DBManager.getConn();
            DatabaseMetaData dbmd = conn.getMetaData();
            ResultSet tableSet = dbmd.getTables("", "%", "%", new String[]{"TABLE"});

            while (tableSet.next()) {
                // 循环每个表名
                String tableName = (String) tableSet.getObject("TABLE_NAME");
                TableInfo ti = new TableInfo(tableName, new ArrayList<ColumnInfo>(), new HashMap<String, ColumnInfo>());
                tables.put(tableName, ti);
                // 查询表中的所有字段
                ResultSet set = dbmd.getColumns("", "%", tableName, "%");
                while (set.next()) {
                    // 循环每个列名
                    ColumnInfo ci = new ColumnInfo(set.getString("COLUMN_NAME"), set.getString("TYPE_NAME"), 0);
                    ti.getColumns().put(set.getString("COLUMN_NAME"), ci);
                }

                // 查询表中的主键
                // System.out.println(tableName);
                ResultSet set2 = dbmd.getPrimaryKeys("", "%", tableName);
                while (set2.next()) {
                    ColumnInfo ci2 = (ColumnInfo) ti.getColumns().get(set2.getObject("COLUMN_NAME"));
                    // 设置为主键类型
                    ci2.setKeyType(1);
                    ti.getPriKeys().add(ci2);
                }
                if (ti.getPriKeys().size() > 0) {
                    // 取唯一主键。方便使用。如果是联合主键。则为空！
                    ti.setOnlyPriKey(ti.getPriKeys().get(0));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 更新类结构
        updateJavaPOFile();
        // 加载po包下面的所有类，便于重用，提高效率！
        loadPOTables();
    }

    /**
     * 根据表结构，更新配置的po包下面的java类
     */
    public static void updateJavaPOFile() {
        Map<String, TableInfo> map = TableContext.tables;
        for (TableInfo t : map.values()) {
            JavaFileUtils.createJavaPOFile(t, new MySqlTypeConvertor());
        }
    }

    /**
     * 加载po包下面的类
     */
    public static void loadPOTables() {
        for (TableInfo tableInfo : tables.values()) {
            try {
                Class c = Class.forName(DBManager.getConf().getPoPackage() + "." + StringUtils.firstChar2UpperCase(tableInfo.getTname()));
                poClassTableMap.put(c, tableInfo);
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Map<String, TableInfo> tables = TableContext.tables;
        System.out.println(tables);
    }

}
