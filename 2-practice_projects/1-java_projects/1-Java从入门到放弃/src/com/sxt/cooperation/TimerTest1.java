package com.sxt.cooperation;

import com.sun.deploy.cache.CacheEntry;
import com.sun.deploy.security.MozillaMyKeyStore;

import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Timer;
import java.util.TimerTask;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TimerTest1.java
 * @time: 2019/11/9 18:27
 * @desc: 定时调度
 */

public class TimerTest1 {
    public static void main(String[] args) {
        Timer timer = new Timer();
        // 执行安排
        // 执行一次
        timer.schedule(new MyTask(), 1000);
        // 执行多次
        timer.schedule(new MyTask(), 1000, 200);
        // 指定时间执行
        Calendar cal = new GregorianCalendar(2099, 11, 3, 11, 22, 22);
        timer.schedule(new MyTask(), cal.getTime(), 200);
    }
}

class MyTask extends TimerTask {
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("放空大脑休息一会儿~");
        }
    }
}
