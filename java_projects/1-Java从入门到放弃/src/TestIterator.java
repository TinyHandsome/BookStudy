import java.util.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIterator.java
 * @time: 2019/10/8 14:57
 * @desc: 迭代器学习
 */

public class TestIterator {
    public static void main(String[] args){
        testIteratorList();
        testIteratorSet();
        testIteratorMap1();
        testIteratorMap2();
    }

    // 遍历List
    public static void testIteratorList(){
        List<String> list = new ArrayList<>();
        list.add("aa");
        list.add("bb");
        list.add("cc");

        for(Iterator<String> iter=list.iterator(); iter.hasNext();){
            String temp = iter.next();
            System.out.println(temp);
        }
    }

    // 遍历Set
    public static void testIteratorSet(){
        Set<String> set = new HashSet<>();
        set.add("aa");
        set.add("bb");
        set.add("cc");

        for(Iterator<String> iter=set.iterator(); iter.hasNext();){
            String temp = iter.next();
            System.out.println(temp);
        }
    }

    // 遍历Map：方法1
    public static void testIteratorMap1(){
        Map<Integer, String> map = new HashMap<>();
        map.put(100, "aa");
        map.put(200, "bb");
        map.put(300, "cc");

        Set<Map.Entry<Integer, String>> ss = map.entrySet();
        for(Iterator<Map.Entry<Integer, String>> iter = ss.iterator(); iter.hasNext();){
            Map.Entry<Integer, String> temp = iter.next();
            System.out.println(temp.getKey() + "--" + temp.getValue());
        }
    }

    // 遍历Map：方法2
    public static void testIteratorMap2(){
        Map<Integer, String> map = new HashMap<>();
        map.put(100, "aa");
        map.put(200, "bb");
        map.put(300, "cc");

        Set<Integer> keySet = map.keySet();

        for(Iterator<Integer> iter = keySet.iterator(); iter.hasNext();){
            Integer key = iter.next();
            System.out.println(key + "--" + map.get(key));
        }
    }
}
