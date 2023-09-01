import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: WebDownloader.java
 * @time: 2019/10/28 15:54
 * @desc: 进程学习2：下载图片
 */

public class WebDownloader {
    public void download(String url, String name) {
        try {
            FileUtils.copyURLToFile(new URL(url), new File(name));
        } catch (MalformedURLException e) {
            System.out.println("不合法的路径！");
        } catch (IOException e) {
            System.out.println("下载失败！");
        }

    }
}
