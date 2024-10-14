package com.sxt.udp;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestTalk.java
 * @time: 2019/11/16 20:25
 * @desc: 自己端口测试
 */

public class TestTalk {
    public static void main(String[] args) {
        System.out.println("李英俊加入聊天室...");
        new Thread(new TalkReceive(9999, "李不羁")).start();
        new Thread(new TalkSend(5555,
                "192.168.1.104", 8888)).start();
    }
}
