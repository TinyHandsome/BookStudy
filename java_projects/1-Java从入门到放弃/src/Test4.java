import java.util.Objects;

/**
 * @author: Li Tian
 * @contact: 694317828@qq.com
 * @software: pycharm
 * @file: Test4.java
 * @time: 2019/8/26 21:14
 * @desc:
 */

public class Test4 {
    public static void main(String[] args){

        User u1 = new User(1000, "小高", "123456");
        User u2 = new User(1000, "小高高", "123456");

        System.out.println(u1==u2);
        System.out.println(u1.equals(u2));
        System.out.println(u1.hashCode());
    }
}

class User{
    int id;
    String name;
    String pwd;

    public User(int id, String name, String pwd) {
        super();
        this.id = id;
        this.name = name;
        this.pwd = pwd;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id ;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, pwd);
    }
}