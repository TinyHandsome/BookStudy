package com.sxt.SORM.core;

import com.sxt.SORM.po.Emp;
import com.sxt.SORM.vo.EmpVO;

import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: MysqlQuery.java
 * @time: 2020/3/13 16:54
 * @desc: |负责针对mysql数据库的查询
 */

public class MysqlQuery extends Query {

    public static void main(String[] args) {
        Object obj = new MysqlQuery().queryValue("select count(*) from emp where salary>?", new Object[]{1000});
        System.out.println(obj);
    }

    /**
     * 复杂多行查询测试
     */
    public static void testQueryRows() {
        List<Emp> list = new MysqlQuery().queryRows("select id,empname,age from emp where age>? and salary<?", Emp.class,
                new Object[]{1, 9000});
        for (Emp e : list) {
            System.out.println(e.getEmpname());
        }

        String sql2 = "select e.id,e.empname,salary+bonus 'xinshui',age,d.dname 'deptName',d.address 'deptAddr' from emp e"
                + " " + "join dept d on e.deptId=d.id;";
        List<EmpVO> list2 = new MysqlQuery().queryRows(sql2, EmpVO.class, null);
        for (EmpVO e : list2) {
            System.out.println(e.getEmpname() + "-" + e.getDeptAddr() + "-" + e.getXinshui());
        }
    }

    /**
     * 增删改操作测试
     */
    public static void testDML() {
        Emp e = new Emp();
        e.setEmpname("Tom");
        e.setBirthday(new java.sql.Date(System.currentTimeMillis()));
        e.setAge(30);
        e.setSalary(8888.0);
        e.setId(1);

        // new MysqlQuery().delete(e);
        // new MysqlQuery().insert(e);
        new MysqlQuery().update(e, new String[]{"empname", "age", "salary"});
    }

    @Override
    public Object queryPagenate(int pageNum, int size) {
        return null;
    }
}
