package com.sxt.planegame2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MyGameFrame.java
 * @time: 2019/11/27 10:33
 * @desc: 飞机游戏的主窗口
 */

public class GameFrame extends Frame {

    Image planeImg = GameUtil.getImage("images/plane.png");
    Image bg = GameUtil.getImage("images/bg.jpg");

    Plane plane = new Plane(planeImg, 250, 250);
    Shell[] shells = new Shell[50];

    Explode bao;
    Date startTime = new Date();
    Date endTime;
    int period;     // 游戏持续的时间

    @Override
    public void paint(Graphics g) {
        // paint是自动调用
        g.drawImage(bg, 0, 0, null);
        plane.drawSelf(g);

        // 画出所有的炮弹
        for (int i = 0; i < shells.length; i++) {
            shells[i].draw(g);
            boolean peng = shells[i].getRect().intersects(plane.getRect());

            if (peng) {
                plane.live = false;

                // 只需要生成一次爆炸效果就ok
                if (bao == null) {
                    bao = new Explode(plane.x, plane.y);
                    endTime = new Date();
                    period = (int) ((endTime.getTime() - startTime.getTime()) / 1000);
                }
                bao.draw(g);
            }

            if(!plane.live){
                g.setColor(Color.red);
                Font f = new Font("宋体", Font.BOLD, 20);
                g.setFont(f);
                g.drawString("时间：" + period + "秒", (int) plane.x, (int) plane.y);
            }
        }
    }

    // 帮助我们反复重画窗口！
    class PaintThread extends Thread {
        @Override
        public void run() {
            while (true) {
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

    // 增加键盘监听内部类
    class KeyMonitor extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            plane.addDirection(e);
        }

        @Override
        public void keyReleased(KeyEvent e) {
            plane.minusDirection(e);
        }
    }

    // 初始化窗口
    public void launchFrame() {
        this.setTitle("李英俊本俊的打飞机游戏");
        this.setVisible(true);
        this.setSize(Constant.GAME_WIDTH, Constant.GAME_HEIGHT);
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
        new PaintThread().start();          // 启动重画窗口的线程
        addKeyListener(new KeyMonitor());   // 给窗口增加键盘的监听

        // 初始化50个炮弹
        for (int i = 0; i < shells.length; i++) {
            shells[i] = new Shell();
        }
    }

    public static void main(String[] args) {
        GameFrame f = new GameFrame();
        f.launchFrame();
    }

    private Image offScreenImage = null;

    @Override
    public void update(Graphics g) {
        if (offScreenImage == null)
            offScreenImage = this.createImage(Constant.GAME_WIDTH, Constant.GAME_HEIGHT);//这是游戏窗口的宽度和高度

        Graphics gOff = offScreenImage.getGraphics();
        paint(gOff);
        g.drawImage(offScreenImage, 0, 0, null);
    }
}
