import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: BlockedSleep1.java
 * @time: 2019/11/1 14:46
 * @desc: sleep模拟倒计时
 */

public class BlockedSleep1 {
    public static void main(String[] args) throws InterruptedException {
        // 倒计时
        Date endTime = new Date(System.currentTimeMillis() + 1000 * 10);
        long end = endTime.getTime();
        while (true) {
            System.out.println(new SimpleDateFormat("mm:ss").format(endTime));
            Thread.sleep(1000);
            endTime = new Date(endTime.getTime()-1000);
            if(end-10000 > endTime.getTime()){
                break;
            }
        }
    }

    public static void test() throws InterruptedException {
        // 倒数10个数，1秒一个
        int num = 10;
        while (true) {
            Thread.sleep(1000);
            System.out.println(num--);
        }
    }
}