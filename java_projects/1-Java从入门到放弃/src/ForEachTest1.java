public class ForEachTest1 {
    public static void main(String[] args) {
        int[] a = new int[4];
        for(int i=0; i<a.length; i++){
            a[i] = i*10;
        }

        for (int m:
             a) {
            System.out.println(m);
        }
    }
}
