/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: StaticProxy.java
 * @time: 2019/10/30 15:29
 * @desc: 静态代理设计模式学习
 */

public class StaticProxy {
    public static void main(String[] args) {
        new WeddingCompany(new You()).happyMarry();
    }
}

interface Marry {
    void happyMarry();
}

// 真实角色
class You implements Marry {
    @Override
    public void happyMarry() {
        System.out.println("你和你的广寒仙子本月了...");
    }
}

//代理角色，婚庆公司
class WeddingCompany implements Marry {
    // 真实角色
    private Marry target;

    public WeddingCompany(Marry target) {
        this.target = target;
    }

    @Override
    public void happyMarry() {
        ready();
        this.target.happyMarry();
        after();
    }

    private void ready() {
        System.out.println("布置猪窝...");
    }

    private void after() {
        System.out.println("闹玉兔...");
    }
}