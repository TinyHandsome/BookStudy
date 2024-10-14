package com.sxt.others;

import static org.quartz.DateBuilder.evenSecondDate;
import static org.quartz.JobBuilder.newJob;
import static org.quartz.TriggerBuilder.newTrigger;
import static org.quartz.SimpleScheduleBuilder.simpleSchedule;

import org.quartz.JobDetail;
import org.quartz.Scheduler;
import org.quartz.SchedulerFactory;
import org.quartz.Trigger;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Date;

/**
 * quartz学习入门
 */
public class QuartzTest {
    public void run() throws Exception {
        // 1. 创建Scheduler的工厂
        SchedulerFactory sf = new StdSchedulerFactory();
        // 2. 从工厂中获取调度器
        Scheduler sched = sf.getScheduler();
        // 时间
        Date runTime = evenSecondDate(new Date());
        // 3. 创建JobDetail
        JobDetail job = newJob(HelloJob.class).withIdentity("job1", "group1").build();

        // 4. 触发器
        // Trigger trigger = newTrigger().withIdentity("trigger1", "group1").startAt(runTime).build();
        // 4 | 2：如果想要循环多次呢，每5秒一次，循环三次
        Trigger trigger = newTrigger().withIdentity("trigger1", "group1").startAt(runTime)
                .withSchedule(simpleSchedule().withIntervalInSeconds(5).withRepeatCount(2)).build();
        // 5. 注册任务和触发条件
        sched.scheduleJob(job, trigger);
        // 6. 启动
        sched.start();
        try {
            // 5秒后停止
            Thread.sleep(30L * 1000L);
            // executing...
        } catch (Exception e) {
        }

        // shut down the scheduler
        sched.shutdown(true);
    }

    public static void main(String[] args) throws Exception {
        QuartzTest example = new QuartzTest();
        example.run();
    }
}
