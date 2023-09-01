/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Racer.java
 * @time: 2019/10/30 14:55
 * @desc: 共享资源：模拟龟兔赛跑
 */

public class Racer implements Runnable {
    private String winner;       // 胜利者

    @Override
    public void run() {
        for (int steps = 1; steps <= 100; steps++) {
            // 模拟休息
            if(Thread.currentThread().getName().equals("rabit") && steps % 10 == 0){
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println(Thread.currentThread().getName() + "-->" + steps);
            // 比赛是否结束
            boolean flag = gameOver(steps);
            if (flag) {
                break;
            }
        }
    }

    private boolean gameOver(int steps) {
        if (winner != null) {
            // 存在胜利者
            return true;
        } else {
            if (steps == 100) {
                winner = Thread.currentThread().getName();
                System.out.println("winner==>" + winner);
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Racer racer = new Racer();
        new Thread(racer, "tortoise").start();
        new Thread(racer, "rabbit").start();
    }
}
