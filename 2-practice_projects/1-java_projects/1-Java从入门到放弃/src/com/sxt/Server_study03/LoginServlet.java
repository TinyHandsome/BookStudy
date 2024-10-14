package com.sxt.Server_study03;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LoginServlet.java
 * @time: 2019/12/3 15:59
 * @desc:
 */

public class LoginServlet implements Servlet {
    @Override
    public void service(Request request, Response response) {
        response.print("<html>");
        response.print("<head>");
        response.print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">");
        response.print("<title>");
        response.print("第一个servlet");
        response.print("</title>");
        response.print("</head>");
        response.print("<body>");
        response.print("欢迎回来..." + request.getParameter("uname"));
        response.print("</body>");
        response.print("</html>");
    }
}
