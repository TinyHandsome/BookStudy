import sun.java2d.loops.TransformHelper;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: BlockedJoin1.java
 * @time: 2019/11/1 15:05
 * @desc: 爸爸和儿子买烟的故事
 */

public class BlockedJoin1 {
    public static void main(String[] args){
        new Father().start();
    }
}

class Father extends Thread{
    @Override
    public void run() {
        System.out.println("想抽烟，发现没了");
        System.out.println("让儿子去买中华");
        Thread t = new Son();
        t.start();
        try {
            t.join();       // father被阻塞
            System.out.println("老爸接过烟，把零钱给了儿子");
        } catch (InterruptedException e) {
            e.printStackTrace();
            System.out.println("孩子走丢了，老爸出去找孩子去了...");
        }
    }
}

class Son extends Thread{
    @Override
    public void run() {
        System.out.println("接过老爸的钱出去了...");
        System.out.println("路边有个游戏厅，玩了10秒");
        for (int i = 0; i < 10; i++) {
            System.out.println(i+"秒过去了...");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("赶紧买烟去...");
        System.out.println("手拿一包中华回家了...");
    }
}

