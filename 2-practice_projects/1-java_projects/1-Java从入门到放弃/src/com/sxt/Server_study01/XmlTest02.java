package com.sxt.Server_study01;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: XmlTest02.java
 * @time: 2019/11/29 15:31
 * @desc: 获取xml中的内容
 */

public class XmlTest02 {
    public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {
        // SAX解析
        // 1. 获取解析工厂
        SAXParserFactory factory = SAXParserFactory.newInstance();
        // 2. 从解析工厂获取解析器
        SAXParser parse = null;
        parse = factory.newSAXParser();
        // 3. 加载文档Document注册处理器
        // 4. 编写处理器
        PersonHandler handler = new PersonHandler();
        parse.parse(Thread.currentThread().getContextClassLoader().getResourceAsStream("com/sxt/Server_study01/p.xml"), handler);
        // 5. 获取数据
        List<Person> persons = handler.getPersons();
        for (Person p : persons) {
            System.out.println(p.getName() + "-->" + p.getAge());
        }
    }
}

class PersonHandler extends DefaultHandler {
    private List<Person> persons;
    private Person person;
    private String tag;     // 存储操作的标签

    @Override
    public void startDocument() throws SAXException {
        System.out.println("解析文档开始");
        persons = new ArrayList<>();
    }

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (null != qName) {
            tag = qName;        // 存储标签名
            if (tag.equals("person")) {
                person = new Person();
            }
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        String contents = new String(ch, start, length).trim();
        if (contents.length() > 0) {
            if (tag.equals("name")) {
                person.setName(contents);
            } else if (tag.equals("age")) {
                person.setAge(Integer.valueOf(contents));
            }
        }
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        if (qName.equals("person")) {
            persons.add(person);
        }
    }

    @Override
    public void endDocument() throws SAXException {
        System.out.println("解析文档结束");
    }

    public List<Person> getPersons() {
        return persons;
    }
}