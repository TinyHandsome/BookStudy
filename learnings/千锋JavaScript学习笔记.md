# 学习笔记

[TOC]

## 写在前面

- 封面 | 摘要

  ![封面](https://img2022.cnblogs.com/blog/1589204/202209/1589204-20220905095739193-1849832512.jpg)

- 学习链接

- 感想 | 摘抄

- 学习时遇到的问题

- 直通车

- <span style="color: skyblue; font-weight: bold">PS：相关工程代码都在 Github 上</span>

## 1. JS基础

1. js实际上是两种语言风格的混合产物，简化的函数式编程和简化的面向对象编程

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/4af87e8485da4f91b0472e8d6981b39c.png)

2. JS决定行为

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/3887e4a783b140cc8267d0601dfd14ad.png)

3. JS的三大核心组成

   - BOM：Browser Object Model，JS操作浏览器发生变化的属性和方法
   - DOM：Document Object Model，JS操作文档流发生变化的属性和方法
   - ECMAScript：JS的书法语法和书写规则

4. JS的书写位置

   - 行内式：直接把代码书写在标签身上

     **强烈不推荐，既不利于代码的维护，也会导致html文件臃肿**

     - a标签：书写在href属性上

       `<a href="javascript: alert('hello world');">点我一下</a>`

     - 非a标签：书写在行为属性上

       `<div onclick="alert('hello world')">点我一下</div>`

   - 内嵌式：把代码书写在一个 script 标签对内

     **不是很推荐**

     ```html
     <script>
     	alert('hello world');
     </script>
     ```

   - 外链式：把代码书写在一个.js文件内

     `<script src="helloworld.js"></script>`

     **最推荐的书写方式**

### 1.1 变量

- 变量赋值：`var num = 100`

- 小结：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/842d5d3ec7794bf0bb2cf3ac4eddf5a9.png)

- 单行注释：`//`

- 多行注释：`/* 注释内容 */`

- 几个在浏览器中输出的方式

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/ced422a5985e45688c3631017b04a7e3.png)

### 1.2 数据类型

- 数值类型

  - 科学计数法：`2e5=2x10^5`

  - 进制：

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/03152ceafda14c018d89a29e567cf7e6.png)

  - js中的数据

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/7e86400763eb48cbb47dd62d518880da.png)

- 字符串：不区分单引号和双引号

- 布尔类型：true，false

- 空类型：

  - null：表示有值，有一个空值：`var k1 = null`
  - undefined：表示没有值：`var k2`

- 使用 `typeof` 关键字来进行数据类型检测，语法：`typeof` 要检测的变量；结果：该变量存储的数据的数据类型

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/d173b74e689142a7ba747ad445c040db.png)

- 小结：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/a8f56398a13d4be2bc6fae30e0ba604b.png)

### 1.3 数据类型转换

- 转数值

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/2e4861953ffb49079a8e31964c4574a8.png)

  - Number就是直接全部转，行就行，不行就NaN
  - parseInt是从前往后扫描，如果是数就要，不是就结束了，如果开始都不是数，就直接NaN
  - parseFloat是可以识别小数，其他的都是只能转化整数

- 转字符串

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/f29f393510204c4294641580de8a502d.png)

  - 没有特别要注意的地方，就是两种方式的语法不同

- 转布尔

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/590a84617f3b4f3bbe02629b32e5324c.png)

  - 只有5个值会被转为false，其他的都会被转为true

- 小结：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/56ecc4d836c9460f8e9d6ab691be1834.png)

### 1.4 运算符

![在这里插入图片描述](https://img-blog.csdnimg.cn/2c9933a99f7144c9b6b36c5b845304b2.png)

- 算数运算符：进行 数学运算 的符号

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/1c815aee27184fe09629edbaf8940f90.png)

- 赋值运算符：进行 赋值操作 的符号

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/b81f9787516640798ad9a8fb8fb69e9a.png)

- 比较运算符：进行 比较运算 的符号

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/7c04b304d4f8473187c78a854c4df36e.png)

- 逻辑运算符：进行 逻辑运算 的符号

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/d586c4b860c14d76800a21688f182419.png)

- 自增自减运算符：单独对一个变量进行 +1 或者 -1 操作的符号

  基本跟C语言一样，++和--

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/89de15117df84465ab5367d7cab4216c.png)

- 小结

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/68906d095ddc4c459a4054cf332df050.png)

