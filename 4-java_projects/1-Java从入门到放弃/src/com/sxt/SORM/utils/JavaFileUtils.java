package com.sxt.SORM.utils;

import com.sxt.SORM.bean.ColumnInfo;
import com.sxt.SORM.bean.JavaFieldGetSet;
import com.sxt.SORM.bean.TableInfo;
import com.sxt.SORM.core.DBManager;
import com.sxt.SORM.core.MySqlTypeConvertor;
import com.sxt.SORM.core.TableContext;
import com.sxt.SORM.core.TypeConvertor;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: JavaFileUtils.java
 * @time: 2020/3/11 13:44
 * @desc: | 封装了生成java文件（源代码）常用操作
 */

public class JavaFileUtils {
    /**
     * 根据字段信息生成java属性信息。如varchar username --> private String username;以及相应的set和get方法源码
     *
     * @param column    字段信息
     * @param convertor 类型转化器
     * @return java属性和set/get方法源码
     */
    public static JavaFieldGetSet createFieldGetSetSRC(ColumnInfo column, TypeConvertor convertor) {
        JavaFieldGetSet jfgs = new JavaFieldGetSet();
        String javaFieldType = convertor.databaseType2JavaType(column.getDataType());
        jfgs.setFieldInfo("\tprivate " + javaFieldType + " " + column.getName() + ";\n");

        // public String getUsername(){return username;}
        StringBuilder getSrc = new StringBuilder();
        getSrc.append("\tpublic " + javaFieldType + " get" + StringUtils.firstChar2UpperCase(column.getName()) + "(){\n");
        getSrc.append("\t\treturn " + column.getName() + ";\n");
        getSrc.append("\t}\n");
        jfgs.setGetInfo(getSrc.toString());

        // public void setUsername(String username){this.username = username;}
        StringBuilder setSrc = new StringBuilder();
        setSrc.append("\tpublic void set" + StringUtils.firstChar2UpperCase(column.getName()) + "(");
        setSrc.append(javaFieldType + " " + column.getName() + "){\n");
        setSrc.append("\t\tthis." + column.getName() + " = " + column.getName() + ";\n");
        setSrc.append("\t}\n");
        jfgs.setSetInfo(setSrc.toString());

        return jfgs;
    }

    /**
     * 根据表信息生成java类的源代码
     *
     * @param tableInfo 表信息
     * @param convertor 数据类型转化器
     * @return java类的源代码
     */
    public static String createJavaSrc(TableInfo tableInfo, TypeConvertor convertor) {
        Map<String, ColumnInfo> columns = tableInfo.getColumns();
        List<JavaFieldGetSet> javaFields = new ArrayList<>();

        for (ColumnInfo c : columns.values()) {
            javaFields.add(createFieldGetSetSRC(c, convertor));
        }
        StringBuilder src = new StringBuilder();

        // 生成package语句
        src.append("package " + DBManager.getConf().getPoPackage() + ";\n\n");
        // 生成import语句
        src.append("import java.sql.*;\n");
        src.append("import java.util.*;\n\n");
        // 生成类声明语句
        src.append("public class " + StringUtils.firstChar2UpperCase(tableInfo.getTname()) + " {\n\n");
        // 生成属性列表
        for (JavaFieldGetSet f : javaFields) {
            src.append(f.getFieldInfo());
        }
        src.append("\n\n");
        // 生成set方法列表
        for (JavaFieldGetSet f : javaFields) {
            src.append(f.getSetInfo());
        }
        // 生成get方法列表
        for (JavaFieldGetSet f : javaFields) {
            src.append(f.getGetInfo());
        }
        // 生成类结束
        src.append("}\n");
        // System.out.println(src);
        return src.toString();
    }

    public static void createJavaPOFile(TableInfo tableInfo, TypeConvertor convertor) {
        String src = createJavaSrc(tableInfo, convertor);
        String srcPath = DBManager.getConf().getSrcPath() + "\\";
        String packagePath = DBManager.getConf().getPoPackage().replaceAll("\\.", "/");
        // 修正poPackage路径，因为没有重新创建项目
        String[] packagePath_list = packagePath.split("/");
        packagePath = packagePath_list[packagePath_list.length - 1];

        File f = new File(srcPath + packagePath);
        // System.out.println(f.getAbsolutePath());

        if (!f.exists()) {
            // 指定目录不存在则帮助用户建立该目录
            f.mkdirs();
        }

        BufferedWriter bw = null;
        try {
            bw = new BufferedWriter(new FileWriter(f.getAbsolutePath() + "/" + StringUtils.firstChar2UpperCase(tableInfo.getTname()) + ".java"));
            bw.write(src);
            System.out.println("建立表" + tableInfo.getTname() + "对应的java类");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (bw != null) {
                    bw.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    public static void main(String[] args) {
        // 测试每一个表的field，set、get方法源码生成
        // ColumnInfo ci = new ColumnInfo("username", "int", 0);
        // JavaFieldGetSet f = createFieldGetSetSRC(ci, new MySqlTypeConvertor());
        // System.out.println(f);
        // System.out.println("\n--------------------" + "分割线" + "--------------------\n");

        // 测试每一个表的从头到尾完全源码生成
        // Map<String, TableInfo> map = TableContext.tables;
        // TableInfo t = map.get("emp");
        // createJavaSrc(t, new MySqlTypeConvertor());

        Map<String, TableInfo> map = TableContext.tables;
        // TableInfo t = map.get("emp");
        for(TableInfo t: map.values()) {
            createJavaPOFile(t, new MySqlTypeConvertor());
        }
    }
}
