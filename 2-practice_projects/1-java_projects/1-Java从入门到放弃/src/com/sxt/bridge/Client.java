package com.sxt.bridge;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/9 15:01
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        // 销售联想的笔记本电脑
        ComputerBridge c = new Laptop2(new Lenovo());
        c.sale();
        // 销售戴尔的台式机
        ComputerBridge c2 = new Desktop2(new Dell());
        c2.sale();
    }
}
