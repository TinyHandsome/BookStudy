import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestCollections.java
 * @time: 2019/10/8 15:24
 * @desc: 学习Collections辅助类
 */

public class TestCollections {
    public static void main(String[] args){
        List<String> list = new ArrayList<>();
        for(int i =0; i<10; i++){
            list.add("li" + i);
        }
        System.out.println(list);

        // 随机排列list中的元素
        Collections.shuffle(list);
        System.out.println(list);
        // 逆序排列
        Collections.reverse(list);
        System.out.println(list);
        // 递增排序
        Collections.sort(list);
        System.out.println(list);
        // 二分查找
        System.out.println(Collections.binarySearch(list, "li"));
        System.out.println(Collections.binarySearch(list, "li2"));

    }
}
