package com.sxt.test.classLoader;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DecrptClassLoader.java
 * @time: 2020/2/1 23:03
 * @desc: 解密工具类：加载文件系统中加密后的class字节码的类加载器
 */

public class DecrptClassLoader extends ClassLoader {
    // com.sxt.test.bean.User --> F:/BookStudy/else/JAVAPro/src/com/sxt/test/bean/User.class
    private String rootDir;

    public DecrptClassLoader(String rootDir) {
        this.rootDir = rootDir;
    }

    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        Class<?> c = findLoadedClass(name);

        // 应该要先查询有没有加载过这个类，如果已经加载，则直接返回加载好的类，如果没有，则加载新的类。
        if (c != null) {
            return c;
        } else {
            ClassLoader parent = this.getParent();
            // 委派给父类加载
            try {
                c = parent.loadClass(name);
            } catch (Exception e) {
                System.out.println("父类加载器没有加载到这个类哦！");
            }
            if (c != null) {
                return c;
            } else {
                byte[] classData = getClassData(name);
                if (classData == null) {
                    throw new ClassNotFoundException();
                } else {
                    c = defineClass(name, classData, 0, classData.length);
                }
            }
        }
        return c;
    }

    private byte[] getClassData(String classname) {
        String path = rootDir + "/" + classname.replace('.', '/') + ".class";
        // 可以使用IOUtils将流中的数据转成字节数组，这里采用手写了
        InputStream is = null;
        ByteArrayOutputStream baos = null;
        try {
            is = new FileInputStream(path);
            baos = new ByteArrayOutputStream();
            int temp = -1;
            while ((temp = is.read()) != -1) {
                // 取反操作，进行解密
                baos.write(temp ^ 0xff);
            }
            return baos.toByteArray();
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } finally {
            try {
                if (is != null) {
                    is.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                if (baos != null) {
                    baos.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
