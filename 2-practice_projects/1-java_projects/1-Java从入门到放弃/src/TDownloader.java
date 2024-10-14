/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: TDownloader.java
 * @time: 2019/10/28 15:58
 * @desc: 进程学习2：下载图片
 */

public class TDownloader extends Thread{
    // 远程路径
    private String url;
    // 存储名字
    private String name;

    public TDownloader(String url, String name) {
        this.url = url;
        this.name = name;
    }

    @Override
    public void run() {
        WebDownloader wd = new WebDownloader();
        wd.download(url, name);
        System.out.println(name);
    }
    
    public static void main(String[] args){
        TDownloader td1 = new TDownloader("https://img-blog.csdnimg.cn/20181107085145510.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0hhcHB5Um9ja2luZw==,size_16,color_FFFFFF,t_70", "lstm.png");
        TDownloader td2 = new TDownloader("https://img-blog.csdnimg.cn/20181107095455442.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0hhcHB5Um9ja2luZw==,size_16,color_FFFFFF,t_70", "peephole_connection.png");
        TDownloader td3 = new TDownloader("https://img-blog.csdnimg.cn/20181107101049389.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0hhcHB5Um9ja2luZw==,size_16,color_FFFFFF,t_70", "gru.png");

        // 启动三个线程
        td1.start();
        td2.start();
        td3.start();
    }
}
