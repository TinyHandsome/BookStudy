package com.sxt.mediator;

import java.util.HashMap;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: President.java
 * @time: 2020/2/14 19:14
 * @desc:
 */

public class President implements Mediator {
    private Map<String, Department> map = new HashMap<String, Department>();

    @Override
    public void regitster(String dname, Department d) {
        map.put(dname, d);
    }

    @Override
    public void command(String dname) {
        map.get(dname).selfAction();
    }
}
