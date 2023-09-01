public class testCopy {
    public static void main(String[] args) {
        String[] s1 = {"aa", "bb", "cc", "dd", "ee"};
        String[] s2 = new String[10];
        System.arraycopy(s1, 2, s2, 6, 3);

        for(int i=0; i<s2.length; i++){
            System.out.println(i+"--"+s2[i]);
        }

        System.out.println("########");
        removeElement(s1, 2);
        System.out.println("########");
        extendRange(s1);
    }

    // 删除数组中指定索引位置的元素，并将原数组返回
    private static String[] removeElement(String[] s, int index){
        System.arraycopy(s, index+1, s, index, s.length-index-1);
        s[s.length-1] = null;

        for (String m:
             s) {
            System.out.println(m);
        }
        return s;
    }

    // 数组的扩容（本质上时：先定义一个更大的数组，然后将原数组内容原封不动拷贝到新数组中）
    private static String[] extendRange(String[] s){
        String[] s2 = new String[s.length + 10];
        System.arraycopy(s, 0, s2, 0, s.length);

        for(String x: s2){
            System.out.println(x);
        }
        return s2;
    }
}
