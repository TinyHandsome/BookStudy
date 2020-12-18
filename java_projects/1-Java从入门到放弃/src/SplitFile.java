import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: SplitFile.java
 * @time: 2019/10/21 9:35
 * @desc: 对RanTest进行封装，功能是拆分文件，面向对象思想封装
 */

public class SplitFile {
    // 源头
    private File src;
    // 目的地（文件夹）
    private String destDir;
    // 所有分割后的文件存储路径
    private List<String> destPaths;
    // 每块大小
    private int blockSize;
    // 块数：多少块
    private int size;

    public SplitFile(String srcPath, String destDir, int blockSize){
        this.src = new File(srcPath);
        this.destDir = destDir;
        this.blockSize = blockSize;
        this.destPaths = new ArrayList<>();

        // 初始化
        init();
    }

    // 初始化
    private void init(){
        // 总长度
        long len = this.src.length();
        // 块数：多少块
        this.size = (int)Math.ceil(len*1.0/blockSize);
        // 路径
        for(int i=0; i<size; i++){
            this.destPaths.add(this.destDir + "/" + i + "-" + this.src.getName());
        }

    }

    // 分割
    public void split() throws IOException {
        /*
        1. 计算每一块起始位置及大小
        2. 分割
         */
        // 总长度
        long len = this.src.length();
        // 每块大小
        int size = (int)Math.ceil(len*1.0/blockSize);
        System.out.println(size);
        int beginPos = 0;
        int actualSize = (int)(this.blockSize>len?len:this.blockSize);

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
            splitDetail(i, beginPos, actualSize);
        }
    }

    // 指定起始位置，读取剩余指定长度内容
    private void splitDetail(int i, int beginPos, int actualSize) throws IOException {
        RandomAccessFile raf = new RandomAccessFile((this.src), "r");
        RandomAccessFile raf2 = new RandomAccessFile((this.destPaths.get(i)), "rw");
        raf.seek(beginPos);
        byte[] flush = new byte[124];
        // 接受长度
        int len = -1;
        while((len = raf.read(flush)) != -1){
            if (actualSize > len){
                // 实际大小大于接受长度，则获取本次读取的所有内容
                raf2.write(flush, 0, len);
                actualSize -= len;
            }else{
                raf2.write(flush, 0, actualSize);
                break;
            }
        }
        raf2.close();
        raf.close();
    }

    // 文件的合并
    private void merge(String destPath) throws IOException {
        // 输出流
        OutputStream os = new BufferedOutputStream(
                new FileOutputStream(destPath, true)
        );
        // 输入流
        for (int i = 0; i < destPaths.size(); i++) {
            InputStream is = new BufferedInputStream((new FileInputStream(destPaths.get(i))));
            // 拷贝
            byte[] flush = new byte[1024];
            int len = -1;
            while((len = is.read(flush)) != -1){
                os.write(flush, 0, len);
            }
            os.flush();
            is.close();
        }
        os.close();
    }

    // 利用合并流来进行文件的合并
    private void seq_merge(String destPath) throws IOException {
        // 输出流
        OutputStream os = new BufferedOutputStream(
                new FileOutputStream(destPath, true)
        );
        Vector<InputStream> vi = new Vector<InputStream>();
        SequenceInputStream sis = null;
        // 输入流
        for (int i = 0; i < destPaths.size(); i++) {
            InputStream is = new BufferedInputStream((new FileInputStream(destPaths.get(i))));
        }
        sis = new SequenceInputStream(vi.elements());

        // 拷贝
        byte[] flush = new byte[1024];
        int len = -1;
        while((len = sis.read(flush)) != -1){
            os.write(flush, 0, len);
        }
        os.flush();
        sis.close();
        os.close();
    }

    public static void main(String[] args) throws IOException {
        SplitFile sf = new SplitFile("test.png", "dest", 1024*10);
        sf.split();
        sf.seq_merge("merge-seq.png");
    }
}
