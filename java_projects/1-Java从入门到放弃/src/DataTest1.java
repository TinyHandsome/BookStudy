import com.sun.xml.internal.messaging.saaj.util.ByteInputStream;

import java.io.*;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DataTest1.java
 * @time: 2019/10/19 15:57
 * @desc: 数据流
 */

public class DataTest1 {
    public static void main(String[] args) throws IOException {
        // 写出
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        DataOutputStream dos = new DataOutputStream(
                new BufferedOutputStream(baos)
        );
        // 操作数据类型 + 数据
        dos.writeUTF("编码辛酸泪啊");
        dos.writeInt(18);
        dos.writeBoolean(false);
        dos.writeChar('a');
        dos.flush();

        byte[] datas = baos.toByteArray();
        System.out.println(datas.length);

        // 读取
        DataInputStream dis = new DataInputStream(
                new BufferedInputStream(
                    new ByteArrayInputStream(datas)
                )
        );
        // 顺序与写出一致
        String msg = dis.readUTF();
        int age = dis.readInt();
        boolean flag = dis.readBoolean();
        char ch = dis.readChar();
        System.out.println(flag);
    }
}
