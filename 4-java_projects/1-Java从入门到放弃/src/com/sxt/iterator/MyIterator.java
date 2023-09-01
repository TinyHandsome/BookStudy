package com.sxt.iterator;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MyIterator.java
 * @time: 2020/2/14 18:42
 * @desc: 自定义的迭代器接口
 */

public interface MyIterator {
    // 将游标指向第一个元素
    void first();
    // 将游标指向下一个元素
    void next();
    // 判断是否存在下一个元素
    boolean hasNext();

    boolean ifFirst();
    boolean isLast();

    // 获取当前游标指向的对象
    Object getCurrentObj();
}
