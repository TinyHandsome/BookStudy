package com.sxt.udp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TalkReceive.java
 * @time: 2019/11/16 20:11
 * @desc: 封装接收器
 */

public class TalkReceive implements Runnable {
    private DatagramSocket server;
    private String from;

    public TalkReceive(int port, String from) {
        this.from = from;
        try {
            server = new DatagramSocket(port);
        } catch (SocketException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        while (true) {
            //  2. 准备容器，封装成DatagramPacket包裹
            byte[] container = new byte[1024 * 60];
            DatagramPacket packet = new DatagramPacket(container, 0, container.length);
            //  3. 阻塞式接受包裹receeive(DatagramPacket p)
            //  阻塞式
            try {
                server.receive(packet);
            } catch (IOException e) {
                e.printStackTrace();
            }
            //  4. 分析数据，byte[] getData，getLength()
            byte[] datas = packet.getData();
            int len = packet.getLength();
            String data = new String(datas, 0, len);
            System.out.println(from + "说：" + data);
            if (data.equals("q")) {
                break;
            }
        }
        //  5. 释放资源
        server.close();
    }
}

