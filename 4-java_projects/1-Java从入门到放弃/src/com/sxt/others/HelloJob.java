package com.sxt.others;

import java.util.Date;

import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

/**
 * Quartz学习
 */
public class HelloJob implements Job {
    public HelloJob() {
    }

    public void execute(JobExecutionContext context)
            throws JobExecutionException {
        System.out.println("----------start----------");
        System.out.println("Hello world-" + new Date());
        System.out.println("----------end----------");
    }

}
