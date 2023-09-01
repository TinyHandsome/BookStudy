import java.util.HashSet;
import java.util.Set;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestSet.java
 * @time: 2019/10/8 14:32
 * @desc: 测试Set
 */

public class TestSet {
    public static void main(String[] args){
        Set<String> s = new HashSet<>();
        s.add("aa");
        s.add("bb");
        s.add("aa");
        System.out.println(s);
        s.remove("bb");
        System.out.println(s);
    }
}
