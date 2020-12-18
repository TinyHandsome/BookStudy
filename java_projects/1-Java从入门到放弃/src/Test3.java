/**
 * @author: Li Tian
 * @contact: 694317828@qq.com
 * @software: pycharm
 * @file: Test3.java
 * @time: 2019/8/20 17:48
 * @desc:
 */

public class Test3 {
    public static void main(String[] args){
        int score = 80;
        String type = score<60? "不及格":"及格";
        System.out.println(type);

        double x = Math.random();
        System.out.println(x);
        System.out.println((int)(6*x + 1));


        outer: for (int i = 101; i < 150; i++) {
            for (int j = 2; j < i / 2; j++) {
                if (i % j == 0){
                    continue outer;
                }
            }
            System.out.print(i + "  ");
        }
    }
}
