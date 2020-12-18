import java.util.Arrays;

public class TestBinarySearch {
    public static void main(String[] args) {
        int[] arr = {30, 20, 50 ,10, 80, 9, 7, 12, 100, 40, 8};
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
        System.out.println(myBinarySearch(arr, 400));
    }

    public static int myBinarySearch(int[] arr, int value){
        /* 二分法查找 */
        int low = 0;
        int high = arr.length - 1;

        while (low <= high){
            int mid = (low + high)/2;

            if (value == arr[mid]){
                return mid;
            }

            if (value > arr[mid]){
                low = mid + 1;
            }

            if (value < arr[mid]){
                high = mid - 1;
            }
            System.out.println(low + "+" + high);

        }
        return -1;
    }
}
