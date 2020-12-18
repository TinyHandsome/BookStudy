import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ConvertTest1.java
 * @time: 2019/10/19 14:48
 * @desc: 转换流：InputStreamReader OutputStreamWriter
 */

public class ConvertTest1 {
    public static void main(String[] args){
        // 操作System.in和System.out
        try(BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));){
            // 循环获取键盘的输入（exit退出），输入此内容
            String msg = "";
            while(!msg.equals("exit")){
                msg = reader.readLine();        // 循环读取
                writer.write(msg);              // 循环写出
                writer.newLine();
                writer.flush();                 // 强制刷新
            }
        } catch (IOException e) {
            System.out.println("操作异常");
        }
    }
}
