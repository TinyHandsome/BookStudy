package com.sxt.planegame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MyGameFrame.java
 * @time: 2019/11/27 10:33
 * @desc: 飞机游戏的主窗口
 */

public class GameFrame extends JFrame {

    Image plane = GameUtil.getImage("images/plane.png");
    Image bg = GameUtil.getImage("images/bg.jpg");

    int planeX = 250;
    int planeY = 250;

    @Override
    public void paint(Graphics g) {
        // paint是自动调用
        g.drawImage(bg, 0, 0, null);
        g.drawImage(plane, planeX, planeY, null);
        planeX++;
    }

    // 帮助我们反复重画窗口！
    class PaintThread extends Thread {
        @Override
        public void run() {
            while (true) {
                System.out.println("窗口画一次！");
                // 重画
                repaint();
                try {
                    Thread.sleep(40);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    // 初始化窗口
    public void launchFrame() {
        this.setTitle("李英俊本俊的打飞机游戏");
        this.setVisible(true);
        this.setSize(500, 500);
        this.setLocation(300, 300);

        // 点x就关闭程序了
        this.addWindowListener(
                new WindowAdapter() {
                    @Override
                    public void windowClosing(WindowEvent e) {
                        System.exit(0);
                    }
                }
        );
        // 启动重画窗口的线程
        new PaintThread().start();
    }

    public static void main(String[] args) {
        GameFrame f = new GameFrame();
        f.launchFrame();
    }
}
