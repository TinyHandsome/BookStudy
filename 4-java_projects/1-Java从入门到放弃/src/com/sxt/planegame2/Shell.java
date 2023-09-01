package com.sxt.planegame2;

import java.awt.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Shell.java
 * @time: 2019/11/28 10:08
 * @desc: 炮弹类
 */

public class Shell extends GameObject {
    double degree;

    public Shell() {
        x = 200;
        y = 200;
        width = 7;
        height = 7;
        speed = 3;

        degree = Math.random() * Math.PI * 2;
    }

    public void draw(Graphics g) {
        Color c = g.getColor();
        g.setColor(Color.yellow);

        g.fillOval((int) x, (int) y, width, height);

        // 炮弹沿着任意角度去飞
        x += speed * Math.cos(degree);
        y += speed * Math.sin(degree);

        // 炮弹遇到墙壁之后反弹
        if (x < 0 || x > Constant.GAME_WIDTH - width) {
            degree = Math.PI - degree;
        }

        if (y < 30 || y > Constant.GAME_HEIGHT - height) {
            degree = -degree;
        }

        g.setColor(c);
    }
}
