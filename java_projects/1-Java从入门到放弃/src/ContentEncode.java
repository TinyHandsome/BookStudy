import java.io.UnsupportedEncodingException;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: ContentEncode.java
 * @time: 2019/10/15 16:26
 * @desc: 编码：字符串-->字节；解码：字节-->字符串
 */

public class ContentEncode {
    public static void main(String[] args) throws UnsupportedEncodingException {
        String msg = "你怕不是个铁憨憨";
        // 编码：字节数组
        byte[] datas = msg.getBytes();
        System.out.println(datas);
        // 中文utf-8：一个字符占3个字节；默认使用工程的字符集
        System.out.println(datas.length);

        // 编码：其他字符集
        datas = msg.getBytes("UTF-16LE");
        System.out.println(datas.length);
        datas = msg.getBytes("GBK");
        System.out.println(datas.length);

        // 解码
        msg = new String(datas, 0, datas.length, "gbk");
        System.out.println(msg);
    }
}
