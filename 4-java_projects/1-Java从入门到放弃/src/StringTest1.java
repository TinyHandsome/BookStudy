/**
 * @author: Li Tian
 * @contact: 694317828@qq.com
 * @software: pycharm
 * @file: StringTest1.java
 * @time: 2019/9/9 18:48
 * @desc:
 */

public class StringTest1 {
    public static void main(String[] args){
        String s1 = "core Java";
        String s2 = "Core java";

        System.out.println(s1.charAt(3));
        System.out.println(s2.length());
        System.out.println(s1.equals(s2));
        System.out.println(s1.equalsIgnoreCase(s2));
        System.out.println(s1.indexOf("Java"));
        System.out.println(s2.indexOf("apple"));

        String s = s1.replace(" ", "&");
        System.out.println(s);

    }
}
