package com.sxt.flyweight;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/10 12:47
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        ChessFlyWeight chess1 = ChessFlyWeightFactory.getChess("black");
        ChessFlyWeight chess2 = ChessFlyWeightFactory.getChess("black");
        System.out.println(chess1);
        System.out.println(chess2);

        // 增加外部状态的处理
        chess1.display(new Coordinate(10, 10));
        chess1.display(new Coordinate(20, 20));
    }
}
