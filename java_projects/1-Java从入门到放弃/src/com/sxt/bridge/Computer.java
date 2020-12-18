package com.sxt.bridge;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Computer.java
 * @time: 2020/2/9 14:44
 * @desc:
 */

public interface Computer {
    void sale();
}

class Desktop implements Computer{

    @Override
    public void sale() {
        System.out.println("销售台式机！");
    }
}

class Laptop implements Computer{

    @Override
    public void sale() {
        System.out.println("销售笔记本！");
    }
}

class Pad implements Computer{

    @Override
    public void sale() {
        System.out.println("销售平板电脑！");
    }
}

class LenovoDesktop extends Desktop{
    @Override
    public void sale() {
        System.out.println("销售联想台式机！");;
    }
}

class LenovoLaptop extends Laptop{
    @Override
    public void sale() {
        System.out.println("销售联想笔记本！");;
    }
}

class LenovoPad extends Pad{
    @Override
    public void sale() {
        System.out.println("销售联想平板电脑！");;
    }
}

class ShenzhouDesktop extends Desktop{
    @Override
    public void sale() {
        System.out.println("销售神舟台式机！");;
    }
}

class ShenzhouLaptop extends Laptop{
    @Override
    public void sale() {
        System.out.println("销售神舟笔记本！");;
    }
}

class ShenzhouPad extends Pad{
    @Override
    public void sale() {
        System.out.println("销售神舟平板电脑！");;
    }
}

class DellDesktop extends Desktop{
    @Override
    public void sale() {
        System.out.println("销售戴尔台式机！");;
    }
}

class DellLaptop extends Laptop{
    @Override
    public void sale() {
        System.out.println("销售戴尔笔记本！");;
    }
}

class DellPad extends Pad{
    @Override
    public void sale() {
        System.out.println("销售戴尔平板电脑！");;
    }
}