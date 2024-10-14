import java.io.*;
import java.net.URL;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ConvertTest2.java
 * @time: 2019/10/19 14:48
 * @desc: 转换流：InputStreamReader OutputStreamWriter
 */

public class ConvertTest2 {
    public static void main(String[] args) {
        // 中文乱码
        test1();
        // 中文不是乱码
        test2();
        // 效率更高
        test3();
    }
    public static void test1(){
        // 操作网络流，下载百度的源代码
        try(InputStream is = new URL("http://www.baidu.com").openStream();){
            int temp;
            while((temp=is.read()) != -1){
                System.out.print((char)temp);
            }
        } catch (IOException e) {
            System.out.println("操作异常");
        }
    }
    public static void test2(){
        // 操作网络流，下载百度的源代码
        try(InputStreamReader is = new InputStreamReader(new URL("http://www.baidu.com").openStream(), "UTF-8")){
            int temp;
            while((temp=is.read()) != -1){
                System.out.print((char)temp);
            }
        } catch (IOException e) {
            System.out.println("操作异常");
        }
    }
    public static void test3(){
        // 操作网络流，下载百度的源代码
        try(BufferedReader reader =
                    new BufferedReader(
                            new InputStreamReader(
                                    new URL("http://www.baidu.com").openStream(), "UTF-8"
                            )
                    );
            BufferedWriter writer =
                    new BufferedWriter(
                            new OutputStreamWriter(
                                    new FileOutputStream("baidu.html"), "UTF-8"
                            )
                    )
        ){
            String msg;
            while((msg = reader.readLine()) != null){
                writer.write(msg);      // 字符集不统一，字节数不够出现乱码
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("操作异常");
        }
    }
}
