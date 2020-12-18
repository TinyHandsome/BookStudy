package com.sxt.test.testDynamicCompile;

import javax.tools.JavaCompiler;
import javax.tools.ToolProvider;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: Demo1.java
 * @time: 2020/1/9 14:38
 * @desc: 动态编译
 */

public class Demo1 {
    public static void main(String[] args) throws IOException {

        // 如果是给的字符串的话，可以
        // 通过IO流操作，将字符串存储成一个临时文件，然后调用动态编译方法！
        // 如果是文件的话，就按下面的方法
        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        int result = compiler.run(null, null, null, "D:\\java_test\\HelloWorld.java");
        System.out.println(result == 0 ? "编译成功" : "编译失败");

        // 上面只是进行了编译，下面还要进行动态运行编译好的类
        // 通过Runtime调用执行类
        Runtime run = Runtime.getRuntime();
        Process process = run.exec("java -cp D:\\java_test HelloWorld");
        InputStream in = process.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(in));
        String info = "";
        while ((info = reader.readLine()) != null) {
            System.out.println(info);
        }

        // 通过反射调用执行类
        try {
            URL[] urls = new URL[]{new URL("file:/" + "D:\\java_test\\")};
            URLClassLoader loader = new URLClassLoader(urls);
            Class c = loader.loadClass("HelloWorld");
            // 调用加载类的main方法
            Method m = c.getMethod("main", String[].class);
            // 如果这里不用Object强制转型的话，invoke后面传入的就不是一个String
            // 的字符串数组，而是两个字符串，认为是两个参数，于是就会发生参数个数不匹配的问题
            m.invoke(null, (Object) new String[]{});

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
