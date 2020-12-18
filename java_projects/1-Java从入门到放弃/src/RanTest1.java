import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Random;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: RanTest1.java
 * @time: 2019/10/21 9:01
 * @desc: 随机读取和写入流 RandomAccessFile
 */

public class RanTest1 {
    public static void main(String[] args) throws IOException {
        // 分多少块
        File src = new File("D:\\李添的数据哦！！！\\BookStudy\\else\\JAVAPro\\src\\PrintTest2.java");
        // 总长度
        long len = src.length();
        // 每块大小
        int blockSize = 240;
        // 块数：多少块
        int size = (int)Math.ceil(len*1.0/blockSize);
        System.out.println(size);
        int beginPos = 0;
        int actualSize = (int)(blockSize>len?len:blockSize);

        for(int i=0; i<size; i++){
            beginPos = i*blockSize;
            if(i == size-1){
                // 最后一块
                actualSize = (int)len;
            }else{
                actualSize = blockSize;
                // 剩余量
                len -= actualSize;
            }
            System.out.println(i + "-->" + beginPos + "-->" + actualSize);
            test1(i, beginPos, actualSize);
        }
    }

    // 指定起始位置，读取剩余指定长度内容
    public static void test1(int i, int beginPos, int actualSize) throws IOException {
        RandomAccessFile raf = new RandomAccessFile(new File("D:\\李添的数据哦！！！\\BookStudy\\else\\JAVAPro\\src\\PrintTest2.java"), "r");
        // 指定起始位置
//        int beginPos = 2;
        // 实际大小
//        int actualSize = 128;
        // 随机读取
        raf.seek(beginPos);
        byte[] flush = new byte[124];
        // 接受长度
        int len = -1;
        while((len = raf.read(flush)) != -1){
            if (actualSize > len){
                // 实际大小大于接受长度，则获取本次读取的所有内容
                System.out.println(new String(flush, 0, len));
                actualSize -= len;
            }else{
                System.out.println(new String(flush, 0, actualSize));
                break;
            }
        }

        raf.close();
    }
}
