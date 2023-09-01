/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LambdaTest1.java
 * @time: 2019/10/31 15:18
 * @desc: lambda推导 + 参数
 */

public class LambdaTest2 {
    public static void main(String[] args) {
        ILove love = (int a) -> {
            System.out.println("偶买噶！-->" + a);
        };
        love.lambda(100);

        // 参数类型可以省略
        ILove love2 = s -> {
            System.out.println("偶买噶！-->" + s);
        };
        love2.lambda(10);

        // 花括号也可以省略
        ILove love3 = s -> System.out.println("偶买噶！-->" + s);
        love3.lambda(1);
    }
}

interface ILove {
    void lambda(int a);
}

class Love implements ILove {
    @Override
    public void lambda(int a) {
        System.out.println("偶买噶！-->" + a);
    }
}
