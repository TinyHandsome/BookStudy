import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: pycharm
 * @file: TestList.java
 * @time: 2019/9/28 14:46
 * @desc: 测试Collection接口中的方法
 */

public class TestList {
    public static void main(String[] args){
        test03();
    }

    public static void test01(){
        Collection<String> c = new ArrayList<>();
        System.out.println(c.size());
        System.out.println(c.isEmpty());

        c.add("你大爷");
        c.add("嗯哼？");
        System.out.println(c);

        System.out.println(c.size());
        System.out.println(c.isEmpty());

        c.clear();
        System.out.println(c.size());
    }

    public static void test02(){
        List<String> list1 = new ArrayList<>();
        list1.add("aa");
        list1.add("bb");
        list1.add("cc");

        List<String> list2 = new ArrayList<>();
        list2.add("aa");
        list2.add("dd");
        list2.add("ee");

        System.out.println("list1: " + list1);
        System.out.println("list2: " + list2);

//        list1.addAll(list2);
//        list1.removeAll(list2);
        list1.retainAll(list2);

        System.out.println("list1: " + list1);

    }

    public static void test03(){
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        list.add("C");
        list.add("D");

        System.out.println(list);
        
        list.add(2, "垃圾");
        System.out.println(list);

        list.remove(2);
        System.out.println(list);

        list.set(2, "李英俊");
        System.out.println(list);

        int index1 = list.indexOf("A");
        System.out.println(index1);

        list.add("A");
        list.add("B");

        int index2 = list.lastIndexOf("A");
        System.out.println(list);
        System.out.println(index2);
    }
}