### 1.5 条件

![在这里插入图片描述](https://img-blog.csdnimg.cn/0c3c8ddfeb184af9b959bfefcffa6032.png)

1. 案例1：平年还是闰年？

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2ed60430ab3a47b38163711d67c08ed5.png)

   ```js
   var year = 2004
           
   if (year % 4 == 0 && year % 100 !=0 || year % 400 == 0) {
       console.log(year + '是闰年')
   } else {
       console.log(year + '不是闰年')
   }
   ```

2. 条件分支语句

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/a2208d4e33674b1ea7805f27c1a171dc.png)

   - 记得满足条件的执行逻辑中需要加入break

   - 最后可以加一个default，如果所有选项都不匹配时，则执行default

   - 小结：

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/85003c6d0cf547eda412bbb6d3b82f7f.png)

3. 案例2：一年中的第几天

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/f760d96430834e33a2eabfac3a45eeb4.png)

### 1.6 循环

- while

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/30b95cbcd9604550ac315fc0b9d8ef8f.png)

    - 小结：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/76c091527787488490f1ae3edb47ab5f.png)

- dowhile;

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/f7c136d8e2d3481099d727e9b944dabb.png)

- for

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/549f713dd8b14171ab5f86f959aed855.png)

    ```js
    for (var i = 0; i < 3; i ++) {
        console.log('啊吧啊吧' + i)
    }
    console.log('完事儿了')
    ```

- 循环的练习

    ```js
    for (var i=0; i <9; i++) {
        for (var j=0; j<9; j++){
            document.write('*')
        }
        document.write('<br>')
    }
    
    for (var i=1; i <= 9; i++){
        for (var j=1; j<=i; j++){
            document.write(i + '*' + j + '=' + i * j + '    ')
        }
        document.write('<br>')
    }
    ```

### 1.7 函数

![在这里插入图片描述](https://img-blog.csdnimg.cn/e36b0c14eaee47a2a4a7fa3040ab930c.png)

- 小结

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/28c94fa8d51f4befaca20bfb83fa9950.png)

1. 递归函数

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/30f2fc4448ef48d7accb0c205c331ef7.png)

2. 作用域

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/98dd2396dccc4b8780041a9ce0b610bb.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/34d4c19a6d7f4c9b80dd4328ba1e6fdc.png)

### 1.8 对象数据类型

- 对象：类似于python中的字典：键值对来表示，`var obj = {'a': 1, 'b': 2}`

- 增：

  - `obj.a = 1`
  - `obj['a'] = 1`

- 删：

  - `delete obj.a`
  - `delete obj['a']`

- 改：与【增】的一样

- 查：

  - `obj.a`
  - `obj['a']`

- 小结：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/aa83156442434ad2a27ce7d76db13695.png)

### 1.9 数组和排序

- 数组中可以存储任何数据类型

- `var arr = [100, true, 'hello world']`

- `arr.length`：获取长度

- `arr.length`：修改长度，截取数据，放弃后面的数据

- `arr[2]`：访问数组数据

- `arr[2] = 1`：设置数组数据

- 通过循环遍历数组：`for(var i=0; i<arr.length; i++)`

- 小结

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/a2d9e6e80e434eaaa58879aa95fb0ae1.png)

1. 冒泡排序

   - 核心思想就是，每一轮从头到尾两两比较，每一轮都能把最大的值冒泡到最后的位置

     ```js
     var arr = [9, 3, 6, 2, 4, 1, 8, 5, 7]
     
     for (var j = 0; j < arr.length - 1; j++) {
         for (var i=0; i < arr.length -1-j; i ++) {
             if(arr[i] > arr[i+1]) {
                 var temp = arr[i]
                 arr[i] = arr[i+1]
                 arr[i + 1] = temp
             }
         }
     }
     console.log(arr)
     ```

2. 选择排序

   - 核心思想是 **索引** 位置上数的对比

   - 假设最小的索引是0，然后拿其他索引位置的值跟它比较，然后找到真实最小的索引，然后交换值。每一轮就可以把最小值搞到。

     ```js
     for (var j=0; j < arr.length - 1; j++){
         var minIndex = j
         for (var i = j + 1; i < arr.length; i++){
             if (arr[i] < arr[minIndex]) {
                 minIndex = i
             }
         }
         var temp = arr[j]
         arr[j] = arr[minIndex]
         arr[minIndex] = temp
     }
     console.log(arr)
     ```

