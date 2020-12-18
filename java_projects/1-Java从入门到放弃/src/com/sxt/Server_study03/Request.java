package com.sxt.Server_study03;

import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.net.Socket;
import java.util.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Request2.java
 * @time: 2019/12/5 10:15
 * @desc: 封装请求协议：封装请求参数为Map
 */

public class Request {
    private String requestInfo;
    // 请求方式
    private String method;
    // 请求url
    private String url;
    // 请求参数
    private String queryStr;
    // 存储参数
    private Map<String, List<String>> parameterMap;

    private final String BLANK = " ";
    private final String CRLF = "\r\n";

    public Request(Socket client) throws IOException {
        this(client.getInputStream());
    }

    public String getMethod() {
        return method;
    }

    public String getUrl() {
        return url;
    }

    public String getQueryStr() {
        return queryStr;
    }

    public Request(InputStream is) {
        parameterMap = new HashMap<>();
        byte[] datas = new byte[1024 * 1024 * 1024];
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
//        System.out.println("---分解---");
//        System.out.println("1. 获取请求方式：开头到第一个/");
        this.method = this.requestInfo.substring(0, this.requestInfo.indexOf("/")).toLowerCase().trim();
//        System.out.println("2. 获取请求url：第一个/ 到HTTP/");
//        System.out.println("可能包含请求参数?前面的url");
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

//        System.out.println("3. 获取请求参数：若果Get已经获取，如果post可能在请求体中");
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
        // 转成Map    fav=1&fav=2&uname=shsxt&age=18&other=
        convertMap();
    }

    // 处理请求参数为Map
    private void convertMap(){
        // 分割字符串 &
        String[] keyValues = this.queryStr.split("&");
        for(String queryStr: keyValues){
            // 再次分割字符串 =
            String[] kv = queryStr.split("=");
            // 保持两个长度 key 和 value
            kv = Arrays.copyOf(kv, 2);
            // 获取key 和 value
            String key = kv[0];
            String value = kv[1]==null? null: decode(kv[1], "utf-8");
            // 存储在Map中
            if(!parameterMap.containsKey(key)){
                // 容器里面没有，第一次
                parameterMap.put(key, new ArrayList<String>());
            }
            parameterMap.get(key).add(value);
        }
    }

    // 处理中文
    private String decode(String value, String enc){
        try {
            return java.net.URLDecoder.decode(value, enc);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return null;
        }
    }

    // 通过name获取对应的多个值
    public String[] getParameterValues(String key){
        List<String> values = this.parameterMap.get(key);
        if(null == values || values.size()<1){
            return null;
        }
        return values.toArray(new String[0]);
    }

    // 通过name获取对应的一个值
    public String getParameter(String key){
        String[] values = getParameterValues(key);
        return values == null?null: values[0];
    }
}
