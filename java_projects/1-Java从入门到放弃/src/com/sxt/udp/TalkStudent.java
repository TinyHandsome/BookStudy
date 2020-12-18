package com.sxt.udp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TalkStudent.java
 * @time: 2019/11/16 20:13
 * @desc: 模拟学生端
 */

public class TalkStudent {
    public static void main(String[] args) {
        System.out.println("学生加入聊天室...");
        new Thread(new TalkSend(7777, "localhost", 9999)).start();
        new Thread(new TalkReceive(8888, "老师")).start();
    }
}
