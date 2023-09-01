import java.io.File;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DirCount.java
 * @time: 2019/10/15 15:58
 * @desc: 使用面向对象：统计文件夹大小
 */

public class DirCount {
    // 大小
    private long len;
    // 文件夹路径
    private String path;
    // 源
    private File src;
    // 文件的个数
    private int fileSize;
    // 文件夹的个数
    private int dirSize;

    public DirCount(String path){
        this.path = path;
        this.src = new File(path);
        count(this.src);
    }

    private void count(File src){
        // 获取大小
        if(null != src && src.exists()){
            if(src.isFile()){
                this.len += src.length();
                this.fileSize++;
            }else{
                this.dirSize++;
                for(File s: src.listFiles()){
                    count(s);
                }
            }
        }
    }

    public long getLen() {
        return len;
    }

    public int getFileSize() {
        return fileSize;
    }

    public int getDirSize() {
        return dirSize;
    }

    public static void main(String[] args){
        DirCount dir = new DirCount("F:\\BookStudy");
        System.out.println(dir.getLen());
        System.out.println("文件的数量" + "--->" + dir.getFileSize());
        System.out.println("文件夹的数量" + "--->" + dir.getDirSize());


        DirCount dir2 = new DirCount("F:\\BookStudy\\else");
        System.out.println(dir2.getLen());
        System.out.println("文件的数量" + "--->" + dir2.getFileSize());
        System.out.println("文件夹的数量" + "--->" + dir2.getDirSize());

    }
}
