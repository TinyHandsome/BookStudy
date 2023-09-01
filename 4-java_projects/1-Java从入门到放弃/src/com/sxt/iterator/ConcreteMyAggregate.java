package com.sxt.iterator;

import java.util.ArrayList;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ConcreteMyAggregate.java
 * @time: 2020/2/14 18:45
 * @desc: 自定义的聚合类
 */

public class ConcreteMyAggregate {
    private List<Object> list = new ArrayList<Object>();

    public void addObject(Object obj) {
        this.list.add(obj);
    }

    public void removeObject(Object obj) {
        this.list.remove(obj);
    }

    public List<Object> getList() {
        return list;
    }

    public void setList(List<Object> list) {
        this.list = list;
    }

    // 获得迭代器
    public MyIterator createIterator(){
        return new ConcreteIterator();
    }

    // 使用内部类定义迭代器，可以直接使用外部类的属性
    private class ConcreteIterator implements MyIterator {
        // 定义游标用于记录遍历时的位置
        private int cursor;

        @Override
        public void first() {
            cursor = 0;
        }

        @Override
        public void next() {
            if (cursor < list.size()) {
                cursor++;
            }
        }

        @Override
        public boolean hasNext() {
            return cursor < list.size();
        }

        @Override
        public boolean ifFirst() {
            return cursor == 0;
        }

        @Override
        public boolean isLast() {
            return cursor == (list.size() - 1);
        }

        @Override
        public Object getCurrentObj() {
            return list.get(cursor);
        }
    }
}
