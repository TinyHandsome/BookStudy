package com.sxt.composite;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Client.java
 * @time: 2020/2/9 16:54
 * @desc:
 */

public class Client {
    public static void main(String[] args){
        AbstarctFile f2, f3, f5, f6;
        Folder f1 = new Folder("我的收藏");
        f2 = new ImageFile("我的头像.jpg");
        f3 = new TextFile("Hello.txt");
        f1.add(f2);
        f1.add(f3);

        Folder f4 = new Folder("电影");
        f5 = new VideoFile("神雕侠侣.avi");
        f6 = new VideoFile("笑傲江湖.avi");

        f4.add(f5);
        f4.add(f6);
        f1.add(f4);

        f1.killVirus();
    }
}
