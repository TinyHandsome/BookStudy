import java.io.*;
import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DataTest2.java
 * @time: 2019/10/19 15:57
 * @desc: 对象流
 */

public class ObjectTest2 {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // 写出：序列化
        ObjectOutputStream oos = new ObjectOutputStream(
                new BufferedOutputStream(
                        new FileOutputStream("obj.txt")
                )
        );
        // 操作数据类型 + 数据
        oos.writeUTF("编码辛酸泪");
        oos.writeInt(18);
        oos.writeBoolean(false);
        oos.writeChar('a');
        // 对象
        oos.writeObject("谁解其中味");
        oos.writeObject(new Date());
        Employee emp = new Employee("马云", 400);
        oos.writeObject(emp);
        oos.flush();
        oos.close();

        // 读取：反序列化
        ObjectInputStream ois = new ObjectInputStream(
                new BufferedInputStream(
                    new FileInputStream("obj.txt")
                )
        );
        // 顺序与写出一致
        String msg = ois.readUTF();
        int age = ois.readInt();
        boolean flag = ois.readBoolean();
        char ch = ois.readChar();
        System.out.println(flag);
        // 对象的数据还原
        Object str = ois.readObject();
        Object date = ois.readObject();
        Object employee = ois.readObject();

        if (str instanceof String){
            String strObj = (String) str;
            System.out.println(strObj);
        }
        if (date instanceof Date){
            Date strObj = (Date) date;
            System.out.println(strObj);
        }
        if (employee instanceof Employee){
            Employee strObj = (Employee) employee;
            System.out.println(strObj.getName() + "-->" + strObj.getSalary());
        }
    }
}
