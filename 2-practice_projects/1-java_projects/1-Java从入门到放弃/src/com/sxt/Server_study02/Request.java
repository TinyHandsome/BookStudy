package com.sxt.Server_study02;

import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Request.java
 * @time: 2019/12/5 10:15
 * @desc:
 */

public class Request {
    private String requestInfo;
    // 请求方式
    private String method;
    // 请求url
    private String url;
    // 请求参数
    private String queryStr;

    private final String BLANK = " ";
    private final String CRLF = "\r\n";

    public Request(Socket client) throws IOException {
        this(client.getInputStream());
    }

    public Request(InputStream is) {
        byte[] datas = new byte[1024 * 1024];
        int len;
        try {
            len = is.read(datas);
            this.requestInfo = new String(datas, 0, len);
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        // 分解字符串
        parseRequestInfo();
    }

    private void parseRequestInfo() {
        System.out.println("---分解---");
        System.out.println("1. 获取请求方式：开头到第一个/");
        this.method = this.requestInfo.substring(0, this.requestInfo.indexOf("/")).toLowerCase().trim();
        System.out.println("2. 获取请求url：第一个/ 到HTTP/");
        System.out.println("可能包含请求参数?前面的url");
        // 1. 获取/的位置
        int startIdx = this.requestInfo.indexOf("/") + 1;
        // 2. 获取HTTP/的位置
        int endIdx = this.requestInfo.indexOf("HTTP/");
        // 3. 分割字符串
        this.url = this.requestInfo.substring(startIdx, endIdx);
        // 4. 获取？的位置
        int queryIdx = this.url.indexOf("?");
        if (queryIdx >= 0) {
            // 表示存在请求参数
            String[] urlArray = this.url.split("\\?");
            this.url = urlArray[0].trim();
            queryStr = urlArray[1].trim();
        }
        System.out.println(this.url);

        System.out.println("3. 获取请求参数：若果Get已经获取，如果post可能在请求体中");
        if (method.equals("post")) {
            String qStr = this.requestInfo.substring(this.requestInfo.lastIndexOf(CRLF)).trim();
            if (null == queryStr) {
                queryStr = qStr;
            } else {
                queryStr += "&" + qStr;
            }
        }
        queryStr = null == queryStr?"": queryStr;
        System.out.println(method + "-->" + url + "-->" + queryStr);
    }
}
