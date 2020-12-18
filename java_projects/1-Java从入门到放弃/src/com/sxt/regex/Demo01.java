package com.sxt.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2020/3/3 14:10
 * @desc: |
 */

public class Demo01 {
    public static void main(String[] args){
        // 在这个字符串：asdfsadf2323，是否符合制定的正则表达式：\w+
        Pattern p = Pattern.compile("\\w+");
        // 创建Matcher对象
        Matcher m = p.matcher("asdfsadf@@2323");
        // 尝试将整个字符序列与该模式匹配
        // boolean yo = m.matches();
        // 该方法扫描输入的序列，查找与该模式匹配的下一个子序列
        while(m.find()){
            // group()和group(0)都是匹配整个表达式的子字符串
            System.out.println(m.group());
            System.out.println(m.group(0));
        }
    }
}
