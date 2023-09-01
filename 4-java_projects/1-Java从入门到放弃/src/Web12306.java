/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Web12306.java
 * @time: 2019/10/30 12:36
 * @desc: 共享资源：模拟买票
 */

public class Web12306 implements Runnable {
    // 票数
    private int ticketNums = 99;

    @Override
    public void run() {
        while(true){
            if(ticketNums<0){
                break;
            }
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "-->" + ticketNums--);
        }
    }

    public static void main(String[] args){
        // 一份资源
        Web12306 web = new Web12306();
        // 多个代理
        new Thread(web, "张三").start();
        new Thread(web, "李四").start();
        new Thread(web, "王五").start();
    }

}