### 1.10 数组常用方法：

- push

  - `arr.push(data)`
  - 将数据追加到数组的末尾，返回 数组最新的长度

- pop

  - `arr.pop()`
  - 删除数组最后一个数据，返回被删除的数据

- unshift

  - `arr.unshift(data)`
  - 将数据添加到数组的最前面，返回 数组最新的长度\

- shift

  - `arr.shift()`
  - 删除数组最前面的数据，返回被删除的数据

- reverse

  - `arr.reverse()`
  - 将数组 反转，返回 被反转的数组

- splice

  - `arr.splice(开始索引, 多少个, 要插入的数据)`
  - 开始索引默认0；多少个默认0；要插入的数据默认没有
  - 删除 数组中若干数据，冰选择是否插入新的数据
  - 返回 以数组的形式|被删除的数据

- sort

  - `arr.sort()`：按位排序
  - `arr.sort(function (a, b) {return a - b})`：从小到大排序
  - `arr.sort(function (a, b) {return b - a})`：从大到小排序
  - 将数组进行 排序

- join

  - `arr.join(连接符)`
  - 将数组 用连接符 连接成一个字符串，返回连接好的 字符串

- concat

  - `arr.concat(其他数组)`
  - 将其他数组和数组 拼接 在一起，返回拼接好的 字符串

- slice

  - `arr.slice(开始索引, 结束索引)`
  - 开始索引的默认值是0，结束索引的默认值是 数组长度
  - 截取 数组中的某些数据，返回截出来数组
  - 前开后闭，包前不包后

- indexOf

  - `arr.indexOf(数据)`
  - 查找 数据 在数组中的 索引位置；如果有该数据，则返回 第一次出现的索引位置，否则返回 -1

- forEach

  - `arr.forEach(function(item, index, arr){})`
  - 遍历数组，没有返回值
  - item：每次循环的值
  - index：每次循环的索引
  - arr：数组本身
  - 然后对数组中的每个元素执行函数操作

- map

  - `arr.map(function(item, index, arr){})`
  - 映射 数组，跟forEach类似，只不过有返回值，返回映射后的新数组
  - 注意这里需要返回处理后的数据

- filter

  - `arr.filter(function(item, index, arr){})`
  - 过滤 数组，返回过滤好的新数组
  - 返回的数组是原始数组中所有满足条件的项
  - 注意，这里跟map不同，函数返回的是布尔类型的数据用来过滤

- every

  - `arr.every(function(item, index, arr){})`
  - 判断数组是不是 每一项 都满足条件，返回 **一个** 布尔值
  - 函数中也是返回布尔类型的数据
  - 逻辑就是数组中是否每一项都满足函数中的条件，即是否都返回True
  - 类似 python 的 **all** 吧

- some

  - `arr.some(function(item, index, arr){})`
  - 跟every相对的，判断数组是不是存在某一项满足条件，返回 **一个** 布尔值
  - 类似python中的 **any** 吧

- 小结

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/777a286a68e04a23b6a9b0e89fd601ca.png)

### 1.11 字符串常用方法

1. charAt

   - `str.charAt(索引)`
   - 获取对应索引位置的字符，返回字符

2. toLowerCase

   - `str.toLowerCase()`
   - 将字符串内的字母全部转换成小写，返回转换后的字符串

3. toUpperCase

   - `str.toUpperCase()`
   - 将字符串内的字母全部转换成大写，返回转换后的字符串

4. replace

   - `str.replace(换下内容, 换上内容)`
   - 将字符串内 第一个 满足换下内容的片段替换成 换上内容，返回换好的字符串

5. trim

   - `str.trim()`
   - 去除字符串首尾的空格，返回修改后的字符串

6. split

   - `str.split(分隔符)`
   - 按照分隔符把字符串切割成一个数组，返回该数组

7. substr, substring, slice

   - `str.substr(开始索引, 长度)`

   - `str.substring(开始索引，结束索引)`，前闭后开

   - `str.slice(开始索引, 结束索引)`，跟substring一样，也是前闭后开

   - 截取字符串，返回该字符串

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/6d0067ddbda14e8bbd6af8c3cb7b6e89.png)

8. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/39b83b9100574b5eb9db447bc3978375.png)

### 1.12 数字常用方法

