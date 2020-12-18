package com.sxt.loc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SpiderTest2.java
 * @time: 2019/11/14 10:26
 * @desc: 网络爬虫，对于那些403拒绝的，模拟浏览器
 */

public class SpiderTest2 {
    public static void main(String[] args) throws IOException {
        // 获取URL
        URL url = new URL("https://www.dianping.com");
        // http协议打开
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        // 设置请求方式
        conn.setRequestMethod("GET");
        conn.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36");
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
        String msg = null;
        while (null != (msg = br.readLine())) {
            System.out.println(msg);
        }
    }
}
