/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: LambdaTest1.java
 * @time: 2019/10/31 15:18
 * @desc: lambda推导
 */

public class LambdaTest1 {
    static class Like2 implements ILike {
        public void lambda() {
            System.out.println("2. 我喜欢你大爷！");
        }
    }

    public static void main(String[] args) {
        class Like3 implements ILike {
            public void lambda() {
                System.out.println("3. 我喜欢你大爷！");
            }
        }

        // 外部类
        ILike like = new Like();
        like.lambda();
        // 静态内部类
        like = new Like2();
        like.lambda();
        // 方法内部类
        like = new Like3();
        like.lambda();

        // 匿名类
        like = new ILike() {
            @Override
            public void lambda() {
                System.out.println("4. 我喜欢你大爷！");
            }
        };
        like.lambda();

        // lambda
        like = () -> {
            System.out.println("5. 我喜欢你大爷！");
        };
        like.lambda();
    }
}

interface ILike {
    void lambda();
}

class Like implements ILike {
    @Override
    public void lambda() {
        System.out.println("1. 我喜欢你大爷！");
    }
}
