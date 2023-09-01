package com.sxt.test.classLoader;

import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: EncrpUtil.java
 * @time: 2020/2/1 22:52
 * @desc: 加密工具类
 */

public class EncrpUtil {
    public static void main(String[] args) {
        encrpt("F:/Java WorkSpace/NewClass.class", "F:/Java WorkSpace/temp/NewClass.class");
    }

    public static void encrpt(String src, String dest) {
        FileInputStream fis = null;
        FileOutputStream fos = null;

        try {
            fis = new FileInputStream(src);
            fos = new FileOutputStream(dest);

            int temp = -1;
            while ((temp = fis.read()) != -1) {
                // 取反操作
                fos.write(temp ^ 0xff);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fis != null) {
                    fis.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        try {
            if (fos != null) {
                fos.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

