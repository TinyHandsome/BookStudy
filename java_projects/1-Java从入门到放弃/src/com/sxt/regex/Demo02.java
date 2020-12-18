package com.sxt.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试正则表达式分组的处理
 */

public class Demo02 {
    public static void main(String[] args) {
        // 在这个字符串：asdfsadf2323，是否符合制定的正则表达式：\w+
        Pattern p = Pattern.compile("([a-z]+)([0-9]+)");
        // 创建Matcher对象
        Matcher m = p.matcher("asdfsa12**asd233**dsd11");
        // 尝试将整个字符序列与该模式匹配
        while (m.find()) {
            // group()和group(0)都是匹配整个表达式的子字符串
            System.out.println("start---");
            System.out.println("满足整个表达式的子字符串：");
            System.out.println(m.group());
            System.out.println("满足第1个括号中表达式的字符串：");
            System.out.println(m.group(1));
            System.out.println("满足第2个括号中表达式的字符串：");
            System.out.println(m.group(2));
        }
    }
}
