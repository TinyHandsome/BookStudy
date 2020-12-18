package com.sxt.SORM.test;

import com.sxt.SORM.core.Query;
import com.sxt.SORM.core.QueryFactory;
import com.sxt.SORM.vo.EmpVO;

import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Test2.java
 * @time: 2020/3/17 16:40
 * @desc: |测试连接池的调用效率
 */

public class Test2 {
    public static void test1(){
        Query q = QueryFactory.createQuery();
        String sql2 = "select e.id,e.empname,salary+bonus 'xinshui',age,d.dname 'deptName',d.address 'deptAddr' from emp e"
                + " " + "join dept d on e.deptId=d.id;";
        List<EmpVO> list2 = q.queryRows(sql2, EmpVO.class, null);
        for (EmpVO e : list2) {
            System.out.println(e.getEmpname() + "-" + e.getDeptAddr() + "-" + e.getXinshui());
        }
    }

    public static void main(String[] args){
        long a = System.currentTimeMillis();
        for (int i = 0; i < 3000; i++) {
            test1();
        }
        long b = System.currentTimeMillis();
        // 不加连接池的耗时：13077ms，增加连接池之后，耗时为2478
        System.out.println(b-a);
    }
}
