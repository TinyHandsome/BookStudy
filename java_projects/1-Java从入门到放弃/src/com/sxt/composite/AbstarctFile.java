package com.sxt.composite;

import java.util.ArrayList;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: AbstarctFile.java
 * @time: 2020/2/9 16:46
 * @desc: 抽象构建
 */

public interface AbstarctFile {
    void killVirus();
}

class ImageFile implements AbstarctFile{
    private String name;

    public ImageFile(String name) {
        this.name = name;
    }

    @Override
    public void killVirus() {
        System.out.println("---图像文件：" + name + "，进行查杀！");
    }
}

class TextFile implements AbstarctFile{
    private String name;

    public TextFile(String name) {
        this.name = name;
    }

    @Override
    public void killVirus() {
        System.out.println("---文本文件：" + name + "，进行查杀！");
    }
}

class VideoFile implements AbstarctFile{
    private String name;

    public VideoFile(String name) {
        this.name = name;
    }

    @Override
    public void killVirus() {
        System.out.println("---视频文件：" + name + "，进行查杀！");
    }
}

class Folder implements AbstarctFile{
    private String name;
    // 定义容器，用来存放本容器构建下的子节点
    private List<AbstarctFile> list = new ArrayList<>();

    public Folder(String name) {
        this.name = name;
    }

    public void add(AbstarctFile file){
        list.add(file);
    }

    public void remove(AbstarctFile file){
        list.remove(file);
    }

    public AbstarctFile getChild(int index){
        return list.get(index);
    }

    @Override
    public void killVirus() {
        System.out.println("---文件夹：" + name + "，进行查杀！");
        for (AbstarctFile file: list){
            file.killVirus();
        }
    }
}