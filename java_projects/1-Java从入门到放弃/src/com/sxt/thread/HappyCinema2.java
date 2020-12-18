package com.sxt.thread;

import java.util.ArrayList;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: HappyCinema.java
 * @time: 2019/11/5 12:57
 * @desc: 快乐电影院抢座位案例
 */

public class HappyCinema2 {
    public static void main(String[] args) {
        // 可用位置
        List<Integer> available = new ArrayList<>();
        for (int i = 1; i < 8; i++) {
            available.add(i);
        }

        // 顾客需要的位置
        List<Integer> seats1 = new ArrayList<>();
        seats1.add(1);
        seats1.add(2);
        List<Integer> seats2 = new ArrayList<>();
        seats2.add(4);
        seats2.add(5);
        seats2.add(6);

        SxtCinema c = new SxtCinema(available, "happy sxt");
        new Thread(new HappyCustomer(c, seats1), "老高").start();
        new Thread(new HappyCustomer(c, seats2), "老李").start();
    }
}

class HappyCustomer implements Runnable {
    SxtCinema cinema;
    List<Integer> seats;

    public HappyCustomer(SxtCinema cinema, List<Integer> seats) {
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

class SxtCinema {
    // 可用的位置
    List<Integer> available;
    // 名称
    String name;

    public SxtCinema(List<Integer> available, String name) {
        this.available = available;
        this.name = name;
    }

    // 购票
    public boolean bookTickets(List<Integer> seats) {
        System.out.println("可用位置为：" + available);
        List<Integer> copy = new ArrayList<>();
        copy.addAll(available);

        // 相减
        copy.removeAll(seats);
        // 判断大小
        if (available.size() - copy.size() != seats.size()) {
            return false;
        }
        // 成功
        available = copy;

        return true;
    }
}
