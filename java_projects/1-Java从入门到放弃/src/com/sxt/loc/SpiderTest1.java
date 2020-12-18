package com.sxt.loc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SpiderTest1.java
 * @time: 2019/11/14 10:20
 * @desc: 网络爬虫
 */

public class SpiderTest1 {
    public static void main(String[] args) throws IOException {
        // 获取URL
        URL url = new URL("https://www.jd.com");
        // 下载资源
        InputStream is = url.openStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
        String msg = null;
        while(null != (msg=br.readLine())){
            System.out.println(msg);
        }
    }
}
