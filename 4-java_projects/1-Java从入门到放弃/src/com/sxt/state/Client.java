package com.sxt.state;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/29 18:17
 * @desc: |
 */

public class Client {
    public static void main(String[] args) {
        HomeContext ctx = new HomeContext(new FreeState());
        ctx.setState(new BookedState());
        ctx.setState(new CheckedState());
    }
}
