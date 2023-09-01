package com.sxt.Server_study03;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: OthersServlet.java
 * @time: 2019/12/9 13:17
 * @desc: 其他测试页面
 */

public class OthersServlet implements Servlet{
    @Override
    public void service(Request request, Response response) {
        response.print("其他测试页面...");
    }
}
