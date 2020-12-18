package com.sxt.SORM.pool;

import com.sxt.SORM.core.DBManager;

import java.sql.Connection;
import java.util.ArrayList;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DBConnPool.java
 * @time: 2020/3/17 14:03
 * @desc: |连接池的类
 */

public class DBConnPool {
    // 最大连接数
    private static final int POOL_MAX_SIZE = DBManager.getConf().getPoolMaxSize();
    // 最小连接数
    private static final int POOL_MIN_SIZE = DBManager.getConf().getPoolMinSize();
    // 连接池对象
    private List<Connection> pool;

    public DBConnPool() {
        initPool();
    }

    /**
     * 初始化连接池，使池中的连接数达到最小值
     */
    public void initPool() {
        if (pool == null) {
            pool = new ArrayList<Connection>();
        }

        while (pool.size() < DBConnPool.POOL_MIN_SIZE) {
            pool.add(DBManager.createConn());
            System.out.println("初始化池，池中连接数：" + pool.size());
        }
    }

    /**
     * 从连接池中取出一个连接
     */
    public synchronized Connection getConnection() {
        int last_index = pool.size() - 1;
        // 获得一个连接
        Connection conn = pool.get(last_index);
        pool.remove(last_index);
        return conn;
    }

    /**
     * 将连接放回池中
     *
     * @param conn
     */
    public synchronized void close(Connection conn) {
        if (pool.size() >= POOL_MAX_SIZE) {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            pool.add(conn);
        }
    }
}
