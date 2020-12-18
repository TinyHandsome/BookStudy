package com.sxt.planegame2;

import java.awt.*;
import java.awt.event.KeyEvent;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Plane.java
 * @time: 2019/11/28 9:27
 * @desc:
 */

public class Plane extends GameObject {
    boolean left, up, right, down;
    boolean live = true;

    public Plane(Image img, double x, double y) {
        super(img, x, y);
        speed = 10;
        width = img.getWidth(null);
        height = img.getHeight(null);
    }

    @Override
    public void drawSelf(Graphics g) {
        if(live){
            g.drawImage(img, (int) x, (int) y, null);

            if (left) {
                x -= speed;
            }
            if (right) {
                x += speed;
            }
            if (up) {
                y -= speed;
            }
            if (down) {
                y += speed;
            }
        }else{
        }
    }

    // 按下某个键增加相应的方向
    public void addDirection(KeyEvent e) {
        switch (e.getKeyCode()) {
            case KeyEvent.VK_LEFT:
                left = true;
                break;
            case KeyEvent.VK_UP:
                up = true;
                break;
            case KeyEvent.VK_RIGHT:
                right = true;
                break;
            case KeyEvent.VK_DOWN:
                down = true;
                break;
        }
    }

    // 抬起某个键取消相应的方向
    public void minusDirection(KeyEvent e) {
        switch (e.getKeyCode()) {
            case KeyEvent.VK_LEFT:
                left = false;
                break;
            case KeyEvent.VK_UP:
                up = false;
                break;
            case KeyEvent.VK_RIGHT:
                right = false;
                break;
            case KeyEvent.VK_DOWN:
                down = false;
                break;
        }
    }
}
