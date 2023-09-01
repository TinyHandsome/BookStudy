import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TestIO07.java
 * @time: 2019/10/17 16:39
 * @desc: 文件字符输入流 加入缓冲流
 */

public class BufferedTest03 {
    public static void main(String[] args){
        // 1. 创建源
        File src = new File("abc.txt");
        // 2. 选择流
        BufferedReader reader = null;
        try{
            reader = new BufferedReader(new FileReader(src));
            // 3. 操作（读取）
            String line = null;
            while((line = reader.readLine()) != null){
                System.out.println(line);
            }
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }finally{
            // 4. 释放资源
            if (null != reader) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
