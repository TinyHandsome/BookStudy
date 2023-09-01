package com.sxt.regex;

import java.util.Arrays;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @desc: | 测试正则表达对象分割字符串的操作
 */

public class Demo04 {
    public static void main(String[] args) {
        String str = "asdfsa12asd233dsd11";

        // 切割
        String[] arrs = str.split("\\d+");
        System.out.println(Arrays.toString(arrs));
    }
}
