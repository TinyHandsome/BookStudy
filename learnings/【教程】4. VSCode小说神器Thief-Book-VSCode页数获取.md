# VSCode小说神器Thief-Book-VSCode页数获取

## 写在前面

- 做这件事的原因：
  1. 用这个工具摸鱼看小说吧，有一个问题，那就是摸鱼的时候很爽，但是有空了可以光明正大看小说的时候，这么一行一行的看就十分离谱，**不能跨设备同步看小说的进度**，但是如果拿出来看吧（比如用手机看，手机可以搜索字段嘛），很容易定位自己摸鱼看的进度。可是看了一段时间，又回到摸鱼的时候，就很难定位自己的进度。
  2. 然后就是，在设置每一行的字数长度的时候（默认是50嘛），设置一次，进度全乱了，很气。但是根据vscode不同的缩放比例（***ctrl*** + ***+***），设置不同的每行字数，很重要，*懂我什么意思叭*（歪头）。
  3. 所以，我就寻思，得想个办法，可以根据某个关键词，定位我看到哪儿了，然后计算这个是拿一页。**于是我开始了我的艰难的阅读源码之旅，然后写个python脚本来解决这个问题**
  4. 如果有需求的话，觉得脚本不香的话，我可以做个软件，不懂编程的人也能用啦（但是不懂编程的人用vscode干神魔呢？（歪头））
