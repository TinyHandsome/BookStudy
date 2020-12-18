/**
 * @author: Li Tian
 * @contact: 694317828@qq.com
 * @software: pycharm
 * @file: Test1.java
 * @time: 2019/8/20 17:32
 * @desc:
 */

public class Test1 {
    public static void main(String[] args){
        int a = 3;
        int b = 4;
        System.out.println(a&b);
        System.out.println(a|b);
        System.out.println(a^b);
        System.out.println(~a);

        // 移位
        int c = 3<<2;
        System.out.println(c);
        System.out.println(12>>1);
    }
}
