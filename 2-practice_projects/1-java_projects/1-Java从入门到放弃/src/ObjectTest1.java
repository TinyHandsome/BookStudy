import java.io.*;
import java.util.Date;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: DataTest1.java
 * @time: 2019/10/19 15:57
 * @desc: 对象流
 */

public class ObjectTest1 {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // 写出：序列化
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream dos = new ObjectOutputStream(
                new BufferedOutputStream(baos)
        );
        // 操作数据类型 + 数据
        dos.writeUTF("编码辛酸泪");
        dos.writeInt(18);
        dos.writeBoolean(false);
        dos.writeChar('a');
        // 对象
        dos.writeObject("谁解其中味");
        dos.writeObject(new Date());
        Employee emp = new Employee("马云", 400);
        dos.writeObject(emp);
        dos.flush();

        byte[] datas = baos.toByteArray();
        System.out.println(datas.length);

        // 读取：反序列化
        ObjectInputStream dis = new ObjectInputStream(
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
        // 对象的数据还原
        Object str = dis.readObject();
        Object date = dis.readObject();
        Object employee = dis.readObject();

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

// javabean 封装数据
class Employee implements java.io.Serializable{
    private transient String name;      // 该数据不需要序列化
    private double salary;

    public Employee() {
    }

    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }
}