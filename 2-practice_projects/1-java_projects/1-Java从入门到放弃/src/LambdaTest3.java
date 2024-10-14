/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LambdaTest1.java
 * @time: 2019/10/31 15:18
 * @desc: lambda推导 + 参数 + 返回值
 */

public class LambdaTest3 {
    public static void main(String[] args) {
        IInterest in = (int q, int p) -> {
            System.out.println(q + p);
            return q + p;
        };
        in.lambda(100, 50);

        // 简化版本
        IInterest in2 = (q, p) -> q + p / 2;
        System.out.println(in2.lambda(10, 20));
    }
}

interface IInterest {
    int lambda(int a, int b);
}

// 参考，下面内容可以不要
class Interest implements IInterest {
    @Override
    public int lambda(int aa, int bb) {
        System.out.println(aa + bb);
        return aa + bb;
    }
}
