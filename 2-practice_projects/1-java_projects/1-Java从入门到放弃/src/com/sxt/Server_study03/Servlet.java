package com.sxt.Server_study03;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Servlet.java
 * @time: 2019/12/9 12:03
 * @desc: 服务器小脚本接口
 */

public interface Servlet {
    void service(Request request, Response response);
}
