package com.sxt.SORM.test;

import com.sxt.SORM.core.MysqlQuery;
import com.sxt.SORM.core.Query;
import com.sxt.SORM.core.QueryFactory;
import com.sxt.SORM.vo.EmpVO;

import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Test.java
 * @time: 2020/3/17 12:55
 * @desc: |客户端调用测试类
 */

public class Test {
    public static void main(String[] args){
        Query q = QueryFactory.createQuery();
        String sql2 = "select e.id,e.empname,salary+bonus 'xinshui',age,d.dname 'deptName',d.address 'deptAddr' from emp e"
                + " " + "join dept d on e.deptId=d.id;";
        List<EmpVO> list2 = q.queryRows(sql2, EmpVO.class, null);
        for (EmpVO e : list2) {
            System.out.println(e.getEmpname() + "-" + e.getDeptAddr() + "-" + e.getXinshui());
        }
    }
}
