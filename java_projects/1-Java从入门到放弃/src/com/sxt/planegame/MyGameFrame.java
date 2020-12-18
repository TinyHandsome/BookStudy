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

public class MyGameFrame extends JFrame {

    Image test = GameUtil.getImage("images/plane.png");

    @Override
    public void paint(Graphics g) {
        // 自动被调用，g相当于一支画笔
        // 把别人传进来的颜色记住，最后再改回去；字体同理呀
        Color c = g.getColor();
        Font f = g.getFont();
        g.setColor(Color.BLUE);

        g.drawLine(100, 100, 300, 300);
        g.drawRect(100, 100, 300, 300);
        g.setColor(Color.green);
        g.drawOval(100, 100, 300, 300);
        g.fillRect(100, 100, 40, 40);
        g.setColor(Color.red);
        g.setFont(new Font("宋体", Font.BOLD, 50));
        g.drawString("我是李英俊！", 200, 200);

        g.drawImage(test, 250, 250, null);

        g.setColor(c);
        g.setFont(f);
    }

    // 初始化窗口
    public void launchFrame() {
        this.setTitle("李英俊本俊");
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
    }

    public static void main(String[] args) {
        MyGameFrame f = new MyGameFrame();
        f.launchFrame();
    }
}
