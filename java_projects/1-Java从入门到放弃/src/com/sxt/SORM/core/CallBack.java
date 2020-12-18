package com.sxt.SORM.core;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: CallBack.java
 * @time: 2020/3/16 13:38
 * @desc: |
 */

public interface CallBack {
    public Object doExecute(Connection conn, PreparedStatement ps, ResultSet rs);

}
