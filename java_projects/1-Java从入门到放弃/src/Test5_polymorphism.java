/**
 * @author: Li Tian
 * @contact: 694317828@qq.com
 * @software: pycharm
 * @file: Test5_polymorphism.java
 * @time: 2019/9/7 17:33
 * @desc:
 */

public class Test5_polymorphism {
    public static void main(String[] args){
        Animal a1 = new Cat();
        a1.shout();
        Animal a2 = new Dog();
        a2.shout();
    }
}

class Animal {
    public void shout() {
        System.out.println("叫了一声！");
    }
}
class Dog extends Animal {
    public void shout() {
        System.out.println("旺旺旺！");
    }
    public void seeDoor() {
        System.out.println("看门中....");
    }
}
class Cat extends Animal {
    public void shout() {
        System.out.println("喵喵喵喵！");
    }
}
