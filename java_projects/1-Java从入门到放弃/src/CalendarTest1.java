/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: pycharm
 * @file: CalendarTest1.java
 * @time: 2019/9/22 10:53
 * @desc: 可视化日历编写
 */

import java.text.ParseException;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;


public class CalendarTest1 {
    public static void main(String[] args) throws ParseException{
        System.out.println("请输入日期（格式为：2010-3-3）：");
        Scanner scanner = new Scanner(System.in);
        String dateString = scanner.nextLine();

        // 将输入的字符串转化为日期类
        System.out.println("您刚刚输入的日期是：" + dateString);
        String[] str = dateString.split("-");
        int year = Integer.parseInt(str[0]);
        int month = new Integer(str[1]);
        int day = new Integer(str[2]);
        Calendar c = new GregorianCalendar(year, month-1, day);

        // 设置该月的第一天，获得这一天是周几
        c.set(Calendar.DATE, 1);

        int dow = c.get(Calendar.DAY_OF_WEEK);
        System.out.println("日\t一\t二\t三\t四\t五\t六");

        // 知道是周几后，那前面就用\t填充
        for(int i=0; i<dow-1; i++){
            System.out.print("\t");
        }

        int maxDate = c.getActualMaximum(Calendar.DATE);
        for (int i = 1; i <= maxDate; i++) {
            StringBuilder sBuilder = new StringBuilder();
            if(c.get(Calendar.DATE) == day){
                sBuilder.append(c.get(Calendar.DATE) + "*\t");
            }else{
                sBuilder.append(c.get(Calendar.DATE) + "\t");
            }
            System.out.print(sBuilder);
            if (c.get(Calendar.DAY_OF_WEEK) == Calendar.SATURDAY){
                System.out.print("\n");
            }
            c.add(Calendar.DATE, 1);

        }
    }
}
