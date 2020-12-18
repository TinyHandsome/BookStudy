import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO06.java
 * @time: 2019/10/17 16:39
 * @desc: 理解操作步骤 标准
 */

public class TestIO06 {
    public static void main(String[] args){
        // 1. 创建源
        File src = new File("abc.txt");
        // 2. 选择流
        InputStream is = null;
        try{
            is = new FileInputStream(src);
            // 3. 操作（读取）
            int temp;
            while((temp=is.read()) != -1){
                System.out.println((char)temp);
            }
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }finally{
            // 4. 释放资源
            if (null != is) {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
