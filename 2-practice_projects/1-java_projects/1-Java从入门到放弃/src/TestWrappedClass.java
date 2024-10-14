/**
 * @author: Li Tian
 * @contact: 694317828@qq.com
 * @software: pycharm
 * @file: TestWrappedClass.java
 * @time: 2019/9/13 19:42
 * @desc: 包装类Integer类的使用，其他包装类的用法类似。
 */

public class TestWrappedClass {
    public static void main(String[] args) {
        // 基本数据类型转成包装类对象
        Integer a = new Integer(3);
        Integer b = Integer.valueOf(30);

        // 包装类对象转成基本数据类型
        int c = b.intValue();
        double d = b.doubleValue();

        // 把字符串转换成包装类对象
        Integer e = new Integer("999");
        Integer f = Integer.parseInt("999");

        // 把包装类对象转换成字符串
        String str = f.toString();

        // 常见的常量
        System.out.println("int类型最大的证书：" + Integer.MAX_VALUE);

    }
}
