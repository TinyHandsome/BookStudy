package com.sxt.SORM.bean;

import java.util.List;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TableInfo.java
 * @time: 2020/3/11 13:56
 * @desc: |存储表结构信息
 */

public class TableInfo {
    // 表名
    private String tname;
    // 所有字段的信息
    private Map<String, ColumnInfo> columns;
    // 唯一主键(目前只能处理表中有且只有一个的情况)
    private ColumnInfo onlyPriKey;
    // 如果联合主键，则在这里存储
    private List<ColumnInfo> priKeys;

    public TableInfo() {
    }

    public TableInfo(String tname, List<ColumnInfo> priKeys, Map<String, ColumnInfo> columns) {
        this.tname = tname;
        this.columns = columns;
        this.priKeys = priKeys;
    }

    public String getTname() {
        return tname;
    }

    public void setTname(String tname) {
        this.tname = tname;
    }

    public Map<String, ColumnInfo> getColumns() {
        return columns;
    }

    public void setColumns(Map<String, ColumnInfo> columns) {
        this.columns = columns;
    }

    public ColumnInfo getOnlyPriKey() {
        return onlyPriKey;
    }

    public void setOnlyPriKey(ColumnInfo onlyPriKey) {
        this.onlyPriKey = onlyPriKey;
    }

    public List<ColumnInfo> getPriKeys() {
        return priKeys;
    }

    public void setPriKeys(List<ColumnInfo> priKeys) {
        this.priKeys = priKeys;
    }
}
