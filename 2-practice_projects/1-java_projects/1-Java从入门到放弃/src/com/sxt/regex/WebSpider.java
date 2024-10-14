package com.sxt.regex;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: WebSpider.java
 * @time: 2020/3/4 17:29
 * @desc: |网络爬虫取数据
 */

public class WebSpider {
    public static void main(String[] args) {
        String url = "http://www.163.com";
        String destStr = getURLContent(url);

        // 取到的超链接的整个内容
        // Pattern p = Pattern.compile("<a[\\s\\S]+?</a>");
        // 取到的超链接的地址
        // Pattern p = Pattern.compile("href=\"(.+?)\"");
        // 注意：上述?是非贪婪模式
        // Matcher m = p.matcher(destStr);
        // while (m.find()) {
        //     System.out.println(m.group());
        //     System.out.println("-----");
        //     System.out.println(m.group(1));
        // }

        List<String> result = getMatherSubstrs(destStr, "href=\"(http://[\\w\\s./]+?)\"");
        for (String temp : result) {
            System.out.println(temp);
        }
    }

    public static String getURLContent(String loc) {
        /*获得url对应的网页源码内容*/
        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(loc);
            BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream(), Charset.forName("gbk")));
            String temp = "";
            while ((temp = reader.readLine()) != null) {
                sb.append(temp);
            }
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    public static List<String> getMatherSubstrs(String destStr, String regexStr) {
        // 取到的超链接地址
        Pattern p = Pattern.compile(regexStr);
        Matcher m = p.matcher(destStr);
        List<String> result = new ArrayList<>();
        while (m.find()) {
            result.add(m.group(1));
        }
        return result;
    }
}
