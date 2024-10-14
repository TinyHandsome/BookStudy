package com.sxt.SORM.bean;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ColumnInfo.java
 * @time: 2020/3/11 13:46
 * @desc: |封装表中一个字段的信息
 */

public class ColumnInfo {
    // 字段名称
    private String name;
    // 字段数据类型
    private String dataType;
    // 字段的键类型(0普通键；1主键；2外键)
    private int keyType;

    public ColumnInfo() {
    }

    public ColumnInfo(String name, String dataType, int keyType) {
        this.name = name;
        this.dataType = dataType;
        this.keyType = keyType;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDataType() {
        return dataType;
    }

    public void setDataType(String dataType) {
        this.dataType = dataType;
    }

    public int getKeyType() {
        return keyType;
    }

    public void setKeyType(int keyType) {
        this.keyType = keyType;
    }
}
