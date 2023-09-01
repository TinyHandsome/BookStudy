package com.sxt.composite;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Component.java
 * @time: 2020/2/9 16:39
 * @desc: 抽象组件
 */

public interface Component {
    void operation();
}

// 叶子组件
interface Leaf extends Component {

}
// 容器组件
interface Composite extends Component{
    void add(Component c);
    void remove(Component c);
    Component getChild(int index);
}
