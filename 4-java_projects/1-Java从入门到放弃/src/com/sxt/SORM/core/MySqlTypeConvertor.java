package com.sxt.SORM.core;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MySqlTypeConvertor.java
 * @time: 2020/3/11 18:16
 * @desc: |mysql数据类型和java数据类型的转换
 */

public class MySqlTypeConvertor implements TypeConvertor {
    @Override
    public String databaseType2JavaType(String columnType) {
        // varchar --> String
        if ("varchar".equalsIgnoreCase(columnType) || "char".equalsIgnoreCase(columnType)) {
            return "String";
        } else if ("int".equalsIgnoreCase(columnType)
                || "tinyint".equalsIgnoreCase(columnType)
                || "smallint".equalsIgnoreCase(columnType)
                || "integer".equalsIgnoreCase(columnType)) {
            return "Integer";
        } else if ("bigint".equalsIgnoreCase(columnType)) {
            return "long";
        } else if ("double".equalsIgnoreCase(columnType) || "float".equalsIgnoreCase(columnType)) {
            return "Double";
        } else if ("clob".equalsIgnoreCase(columnType)) {
            return "java.sql.Clob";
        } else if ("blob".equalsIgnoreCase(columnType)) {
            return "java.sql.Blob";
        }else if("date".equalsIgnoreCase(columnType)){
            return "java.sql.Date";
        }else if("time".equalsIgnoreCase(columnType)){
            return "java.sql.Time";
        }else if("timestamp".equalsIgnoreCase(columnType)){
            return "java.sql.Timestamp";
        }
        return null;
    }

    @Override
    public String javaType2DatabaseType(String javaDataType) {
        return null;
    }
}
