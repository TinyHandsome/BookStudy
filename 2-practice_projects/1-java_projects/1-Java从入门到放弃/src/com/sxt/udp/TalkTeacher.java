package com.sxt.udp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TalkTeacher.java
 * @time: 2019/11/16 20:13
 * @desc: 模拟老师端
 */

public class TalkTeacher {
    public static void main(String[] args) {
        System.out.println("老师加入聊天室...");
        new Thread(new TalkReceive(9999, "学生")).start();
        new Thread(new TalkSend(5555, "localhost", 8888)).start();
    }
}
