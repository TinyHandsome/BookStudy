package com.sxt.thread;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: HappyCinema.java
 * @time: 2019/11/5 12:57
 * @desc: 快乐电影院抢座位案例
 */

public class HappyCinema {
    public static void main(String[] args) {
        Cinema c = new Cinema(2, "happy sxt");
        new Thread(new Customer(c, 2), "老高").start();
        new Thread(new Customer(c, 1), "老李").start();
    }
}

class Customer implements Runnable {
    Cinema cinema;
    int seats;

    public Customer(Cinema cinema, int seats) {
        this.cinema = cinema;
        this.seats = seats;
    }

    @Override
    public void run() {
        synchronized (cinema) {
            boolean flag = cinema.bookTickets(seats);
            if (flag) {
                System.out.println("出票成功" + Thread.currentThread().getName() + "-<位置为：" + seats);
            } else {
                System.out.println("出票失败" + Thread.currentThread().getName() + "-<位置不够！");
            }
        }
    }
}

class Cinema {
    // 可用的位置
    int available;
    // 名称
    String name;

    public Cinema(int available, String name) {
        this.available = available;
        this.name = name;
    }

    // 购票
    public boolean bookTickets(int seats) {
        System.out.println("可用位置为：" + available);
        if (seats > available) {
            return false;
        }
        available -= seats;
        return true;
    }
}
