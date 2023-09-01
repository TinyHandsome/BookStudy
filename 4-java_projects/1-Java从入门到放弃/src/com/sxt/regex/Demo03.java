package com.sxt.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试正则表达对象替换操作
 */

public class Demo03 {
    public static void main(String[] args) {
        // 在这个字符串：asdfsadf2323，是否符合制定的正则表达式：\w+
        Pattern p = Pattern.compile("[0-9]");
        // 创建Matcher对象
        Matcher m = p.matcher("asdfsa12**asd233**dsd11");

        // 替换
        String newStr = m.replaceAll("#");
        System.out.println(newStr);
    }
}
