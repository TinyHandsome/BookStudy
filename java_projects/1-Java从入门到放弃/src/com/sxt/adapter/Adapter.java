package com.sxt.adapter;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Adapter.java
 * @time: 2020/2/7 11:03
 * @desc: 【类适配器方式】适配器，相当于把键盘转换成usb接口的转接器
 */

public class Adapter extends Adaptee implements Target{
    // 我的理解：把适配器变成键盘（子类），并实现USB接口-->打字

    @Override
    public void handleReq() {
        super.request();
    }
}
