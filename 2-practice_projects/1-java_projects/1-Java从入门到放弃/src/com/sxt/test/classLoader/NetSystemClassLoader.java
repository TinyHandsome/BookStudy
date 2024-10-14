package com.sxt.test.classLoader;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: FileSystemClassLoader.java
 * @time: 2020/1/31 20:58
 * @desc: 自定义网路类加载器
 */

public class NetSystemClassLoader extends ClassLoader {
    // com.sxt.test.bean.User --> www.sxt.cn/JAVAPro/src/com/sxt/test/bean/User.class
    private String rootUrl;

    public NetSystemClassLoader(String rootDir) {
        this.rootUrl = rootDir;
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
            }catch (Exception e){
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
        String path = rootUrl + "/" + classname.replace('.', '/') + ".class";
        // 可以使用IOUtils将流中的数据转成字节数组，这里采用手写了
        InputStream is = null;
        ByteArrayOutputStream baos = null;
        try {
            URL url = new URL(path);
            is = url.openStream();
            baos = new ByteArrayOutputStream();
            byte[] buffer = new byte[1024];
            int temp = 0;
            while ((temp = is.read(buffer)) != -1) {
                baos.write(buffer, 0, temp);
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
            }catch(IOException e){
                e.printStackTrace();
            }
            try {
                if (baos != null) {
                    baos.close();
                }
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}
