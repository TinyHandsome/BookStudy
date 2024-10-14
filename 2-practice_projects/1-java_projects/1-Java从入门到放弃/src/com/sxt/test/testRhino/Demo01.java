package com.sxt.test.testRhino;

import javax.script.Invocable;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import java.io.FileReader;
import java.net.URL;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo01.java
 * @time: 2020/1/13 15:58
 * @desc: 测试脚本引擎执行JavaScript代码
 */

public class Demo01 {
    public static void main(String[] args) throws Exception {
        // 获得脚本引擎的对象
        ScriptEngineManager sem = new ScriptEngineManager();
        ScriptEngine engine = sem.getEngineByName("javascript");

        // 定义变量，存储到引擎上下文中
        engine.put("msg", "liyingjun is g good man!");
        String str = "var user = {name: 'litian', age: 18, schools: ['清华大学', '北京尚学堂']};";
        str += "print(user.name);";

        // 执行脚本
        engine.eval(str);
        engine.eval("msg = 'sxt is a good school!'");
        System.out.println(engine.get("msg"));
        System.out.println("########################");

        // 定义函数
        engine.eval("function add(a, b){var sum = a + b; return sum;}");
        // 取得调用接口
        Invocable jsInvoke = (Invocable) engine;
        // 执行脚本中定义的方法
        Object result1 = jsInvoke.invokeFunction("add", new Object[]{13, 20});
        System.out.println(result1);

        // 导入其他java包，使用其他包中的java类
        String jsCode = "var list=java.util.Arrays.asList([\"北京尚学堂\", \"清华大学\", \"中国石油大学\"]);";
        engine.eval(jsCode);

        List<String> list2 = (List<String>) engine.get("list");
        for (String temp : list2) {
            System.out.println(temp);
        }

        // 执行一个js文件
        URL url = Demo01.class.getClassLoader().getResource("com/sxt/test/testRhino/test.js");
        FileReader fr = new FileReader(url.getPath());
        engine.eval(fr);
        fr.close();
    }
}