1. random

   - `Math.random()`
   - 获取`[0, 1)`之间的随机小数，前闭后开，返回该数

2. round

   - `Math.round(数字)`
   - 对数字进行四舍五入的取整，返回该数

3. ceil | floor

   - `Math.ceil(数字)` | `Math.floor(数字)`
   - 对数字进行向上|下取整，返回该数

4. pow

   - `Math.pow(底数，指数)`
   - 对数字进行 取幂 运算，返回结果

5. sqrt

   - `Math.sqrt(数字)`
   - 对数字进行 二次方根 运算，返回结果

6. abs

   - `Math.abs(数字)`
   - 对数字进行 绝对值 运算，返回结果

7. max | min

   - `Math.max(多个数字)` | `Math.min(多个数字)`
   - 获得多个数字的最大|小值，返回结果

8. PI

   - `Math.PI`
   - 得到一个近似Π的值

9. 案例1：获得0-10之间的随机证数

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/7be90680923f4157acf6a2ac492e3d3f.png)

10. 小结

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/8468e99ca52946b09edb6f85abdc2e2a.png)

### 1.13 时间常用方法

1. 查看时间

   ```js
   var time = new Date()
   console.log(time)
   ```

2. 创建时间

   ```js
   var time = new Date(2002, 1, 23, 11, 22, 18)
   console.log(time)
   ```

3. 获取时间的方法

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2e801fd2070a4d0db585c2a1c2344732.png)

   - 时间戳

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/b95bf3f006f44c8992791bbb4a21152a.png)

4. 设置时间的方法

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/6643d31a6a7445ccaf4268b5f43b2058.png)

5. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/b3f41a81898242078184e3999034a912.png)

6. 案例1：计算时间差

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/9a858e33890e4b67bfbffda33e4a6056.png)

### 1.14 JS的BOM操作

BOM：Browser Object Model

1. 获取浏览器窗口尺寸

   - 获取可视窗口宽度：window.innerWidth
   - 获取可视窗口高度：window.innerHeight

2. 浏览器的弹出层

   - 提示框：window.alert(info)

   - 询问框：window.confirm(info)

     有返回值，true | false

   - 输入框：window.prompt(info)

     有返回值，输入的内容 | null

3. 开启和关闭标签页

   - 开启：window.open(地址)

   - 关闭：window.close()

   - 样例

     ```html
     <body>
     
         <button id="on">开启</button>
         <button id="off">关闭</button>
     
         <script>
             on.onclick = function () {
                 window.open('http://www.baidu.com/')
             }
             off.onclick = function () {
                 window.close()
             }
     
         </script>
     </body>
     ```

   - 在js中可以直接引用  **id**  设置属性和事件

4. 浏览器的常用事件

   - 资源加载完毕：window.onload = function(){}
   - 可视尺寸改变：window.onresize= function(){}
   - 滚动条位置改变：window.onscroll= function(){}

5. 浏览器的历史记录操作

   - 回退页面：window.history.back()

     相当于浏览器的左箭头

   - 前进页面：window.history.forward()

     相当于浏览器的右箭头

6. 浏览器卷去的尺寸

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/e377befe664546939236550e17b9be2f.png)

   - 卷去的高度：即拖动滚动条越大，值越大，初始位置的值为0

     - document.documentElement.scrollTop

     - document.body.scrollTop

     - 上面两个语法的区别在于，前者需要html头有 `<!DOCTYPE html>`，否则就用后者，所以在实际使用中可以写成如下兼容的写法

       ```js
       var height = document.documentElement.scrollTop || document.body.scrollTop
       ```

   - 卷去的宽度：

     - document.documentElement.scrollLeft
     - document.body.scrollLeft
     - 规则与上述高度一样

7. 浏览器滚动到

   - window.scrollTo()

     - 参数方式1：window.scrollTo(left, top)

       - left：浏览器卷去的宽度
       - top：浏览器卷去的高度
       - **这种方法只能瞬间定位，不能滚动**

     - 参数方式2：

       ```js
       window.scrollTo({
       	left: xx,
       	top: yy,
       	behavior: 'smooth'
       })
       ```

       - 滚动条滚动到指定位置

8. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/7541f06f33244d24806f1b3a70871861.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/d2c53d417daa41f790d9d4f03597ae3c.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/88e3750c84ed4402aa670acf4b22b47b.png)

### 1.15 JS的定时器

1. 

















学到P212


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
