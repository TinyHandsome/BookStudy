package com.sxt.Server_study03;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: RegisterServlet.java
 * @time: 2019/12/3 15:59
 * @desc:
 */

public class RegisterServlet implements Servlet{
    @Override
    public void service(Request request, Response response){
        response.print("注册成功...");
    }
}
