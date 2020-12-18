/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DecorateTest02.java
 * @time: 2019/10/18 15:53
 * @desc: 模拟咖啡
 */

public class DecorateTest02 {
    public static void main(String[] args){
        Drink coffee = new Coffee();
        Drink suger = new Suger(coffee);    // 装饰
        System.out.println(suger.info() + "-->" + suger.cost());
        Drink milk = new Milk(coffee);    // 装饰
        System.out.println(milk.info() + "-->" + milk.cost());

        Drink mixed = new Milk(suger);    // 装饰
        System.out.println(mixed.info() + "-->" + mixed.cost());
    }
}

// 抽象组件
interface Drink{
    double cost();      // 费用
    String info();      // 说明
}

// 具体组件
class Coffee implements Drink{
    private String name = "原味咖啡";

    @Override
    public double cost() {
        return 10;
    }

    @Override
    public String info() {
        return name;
    }
}

// 抽象装饰类
abstract class Decorate implements Drink{
    // 对抽象组件的引用
    private Drink drink;
    public Decorate(Drink drink){
        this.drink = drink;
    }

    @Override
    public double cost() {
        return this.drink.cost();
    }

    @Override
    public String info() {
        return this.drink.info();
    }
}

// 具体装饰类
class Milk extends Decorate{
    public Milk(Drink drink) {
        super(drink);
    }

    @Override
    public double cost() {
        return super.cost()*4;
    }

    @Override
    public String info() {
        return super.info() + "加入了牛奶";
    }
}

class Suger extends Decorate{
    public Suger(Drink drink) {
        super(drink);
    }

    @Override
    public double cost() {
        return super.cost()*2;
    }

    @Override
    public String info() {
        return super.info() + "加入了糖";
    }
}