- 参考连接：
  1. [Thief-Book-VSCode的github地址](https://github.com/cteamx/Thief-Book-VSCode)
  2. [主要参考源码地址](https://github.com/cteamx/Thief-Book-VSCode/blob/master/src/bookUtil.ts)
  3. [插件安装地址](https://marketplace.visualstudio.com/items?itemName=C-TEAM.thief-book)

## 解决方案

1. 如果不会编程的话，我可以想办法把程序做成小软件，留言告诉我哦。（没需求我就不做了）

2. 以下是python代码，环境python3.7

   ```python
   #!/usr/bin/env python
   # -*- coding: UTF-8 -*-
   # coding=utf-8 
   
   """
   @author: Li Tian
   @contact: litian_cup@163.com
   @software: pycharm
   @file: xiaoshuo_locatoin.py
   @time: 2020/12/19 14:07
   @desc: Thief-Book-VSCode查找小说的显示进度
   """
   
   from dataclasses import dataclass
   from math import ceil
   
   
   @dataclass
   class XiaoshuoLocation:
       line_length: int
       file_path: str
   
       def __post_init__(self):
           self.pages, self.view_list = self.get_location()
   
       def depart_line(self, line):
           count = int(len(line) / 30) + 1
           result_line = []
           for i in range(count):
               start = i * self.line_length
               end = start + self.line_length
               result_line.append(line[start: end])
           return result_line
   
       def get_location(self):
           """获取小说的显示页数"""
           with open(self.file_path, 'r', encoding='utf-8') as f:
               result = f.read()
               temp = result.replace('\n', " ").replace('\r', " ").replace('　　', " ").replace(' ', " ")
   
               return ceil(len(temp) / self.line_length), self.depart_line(temp)
   
       def search_words(self, aim_words):
           count = 1
           for line in self.view_list:
               if aim_words in line:
                   print(count, ": ", line)
   
               count += 1
   
   
   if __name__ == '__main__':
       XiaoshuoLocation(30, 'E:\study_books\《明朝那些事》(全集).txt').search_words('小弟的肩膀')
   ```

3. 使用方式不用我教了叭

   - 30：每行多少个字嘛，就是配置里面的那个Page Size

   - 后面的就是小说的txt路径啦

   - 最后一个参数：就是要搜索的内容，如果查不到的话，**如果你改了PageSize，是有可能查不到的，因为原来是一个page 的，可能分成两个page了，被隔断了**，那就搜内容的前后一小部分看看。

   - 结果展示：冒号前面的数字，就是你要的目标页数啦。

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201219175138581.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 源码解析

> 讲道理，看完源码，觉得内存烧的有点多，内容啊、页码啊获取一次就好啦，我看每次翻页都要搞一次IO，很影响性能的。希望作者可以优化一下代码，早日添加内容搜索定位页码的功能嗷！

1. 首先啊，先贴上这个神器的源码

   ```js
   import { ExtensionContext, workspace, window } from 'vscode';
   import * as fs from "fs";
   
   export class Book {
       // 现在是哪一页
       curr_page_number: number = 1;
       // 每一页显示的长度
       page_size: number | undefined = 50;
       // text分几页，总页数
       page = 0;
       start = 0;
       end = this.page_size;
       // 文件路径
       filePath: string | undefined = "";
       extensionContext: ExtensionContext;
   
       constructor(extensionContext: ExtensionContext) {
           this.extensionContext = extensionContext;
       }
   
       getSize(text: string) {
           // text长度
           let size = text.length;
           // text分几页，向上取整
           this.page = Math.ceil(size / this.page_size!);
       }
   
       getFileName() {
           var file_name: string | undefined = this.filePath!.split("/").pop();
           console.log(file_name);
       }
   
       getPage(type: string) {
           // 取出当前页
           var curr_page = <number>workspace.getConfiguration().get('thiefBook.currPageNumber');
           var page = 0;
   
           if (type === "previous") {
               // 如果按了上一页，当前页减一或为第一页
               if (curr_page! <= 1) {
                   page = 1;
               } else {
                   page = curr_page - 1;
               }
           } else if (type === "next") {
               // 如果按了下一页，当前页加一
               if (curr_page! >= this.page) {
                   page = this.page;
               } else {
                   page = curr_page + 1;
               }
           } else if (type === "curr") {
               page = curr_page;
           }
   
           this.curr_page_number = page;
           // this.curr_page_number = this.extensionContext.globalState.get("book_page_number", 1);
       }
   
       updatePage() {
           workspace.getConfiguration().update('thiefBook.currPageNumber', this.curr_page_number, true);
       }
   
       getStartEnd() {
           this.start = this.curr_page_number * this.page_size!;
           this.end = this.curr_page_number * this.page_size! - this.page_size!;
       }
   
       readFile() {
           if (this.filePath === "" || typeof (this.filePath) === "undefined") {
               window.showWarningMessage("请填写TXT格式的小说文件路径 & Please fill in the path of the TXT format novel file");
           }
   
           var data = fs.readFileSync(this.filePath!, 'utf-8');
   
           var line_break = <string>workspace.getConfiguration().get('thiefBook.lineBreak');
   
           return data.toString().replace(/\n/g, line_break).replace(/\r/g, " ").replace(/　　/g, " ").replace(/ /g, " ");
       }
   
       init() {
           this.filePath = workspace.getConfiguration().get('thiefBook.filePath');
           var is_english = <boolean>workspace.getConfiguration().get('thiefBook.isEnglish');
   
           if (is_english === true) {
               this.page_size = <number>workspace.getConfiguration().get('thiefBook.pageSize') * 2;
           } else {
               this.page_size = workspace.getConfiguration().get('thiefBook.pageSize');
           }
       }
   
       getPreviousPage() {
           this.init();
   
           let text = this.readFile();
   
           this.getSize(text);
           this.getPage("previous");
           this.getStartEnd();
   
           var page_info = this.curr_page_number.toString() + "/" + this.page.toString();
   
           this.updatePage();
           return text.substring(this.start, this.end) + "    " + page_info;
       }
   
       getNextPage() {
           this.init();
   
           let text = this.readFile();
   
           this.getSize(text);
           this.getPage("next");
           this.getStartEnd();
   
           var page_info = this.curr_page_number.toString() + "/" + this.page.toString();
   
           this.updatePage();
   
           return text.substring(this.start, this.end) + "    " + page_info;
       }
   
       getJumpingPage() {
           this.init();
   
           let text = this.readFile();
   
           this.getSize(text);
           this.getPage("curr");
           this.getStartEnd();
   
           var page_info = this.curr_page_number.toString() + "/" + this.page.toString();
   
           this.updatePage();
   
           return text.substring(this.start, this.end) + "    " + page_info;
       }
   }
   ```

2. 我们先看readFile()函数

   ```js
   readFile() {
       if (this.filePath === "" || typeof (this.filePath) === "undefined") {
           window.showWarningMessage("请填写TXT格式的小说文件路径 & Please fill in the path of the TXT format novel file");
       }
   
       var data = fs.readFileSync(this.filePath!, 'utf-8');
   
       var line_break = <string>workspace.getConfiguration().get('thiefBook.lineBreak');
   
       return data.toString().replace(/\n/g, line_break).replace(/\r/g, " ").replace(/　　/g, " ").replace(/ /g, " ");
   }
   ```

   - 先读文件路径

   - 然后读文件

   - 获取line_break，也就是分隔符（默认是一个空格）

   - 替换各个符号

     - `/[\r]/g`在js中是正则表达式对象，在两个`/`之间的部分是表达式的主体，表示要匹配的字符串；`g`表示在整个字符串中搜索。所以这段代码中要匹配的字符串是`[\r]`所代表的字符串，其中`[]`”表示字符的可选范围。

     - 首先是`\n`，即软回车，替换为line_break

     - 然后是把`\r`，即软空格，表示回到当前行的行首，替换为一个空格

       ```python
       print('asdf\rqw')
       # qw
       ```

     - 然后是一个unicode为12288的字符，为全角空格，这里替换为一个空格，

       ```python
       print(ord('　'))
       # 12288
       ```

     - 然后是将空格转换为空格，这里我蒙了。。。

     - 最后返回的就是各种处理之后的小说文字了，string。

3. 然后从按键的逻辑粗发

   ```js
   getPage(type: string) {
       // 取出当前页
       var curr_page = <number>workspace.getConfiguration().get('thiefBook.currPageNumber');
       var page = 0;
   
       if (type === "previous") {
           // 如果按了上一页，当前页减一或为第一页
           if (curr_page! <= 1) {
               page = 1;
           } else {
               page = curr_page - 1;
           }
       } else if (type === "next") {
           // 如果按了下一页，当前页加一
           if (curr_page! >= this.page) {
               page = this.page;
           } else {
               page = curr_page + 1;
           }
       } else if (type === "curr") {
           page = curr_page;
       }
       this.curr_page_number = page;
   ```

   - 先获取当前页，从设置里面的当前页获取这个值
   - `!`：用在赋值的内容后时，使null和undefined类型可以赋值给其他类型并通过编译
   - 然后是if-else逻辑了：
     - 如果是 **上一页** ：先检查当前页是不是<=1，是的话就把page=1，否则page=当前页-1
     - 如果是 **下一页** ：先检查当前页是不是>=小说的总页数，是的话page=小说的总页数，否则page=当前页+1
     - 如果是 **当前页** ：page=当前页
     - 设置全局当前页为page

4. 初始化

   ```js
   init() {
       this.filePath = workspace.getConfiguration().get('thiefBook.filePath');
       var is_english = <boolean>workspace.getConfiguration().get('thiefBook.isEnglish');
   
       if (is_english === true) {
           this.page_size = <number>workspace.getConfiguration().get('thiefBook.pageSize') * 2;
       } else {
           this.page_size = workspace.getConfiguration().get('thiefBook.pageSize');
       }
   }
   ```

   - **获取文件路径**，放到全局变量filePath
   - 英文处理：这就不说了
   - **获取每一页显示的长度**，默认50
   - 所以初始化就这两步

5. 上一页的逻辑

   ```js
   getPreviousPage() {
       this.init();
   
       let text = this.readFile();
   
       this.getSize(text);
       this.getPage("previous");
       this.getStartEnd();
   
       var page_info = this.curr_page_number.toString() + "/" + this.page.toString();
   
       this.updatePage();
       return text.substring(this.start, this.end) + "    " + page_info;
   }
   ```

   - 初始化
   - 获取小说string
   - getSize：获取整篇小说的长度，并进行分页
   - 获取上一页，这里将全局变量curr_page_number设置为 **上一页** 
   - 获取开始和结束：
     - 全局变量开始 = 全局变量curr_page_number × 每一页长度
     - 全局变量结束 = 全局变量curr_page_number × 每一页长度 - 每一页长度
   - page_info：这里显示`当前页/总页数`
   - updatePage：将当前页的值写到配置文件中
   - 返回：每页的文字 + 四个空格 + page_info
   - 下一页和跳页的逻辑几乎一样

------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友