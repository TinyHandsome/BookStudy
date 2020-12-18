import java.util.Arrays;

public class TestBubbleSort {
    public static void main(String[] args) {
        int[] values = {3, 1, 6, 2, 9, 0, 7, 4, 5, 8};
        bubble(values);
        bubble_improve(values);
    }

    public static void bubble(int[] values){
        /*冒泡排序*/
        int temp = 0;

        // 遍历前n-1个数
        for (int i = 0; i < values.length-1; i++) {
            // 每次循环都把最大值放到后面，所以后面的就不必在比较了
            for (int j = 0; j < values.length-1-i; j++) {
                // 如果前一个值大于后一个值，则交换位置
                if(values[j]>values[j+1]){
                    temp = values[j];
                    values[j] = values[j+1];
                    values[j+1] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(values));
    }

    public static void bubble_improve(int[] values){
        /* 改良冒泡排序 */
        /* 也就是当一次外循环没有发生交换的时候，那么停止 */
        int temp = 0;

        // 遍历前n-1个数
        for (int i = 0; i < values.length-1; i++) {
            // 每次循环都把最大值放到后面，所以后面的就不必在比较了
            boolean flag = true;
            for (int j = 0; j < values.length-1-i; j++) {
                // 如果前一个值大于后一个值，则交换位置
                if(values[j]>values[j+1]){
                    temp = values[j];
                    values[j] = values[j+1];
                    values[j+1] = temp;

                    flag = false;
                }
            }

            if(flag){
                break;
            }
        }
        System.out.println(Arrays.toString(values));
    }
}
