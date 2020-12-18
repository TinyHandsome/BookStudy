package com.sxt.planegame2;

import java.awt.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: GameObject.java
 * @time: 2019/11/28 9:15
 * @desc:
 */

public class GameObject {
    Image img;
    double x, y;
    int speed;
    int width, height;

    public void drawSelf(Graphics g){
        g.drawImage(img, (int)x, (int)y, null);
    }

    public GameObject(Image img, double x, double y) {
        this.img = img;
        this.x = x;
        this.y = y;
    }


    public GameObject(){
    }

    public Rectangle getRect(){
        // 返回物体所在的矩形，便于后续的碰撞检测
        return new Rectangle((int)x, (int)y, width, height);
    }
}
