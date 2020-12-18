package com.sxt.Server_study03;

import com.sxt.Server_study01.servlet.WebContext;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: WebApp.java
 * @time: 2019/12/9 12:37
 * @desc: 解析代码
 */

public class WebApp {
    private static WebContext context;

    static {
        try {
            // SAX解析
            // 1. 获取解析工厂
            SAXParserFactory factory = SAXParserFactory.newInstance();
            // 2. 从解析工厂获取解析器
            SAXParser parse = null;
            parse = factory.newSAXParser();
            // 3. 加载文档Document注册处理器
            // 4. 编写处理器
            WebHandler handler = new WebHandler();
            parse.parse(Thread.currentThread().getContextClassLoader().getResourceAsStream("web.xml"), handler);
            // 5. 获取数据
            context = new WebContext(handler.getEntitys(), handler.getMappings());

        } catch (Exception e) {
            System.out.println("解析配置文件错误！");
        }
    }

    // 通过url获取配置文件对应的servlet
    public static Servlet getServletFromUrl(String url) {
        // 假设你输入了 /login or /g or /reg
        String className = context.getClz("/" + url);
        if (className == null){
            return null;
        }
        Class clz = null;
        try {
            clz = Class.forName(className);
            Servlet servlet = (Servlet) clz.getConstructor().newInstance();
            return servlet;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
