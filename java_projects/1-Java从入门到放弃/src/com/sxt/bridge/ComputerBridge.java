package com.sxt.bridge;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ComputerBridge.java
 * @time: 2020/2/9 14:58
 * @desc: 电脑类型的维度
 */

public class ComputerBridge {
    protected Brand brand;

    public ComputerBridge(Brand brand) {
        this.brand = brand;
    }

    public void sale(){
        brand.sale();
    }
}

class Desktop2 extends ComputerBridge{

    public Desktop2(Brand brand) {
        super(brand);
    }

    @Override
    public void sale() {
        super.sale();
        System.out.println("销售台式机！");
    }
}

class Laptop2 extends ComputerBridge{

    public Laptop2(Brand brand) {
        super(brand);
    }

    @Override
    public void sale() {
        super.sale();
        System.out.println("销售笔记本电脑！");
    }
}