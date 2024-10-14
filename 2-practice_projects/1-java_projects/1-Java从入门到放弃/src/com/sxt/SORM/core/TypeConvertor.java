package com.sxt.SORM.core;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TypeConvertor.java
 * @time: 2020/3/11 13:39
 * @desc: |负责java数据类型和数据库数据类型的互相转换
 */

public interface TypeConvertor {
    /**
     * 将数据库数据类型转化成java的数据类型
     * @param columnType 数据库字段的数据类型
     * @return java的数据类型
     */
    public String databaseType2JavaType(String columnType);

    /**
     * 将java数据类型转化为数据库数据类型
     * @param javaDataType java数据类型
     * @return 数据库数据类型
     */
    public String javaType2DatabaseType(String javaDataType);
}
