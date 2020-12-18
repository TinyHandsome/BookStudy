package com.sxt.chat3;

import java.io.Closeable;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SxtUtils.java
 * @time: 2019/11/25 13:40
 * @desc: 工具类：释放资源
 */

public class SxtUtils {
    public static void close(Closeable... targets){
        for (Closeable target: targets){
            try{
                if(null != target){
                    target.close();
                }
            }catch (Exception e){
                e.printStackTrace();
            }
        }
    }
}
