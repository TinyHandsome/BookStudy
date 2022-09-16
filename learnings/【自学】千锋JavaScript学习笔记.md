# 学习笔记

[TOC]

## 写在前面

- 封面 | 摘要

  ![封面](https://img2022.cnblogs.com/blog/1589204/202209/1589204-20220905095739193-1849832512.jpg)

- 学习链接：[千锋HTML5前端开发教程1000集](https://www.bilibili.com/video/BV17z4y1D7Yj)：`[184集: 286集]，共103集`

- 感想 | 摘抄

- 学习时遇到的问题

  1. [CSS中的position:relative理解](https://blog.csdn.net/gamenoover/article/details/90614014)

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

### 1.14 BOM基本操作

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

1. 间隔定时器

   - 按照指定周期（毫秒）去执行指定的代码

   - 语法：`setInterval(函数, 时间)`

     - 函数：每次要执行的内容
     - 时间：单位是毫秒

   - 实例：

     ```js
     var n = 0;
     setInterval(
         function () {
             n += 1
             console.log(n)
         }, 1000
     )
     ```

2. 延时定时器

   - 在固定的时间（毫秒）后执行一次代码
   - 语法：`setTimeout(函数, 时间)`
     - 函数：时间到达执行的内容
     - 时间：单位是毫秒

3. 定时器的返回值

   - 不区分定时器种类，表示当前页面的第几个定时器，从1开始计数
   - 作用：关闭定时器需要知道定时器索引

4. 关闭定时器：

   - clearInterval(要关闭的定时器返回值)
   - clearTimeout(要关闭的定时器返回值)
   - 注意：定时器的关闭是不区分定时器种类的

5. 小结：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/84582eaba60d46e19d921bf7ac740061.png)

### 1.16 DOM的基本操作

DOM：Document Object Model

1. 一整套操作文档流相关内容的属性和方法，可以操作元素：
   - 修改样式
   - 修改属性
   - 改变位置
   - 添加事件

2. 获取元素的方式
   - 根据 id 名称获取
     - `document.getElementById('id名称')`
     - 获取文档流中 id 对应的 **一个** 元素
     - 返回：
       - 这个元素，if 有
       - null，if 没有
   - 根据类名获取
     - `document.getElementsByClassName('元素类名')`
     - 获取文档流中的 **所有** 类名对应的元素（注意这里有s，这是因为id是唯一的，类名不是）
     - 返回值必然是一个 **伪数组**：
       - 有多少获取多少，if 有
       - 空的伪数组，if 没有
   - 根据标签名获取
     - `document.getElementsByTagName('标签名')`
     - **同类名获取**，返回伪数组
   - 根据选择器获取
     - `document.querySelector('选择器')`
     - **同id名称获取**，但是与id不同的，可能会取到多个，但是只会获取 **第一个**
     - 选择器可以获取上述所有的元素
       - class：.类名
       - id：#id名
       - tag：标签名
   - 通过选择器获取一组元素
     - `document.querySelectorAll('选择器')`
     - 获取文档流中 **所有** 满足选择器规则的元素，返回伪数组
     - **同类名获取**

3. 操作元素内容
   - 操作元素文本内容，就是元素中的内容
     - 获取：`元素.innerText`
     - 设置：`元素.innerText = '新内容'`
   - 操作元素超文本内容，就是整个元素
     - 获取：`元素.innerHTML`
     - 设置：`元素.innerHTML = '新内容'`

4. 操作元素属性
   - 原生属性
     - 获取：`元素.属性名`
     - 设置：`元素.属性名= '属性值'`
   - 自定义属性
     - 获取：`元素.getAttribute('属性名')`
     - 设置：`元素.setAttribute('属性名', '属性值')`
     - 删除：`元素.removeAttribute('属性名')`
   - 注意：以上方法一般埠用作操作元素的 **类名** 和 **样式**

5. 操作元素类名
   - 获取：`元素.className`
   - 设置：`元素.className = '新类名'`

6. 操作元素行内样式
   - 获取：`元素.style.样式名`
   - 设置：`元素.style.样式名 = '样式值'`
   - 获取样式中的值时使用类似 `box.style.width` 的语法，需要注意的是，中划线的样式名需要改为驼峰式语法：`box.style.backgroundColor`
   - 注意：只能获取和设置元素的 **行内样式**

7. 获取元素非行内样式
   - 获取：`window.getComputedStyle(元素).样式名`
   - 注意：可以获取行内样式，也可以获取非行内样式
   - 但是不能设置非行内样式，前端只能设置行内样式

8. 小结：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/60a677e41a3345ff8c1a8a9399194e4b.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/aae3ef814a9e4a7a8320fdc6a32bdf4f.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/00919cab63e44fae8a2a3be904ee1aec.png)

9. 案例1：回到顶部

   - 确认需求

     1. 滚动条滚动超过临界点：顶部通栏显示，否则隐藏
     2. 滚动条滚动超过临界点：回到顶部按钮显示，否则隐藏
     3. 点击回到顶部按钮：滚动条滚动回到顶部

   - 布局结构

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/6ffce889a32243de9c9be880ca7e7594.png)

   - 代码逻辑

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/1b2ea6a4206347c19423d9d3015dea4d.png)

   - 代码：

     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Document</title>
         <style>
             * {
                 margin: 0;
                 padding: 0;
             }
             body {
                 height: 3000px;
             }
             .header {
                 width: 100%;
                 height: 80px;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 font-size: 30px;
                 color: #fff;
                 background-color: skyblue;
     
                 transition: top 0.2s linear;
     
                 position: fixed;
                 top: -80px;
                 left: 0;
             }
     
             .goTop {
                 width: 50px;
                 height: 50px;
                 background-color: pink;
                 font-size: 20px;
                 text-align: center;
                 line-height: 25px;
                 color: #fff;
     
                 position: fixed;
                 bottom: 50px;
                 right: 50px;
     
                 display: none;
             }
         </style>
     </head>
     <body>
         <div class="header">顶部通栏</div>
         <div class="goTop">回到顶部</div>
     
         <script>
             // 1. 获取元素
             var header = document.querySelector('.header')
             var goTop = document.querySelector('.goTop')
     
             // 2. 绑定滚动事件
             window.onscroll = function(){
                 // 2.1 获取浏览器卷去的高度
                 var height = document.documentElement.scrollTop || document.body.scrollTop
                 // 2.2 判断卷去的高度
                 if (height >= 300) {
                     // 显示
                     header.style.top = '0px'
                     goTop.style.display = 'block'
                 }else{
                     // 隐藏
                     header.style.top = '-80px'
                     goTop.style.display = 'none'
                 }
             }
     
             // 3. 绑定点击事件
             goTop.onclick = function(){
                 window.scrollTo({
                     top: 0,
                     behavior: 'smooth'
                 })
             }
         </script>
     </body>
     </html>
     ```

10. 案例2：全选

    - 确认需求：

      1. 全选按钮点击的时候，根据自身状态决定所有选项按钮状态
      2. 点击每一个选项按钮的时候，根据所有选项按钮状态决定全选按钮状态

    - 布局结构

      1. 需要一个 全选按钮 和若干的 选项按钮 标签

    - 代码逻辑

      1. 给 全选按钮 绑定点击事件
         - 拿到自己的选中状态
         - 给所有选项按钮设置选中状态
      2. 给 每一个选项按钮 绑定点击事件
         - 判断是不是所有选项按钮都是选中的
         - 根据判断结果给全选按钮设置选中状态

    - 代码

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
          <style>
              * {
                  margin: 0;
                  padding: 0;
              }
              .box {
                  width: 100px;
                  padding: 20px;
                  border: 1px solid pink;
                  margin: 30px auto;
                  border-radius: 5px;
              }
              hr {
                  margin: 10px 0;
              }
          </style>
      </head>
      <body>
          <div class="box">
              全选：<input type="checkbox"> <br>
              <hr>
              <input type="checkbox"> 选项一 <br>
              <input type="checkbox"> 选项二 <br>
              <input type="checkbox"> 选项三 <br>
              <input type="checkbox"> 选项四 <br>
          </div>
      
          <script>
              // 1. 获取元素
              var allBtn = document.querySelector('input')
              // n+2指的是从第二个子元素开始
              var items = document.querySelectorAll('input:nth-child(n+2)')
              // console.log(allBtn);
              // console.log(items);
      
              // 2. 给全选按钮绑定事件
              allBtn.onclick = function () {
                  // 2.1 拿到自己的选中状态
                  var myType = allBtn.checked
                  // 2.2 把自己的选中状态设置给每一个选项按钮
                  for(var i = 0; i < items.length; i++) {
                      items[i].checked = myType
                  }
              }
      
              // 3. 循环给每一个选项按钮绑定点击事件
              for(var i = 0; i < items.length; i++) {
                  // 3.1 给每一个选项按钮绑定点击事件
                  items[i].onclick = function() {
                      // 3.2 首先定义假设变量，假设所有按钮都是选中的
                      var flag = true
      
                      // 3.3 啊通过循环来验证我们的假设
                      for (var j = 0; j < items.length; j++) {
                          if(items[j].checked === false) {
                              flag = false
                              break
                          }
                      }
      
                      // 3.4 把我们得到的结果设置给全选按钮
                      allBtn.checked = flag
                  }
              }
          </script>
      </body>
      </html>
      ```

11. 案例3：选项卡

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/29abc47b19684ddda993429bb0470924.png)

    - 确认需求：
      1. 点击哪一个按钮，其他按钮全部回归原始，当前高亮
      2. 点击哪一个按钮，其他盒子全部隐藏，当前索引对应盒子显示
    - 布局结构：
      1. 三个表示按钮的盒子，横向排列，初始一个高亮
      2. 三个显示内容的盒子，在 同一位置不同层级 排列，初始一个显示
    - 代码逻辑：
      1. 每一个 按钮盒子 绑定一个点击事件
      2. 点击任何一个按钮盒子时
         - 所有按钮盒子取消高亮状态
         - 所有内容盒子隐藏
      3. 点击任何一个按钮盒子时
         - 当前按钮盒子高亮
         - 当前索引对应内容盒子显示

12. 节点操作

    - 创建节点

      - `document.createElement('标签名称')`
      - 创建一个指定标签元素，返回创建好的元素节点

    - 插入节点

      - 语法1：`父节点.appendChild(子节点)`
      - 把 子节点 放在父节点 的内部，并且放在最后的位置
      - 语法2：`父节点.insertBefore(要插入的子节点，哪一个子节点的前面)`
      - 把子节点放在父节点的内部，并且放在指定某一个子节点的前面

    - 删除节点

      - 语法1：`父节点.removeChild(子节点)`
      - 从父节点内删除一个子节点
      - 语法2：`节点.remove()`
      - 把自己删除

    - 替换节点

      - `父节点.replaceChild(换上节点, 换下节点)`
      -  在父节点内，使用 换上节点 替换掉 换下节点

    - 克隆节点

      - `节点.cloneNode(是否克隆后代节点)`
      - 把该节点 复制 一份一模一样的内容
      - 返回克隆好的节点

    - 小结

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/54d025b5a065448081ae6f32f063c612.png)

13. 获取元素尺寸

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/a9a85ddaa3374012a7d193e4b09b98ab.png)

14. 案例4：动态渲染页面

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/2bef23c95f194bfebf327b59c24aa3ec.png)

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            * {
                margin: 0;
                padding: 0;
            }
            ul, ol, li {
                list-style: none;
            }
            .box {
                width: 600px;
                height: 400px;
                border: 3px solid pink;
                margin: 50px auto;
                display: flex;
                flex-direction: column;
            }
            .box > ul {
                height: 60px;
                display: flex;
            }
            .box > ul > li {
                flex: 1;
                color: #fff;
                background-color: skyblue;
                font-size: 30px;
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: pointer;
            }
            .box > ul > li.active {
                background-color: orange;
            }
    
            .box > ol {
                flex: 1;
                position: relative;
            }
    
            .box > ol > li {
                width: 100%;
                height: 100%;
                background-color: purple;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #fff;
                font-size: 100px;
    
                position: absolute;
                left: 0;
                top: 0;
    
                display: none;
            }
    
            .box > ol > li.active {
                display: flex;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <ul>
                <li class="active">1</li>
                <li>2</li>
                <li>3</li>
            </ul>
            <ol>
                <li class="active">1</li>
                <li>2</li>
                <li>3</li>
            </ol>
        </div>
    
        <script>
            // 1. 获取元素
            var btns = document.querySelectorAll('ul > li')
            var tabs = document.querySelectorAll('ol > li')
    
            // 2. 给btns里面所有按钮添加点击事件
            btns.forEach(function(item, index){
                item.onclick = function(){
                    // 2.1 给btns和tabs里面所有的内容取消 active 类名
                    btns.forEach(function(t, i){
                        t.className = ''
                        tabs[i].className = ''
                    })
    
                    // 2.2 当前点击的按钮和索引对应的盒子添加active类名
                    item.className = 'active'
                    tabs[index].className = 'active'
                }
            })
        </script>
    </body>
    </html>
    ```

### 1.17 事件

- 前端通过代码的方式和页面中的某些内容做好一个约定

- 用户触发指定行为的时候，就会执行代码

- 事件绑定

  - 事件绑定的三要素
    1. 事件源：和谁做好约定
    2. 事件类型：约定一个什么行为
    3. 事件处理函数：当用户触发该行为的时候，执行什么代码
  - 语法：`事件源.on事件类型 = 事件处理函数`

- 事件类型

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/954a6083e71041a59012a2c83611c60d.png)

- 事件对象

  - 当事件触发的时候，一个描述该事件信息的对象数据类型

  - 直接在事件处理函数接收形参就是事件对象了

    ```js
    div.onclick = function(e){
    	console.log(e)
    }
    ```

- 事件对象内的信息

  - 鼠标事件

    - 坐标信息
      1. offsetX和offsetY：相对于触发事件的元素的位置
      2. clientX和clientY：相对于浏览器可视窗口的位置
      3. pageX和pageY：相对于页面文档流的位置

  - 键盘事件

    - 键盘编码：`事件对象.keyCode`

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/3c31c2bf9f8e4752b0be3c6c0a04a3c5.png)

- 案例：鼠标跟随

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
          img {
              width: 50px;
              height: 50px;
              position: fixed;
              left: 0;
              top: 0;
          }
      </style>
  </head>
  <body>
      <img src="./pic/棒棒糖.png" alt="">
      <script>
          var imgBox = document.querySelector('img')
          //  给 document 绑定一个鼠标移动事件
          document.onmousemove = function(e) {
              // 拿到光标相对于窗口的坐标点位
              var x = e.clientX
              var y = e.clientY
              // 把 x 和 y 的值复制给img标签的left和top样式
              imgBox.style.left = x + 5 + 'px'
              imgBox.style.top = y + 5 + 'px'
          }
      </script>
  </body>
  </html>
  ```

- 事件传播 ![在这里插入图片描述](https://img-blog.csdnimg.cn/36046364733a4f7d978cc408868577df.png)

  - 浏览器的响应事件的机制

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20796fc4cab34d2cac4ed3602cbf34ab.png)

    - 浏览器窗口最先知道事件的发生
    - 捕获阶段：从window按照结构子级的顺序传递到目标
    - 目标阶段：准确触发事件的元素接收到行为
    - 冒泡阶段：从目标按照结构父级的顺序传递到window
    - 本次事件传播结束
    - **浏览器的传播机制默认都是在冒泡阶段触发事件的**

  - 阻止事件传播

    - `事件对象.stopPropagation()`

    - 代码

      ```js
      inner.onclick = function(e){
      	e.stopProgation()
      	console.log('aaa')
      }
      ```

  - 事件委托

    - 利用事件冒泡的机制，把自己的事件委托给结构父级中的某一层

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/7e228fbd56824d93b62d0af1c3e54464.png)

    - 通过事件对象的 `e.taget` 拿到点击的对象

      ```js
      ul.onclick = function(e){
      	if(e.target.tagName === 'LI'){
      		console.log('你点击的是li')
      	}
      }
      ```

    - 上述代码通过识别点击对象的tagName，设置仅对li对象的点击响应，而不对其父对象ul响应

- 案例：轮播图

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/82310e630c4e48bbb16ebb1464dba2fa.png)

  - 需求：

    - 点击左按钮，当前这一张消失，上一张出现
    - 点击右按钮，当前这一张消失，下一张出现
    - 点击焦点按钮，当前这一张消失，某一张出现

  - 代码

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            * {
                margin: 0;
                padding: 0;
            }
    
            ul,
            ol,
            li {
                list-style: none;
            }
    
            img {
                width: 100%;
                height: 100%;
                display: block;
            }
    
            .banner {
                width: 100%;
                height: 500px;
                position: relative;
                margin: 50px 0;
            }
    
            .banner>ul {
                width: 100%;
                height: 100%;
                position: relative;
            }
    
            .banner>ul>li {
                width: 100%;
                height: 100%;
                position: absolute;
                left: 0;
                top: 0;
    
                opacity: 0;
                transition: opacity .5s linear
            }
    
            .banner>ul>li.active {
                opacity: 1;
            }
    
            .banner>ol {
                width: 200px;
                height: 30px;
                position: absolute;
                left: 30px;
                bottom: 30px;
                background-color: rgba(0, 0, 0, 0.5);
    
                display: flex;
                justify-content: space-around;
                align-items: center;
                border-radius: 15px;
            }
    
            .banner>ol>li {
                width: 20px;
                height: 20px;
                background-color: #fff;
                border-radius: 50%;
                cursor: pointer;
            }
    
            .banner>ol>li.active {
                background-color: orange;
            }
    
            .banner>div {
                width: 40px;
                height: 60px;
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                background-color: rgba(0, 0, 0, 0.5);
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 30px;
                color: #fff;
                cursor: pointer;
            }
    
            .banner>div.left {
                left: 0;
            }
    
            .banner>div.right {
                right: 0;
            }
        </style>
    </head>
    
    <body>
        <div class="banner">
            <!-- 图片区域 -->
            <ul>
                <li class="active"><img src="./pic/lb-1.jpg" alt=""></li>
                <li><img src="./pic/lb-2.jpg" alt=""></li>
                <li><img src="./pic/lb-3.jpg" alt=""></li>
                <li><img src="./pic/lb-4.jpg" alt=""></li>
            </ul>
    
            <!-- 焦点区域 -->
            <ol>
                <li data-i="0" data-name="point" class="active"></li>
                <li data-i="1" data-name="point"></li>
                <li data-i="2" data-name="point"></li>
                <li data-i="3" data-name="point"></li>
            </ol>
    
            <!-- 左右切换按钮 -->
            <div class="left">&lt;</div>
            <div class="right">&gt;</div>
        </div>
    
        <script>
            // 获取到所有承载图片的li喝所有承载焦点的li
            var imgs = document.querySelectorAll('ul>li')
            var points = document.querySelectorAll('ol>li')
            var banner = document.querySelector('.banner')
            // 准备一个变量，表示当前是第几张，默认是0，因为默认显示的是索引第0张
            var index = 0
            // 书写一个切换一张的函数
            function changeOne(type) {
                /*
                    约定：
                        1. 参数为true，我们切换下一张
                        2. 参数为false，我们切换上一张
                        3. 参数为数字，我们切换到指定索引的那一张
                */
                //    1. 让当前这一张消失
                imgs[index].className = ''
                points[index].className = ''
    
                // 2. 根据type传递啦id参数，来切换index的值
                if (type === true) {
                    index++
                } else if (type === false) {
                    index--
                } else {
                    index = type
                }
                // 判定一下 index 的边界值
                if (index >= imgs.length) {
                    index = 0
                }
                if (index < 0) {
                    index = imgs.length - 1
                }
                // 3. 让改变后的这一张显示出来
                imgs[index].className = 'active'
                points[index].className = 'active'
            }
            // 给轮播图区域盒子绑定点击事件
            banner.onclick = function (e) {
                // console.log('点击事件');
    
                // 判断点击的是左按钮
                if (e.target.className === 'left') {
                    console.log('点击的是左按钮');
                    // 切换上一张，调用changeOne 方法传递参数为false
                    changeOne(false)
                }
    
                // 判断点击的是右按钮
                if (e.target.className === 'right') {
                    console.log('点击的是右按钮');
                    // 切换下一张，调用changeOne方法传递参数为true
                    changeOne(true)
                }
    
                // 判断点击的是焦点盒子
                if (e.target.dataset.name === 'point'){
                    console.log('点击的是焦点盒子');
                    // 拿到自己身上记录的索引
                    var i = e.target.dataset.i - 0
                    // 切换某一张，调用changeOne方法传递参数为要切换的索引
                    changeOne(i)
                }
            }
    
            // 自动切换功能
            setInterval(function(){
                changeOne(true)
            }, 3000)
        </script>
    </body>
    
    </html>
    ```

## 2. 面向对象

1. 了解面向对象
   - 面向对象是我们的一种开发方式
   - 面向过程：一种关注过程的开发方式
     - 在开发过程中，我们要关注每一个细节，步骤，顺序
   - 面向对象：一种面向对象的开发方式
     - 在开发过程中，我们看看有没有一个对象能帮我们完成任务
   - 面向对象的核心：高内聚，低耦合

2. 创建对象的方式

   1. 字面量方式创建对象

      - `var obj = {...}`

      - 可以后期动态添加

        ```js
        var obj = {
        	name: 'Jack',
        	age: 18,
        	sayHi: function () {console.log('hello world')}
        }
        ```

   2. 内置构造函数创建对象

      - `var obj = new Object()`

      - 可以后期动态添加

        ```js
        var obj = new Object()
        obj.name = 'Jack'
        obj.age = 18
        obj.sayHi = function () {console.log('hello world')}
        ```

   3. 工厂函数创建对象

      1. 制造一个工厂函数

      2. 使用工厂函数创建对象

         ```js
         function createObj(name, age, sayHi) {
             var obj = {}
         
             obj.name = name
             obj.age = age
             obj.sayHi = sayHi
         
             return obj
         }
         
         var s1 = createObj('a', 1, function(){return 1})
         var s2 = createObj('b', 2, function(){return 2})
         ```

   4. 自定义构造函数创建对象

      1. 制造一个自定义的构造函数
      2. 使用自定义的构造函数去创建对象

      - 构造函数会自动创建对象，自动返回这个对象，我们只需要手动向里面添加内容就可以了

      - 构造函数在使用的时候，需要和new关键字连用，如果不连用，那么没有意义

        ```js
        function createObj() {
        	this.name = 'Jack'
        	this.age = 18
        	this.sayHi = function () {console.log("11")}
        }
        ```

      - 每一个对象可能类似，但是内容不太一样

        - 构造函数

        - 可以批量生产对象

        - 可以像函数一样传递参数，可以给每一个对象添加一些不同的内容

          ```js
          function createObj2() {
              this.name = 'Jack'
              this.age = 18
              this.sayHi = function () { console.log("11") }
          }
          
          var obj1 = new createObj2()
          var obj2 = new createObj2()
          ```

3. 构造函数的使用

   1. 构造函数和普通函数没有区别
      - 只不过在调用的时候和 new 关键字连用
   2. 书写构造函数，函数名首字母大写
   3. 调用的时候，需要和new关键字联用
   4. 调用构造函数的时候，如果不需要传递参数，可以不写最后的小括号
   5. 构造函数内部，不要随便写return
      - 如果在函数体中写了 `return 基本数据类型` ，则该return不起作用
      - 如果return 的是 复杂数据类型，则构造函数白写（数组，函数，时间对象）

4. 构造函数的不合理

   - 当你在构造函数体内书写方法的时候
     - 你需要向对象上添加方法的时候
     - 只要创建一次对象（new一次），就会有一个函数在占用空间
     - 函数无法被重复利用

5. 原型 prototype

   - 定义：每一个函数天生自带一个属性，叫做prototype，是一个 **对象**
   - 构造函数也是函数，也会有这个自带的空间 prototype
   - 既然 prototype是一个对象，我们就可以使用对象操作的语法，向里面添加一些内容

6. 对象

   - 定义：每一个对象，在你访问他的成员的时候，如果自己没有这个属性，会自动的去所属构造函数的prototype上查找
   - 自定义构造函数创建的对象也是对象，当你访问某一个成员的时候
     - 如果没有，也会自动取所属构造函数的原型上查找
     - 哪一个构造函数创建的对象，这个对象就属于哪一个构造函数
     - 因为构造函数在创建对象的过程，叫做 实例化 过程，创建出来的对象家做这个构造函数的一个 实例化对象
   - **理解：函数的原型可以用来定义类方法，该方法每一个实例都可以使用，渐少资源的浪费**

7. 面向对象开发

   - 选项卡：

     1. 书写一个构造函数
     2. 创建一个能够完成选项卡的对象
        - 属性1：选项卡中能够点击的按钮
        - 属性2：选项卡中用于切换的盒子
        - 方法：控制点击的按钮添加点击事件，给盒子进行切换操作
     3. 使用构造函数创建一个选项卡对象

   - 代码

     ```html
     <!DOCTYPE html>
     <html lang="en">
     
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Document</title>
         <style>
             * {
                 margin: 0;
                 padding: 0;
             }
     
             ul,
             ol,
             li {
                 list-style: none;
             }
     
             .tab {
                 width: 600px;
                 height: 400px;
                 border: 10px solid #333;
     
                 display: flex;
                 flex-direction: column;
             }
     
             ul {
                 height: 60px;
                 display: flex;
             }
     
             ul>li {
                 flex: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 font-size: 40px;
                 color: #fff;
                 background-color: skyblue;
                 cursor: pointer;
             }
     
             ul>li.active {
                 background-color: orange;
             }
     
             ol {
                 flex: 1;
                 position: relative;
             }
     
             ol>li {
                 position: absolute;
                 left: 0;
                 top: 0;
                 width: 100%;
                 height: 100%;
                 font-size: 100px;
                 color: #fff;
                 background-color: purple;
                 display: none;
                 justify-content: center;
                 align-items: center;
             }
     
             ol>li.active {
                 display: flex;
             }
         </style>
     </head>
     
     <body>
         <div class="tab" id="box">
             <ul>
                 <li class="active">1</li>
                 <li>2</li>
                 <li>3</li>
             </ul>
             <ol>
                 <li class="active">1</li>
                 <li>2</li>
                 <li>3</li>
             </ol>
         </div>
     
         <div class="tab" id="box2">
             <ul>
                 <li class="active">1</li>
                 <li>2</li>
                 <li>3</li>
                 <li>4</li>
             </ul>
             <ol>
                 <li class="active">1</li>
                 <li>2</li>
                 <li>3</li>
                 <li>4</li>
             </ol>
         </div>
     
         <script>
             function Tabs(ele) {
                 // 范围
                 this.ele = document.querySelector(ele)
                 // 在范围内找到所有可以点击的盒子
                 this.btns = this.ele.querySelectorAll('ul > li')
                 // 在范围内找到所有需要切换显示的盒子
                 this.tabs = this.ele.querySelectorAll('ol > li')
             }
             // 原型上书写方法
             Tabs.prototype.change = function () {
                 // 保存一下当前的实例，在下面的函数中需要使用该实例的变量
                 var current_tab = this
     
                 for (var i = 0; i < current_tab.btns.length; i++) {
                     // 给每一个按钮设置index的索引
                     this.btns[i].setAttribute('index', i)
                     // 去掉所有btn和tab的active标记
                     this.btns[i].addEventListener('click', function () {
                         for (var j = 0; j < current_tab.btns.length; j++) {
                             current_tab.btns[j].className = ''
                             current_tab.tabs[j].className = ''
                         }
                         // 当前点击的这个li有active类名
                         this.className = 'active'
                         // 同时，对应的tab索引的li也同样有active类名
                         var index = this.getAttribute('index') - 0
                         current_tab.tabs[index].className = 'active'
                     })
                 }
             }
             var t = new Tabs('#box')
             t.change()
             var t2 = new Tabs('#box2')
             t2.change()
         </script>
     </body>
     
     </html>
     ```

## 3. 原型和原型链

1. 原型

   - 问题：在构造函数体内直接向实例对象添加方法，这个行为并不好

   - 原因：每次创建实例的时候，都会创建一个函数数据类型，浪费存储空间

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/ef5aaa2669a04fe6a5d7d21494889308.png)

2. 概念：

   - 每一个构造函数天生自带一个 prototype属性，是一个对象数据类型

   - 当函数被书写完毕以后，就会有 prototype 出现

   - **我的理解：** prototype相当于定义类变量和类方法的位置

   - 每一个对象天生自带一个属性 \__proto__，指向所属构造函数（类）的prototype

   - 当你访问对象的成员的时候，首先在自己身上查找，如果没有，自动去到 \__proto__ 上查找 

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/778ef19521064cf693f354e2bcfd2680.png)

3. 原型链

   - 问题1：实例对象上的 `__proto__` 指向谁？

     - 指向所属构造函数的 prototype

   - 问题2：`Person.prototype` 的 `__proto__` 指向谁？

     - 指向内置构造函数Object.prototype

   - 问题3：`Person` 的 `__proto__` 指向谁？

     - 指向内置构造函数Function.prototype

   - 问题4：`Object.prototype` 的 `__proto__` 指向谁？

     - ~~指向内置构造函数Object.prototype~~
     - **注意：Object.prototype 在JS内叫做顶级原型，不再有 `__proto__` **
     - 指向null

   - 问题5：`Object` 的 `__proto__` 指向谁？

     - Object是一个内置构造函数（类）、函数、对象
     - 在JS内，所有的函数都是属于内置构造函数（类） Function 的实例
     - 所以，Object也是Function的实例
     - 所以，指向 Function.prototype

   - 问题6：`Function.protptype`的  `__proto__`  指向谁？

     - Function.prototype 也是一个对象数据实例
     - 只要是对象数据类型都是 Object 的实例
     - 指向 Object.prototype

   - 问题7：`Function` 的 `__proto__` 指向谁？

     - Function 是一个内置函数（类）、函数
     - 在JS内，所有的函数都是属于内置构造函数Function的实例
     - Function 自己是自己的构造函数、也是自己的实例对象
     - 所以，指向 Function.prototype

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/c6f74802e8504b0c8a2477cd84dc5cb9.png)

   - 原型链：

     - 用 `__proto__` 串联起来的对象链状结构
     - **注意：使用 `__proto__` 串联**
     - 每一个对象数据类型都有一个属于自己的原型链
     - 作用：为了访问对象成员

   - 对象访问机制

     - 当你需要访问对象的成员的时候
     - 首先在自己身上查找，如果有则直接使用
     - 否则，在 `__proto__` 上查找
     - 再否则，顺着原型链的 `__proto__` 查找
     - 直到Object.prototype 都没有，则返回undefined

## 4. ES6

1. 定义变量

   - 以前：var
   - 新增：
     - let：定义变量
     - const：定义常量（特殊的变量）
   - var与let/const的区别：
     - var会进行预解析，let/const不会
       - 预解析可以使得变量在定义之前使用，如果是let的话，会报错
     - var可以声明两个重名的变量，let/const不能
     - var没有块级作用域，let/const有
       - 任何一个可以执行代码段的 `{}` 都会限制该变量的使用范围
   - let与const的区别
     - let可以定义变量的时候不进行赋值，const则必须赋值
     - let定义的变量可以被修改，const则不可以

2. 箭头函数

   - 是在ES6语法中对函数表达式的简写

   - 对于声明式函数不能使用

   - 在某些规则上又和以前的函数有一些不一样

   - 什么是函数表达式

     - 又叫匿名函数

     - 也就是我们不需要单独定义函数，直接使用的位置

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/c09f0c759e744d42ac1ba5862dbed31f.png)

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/fcfb316ae74541dda87568c16dd7e4cb.png)

   - 箭头函数的特殊之处

     1. 当你的形参只有一个的时候可以不写 ()

        `var f1 = a => {console.log('a', a)}`

     2. 当你的代码只有一句话的时候，可以不写 {}，直接返回该句话的结果

        `var f1  = (a, b) => a + b`

     3. 箭头函数内没有arguments

     4. 箭头函数内没有this，箭头函数中的this就是外部作用域的this

3. 函数参数默认值

   - 函数在定义的时候，可以直接给形参设置一个默认值
   - 当没有传递实参的时候，就使用默认值
   - 当传递了实参，就使用传递的实参
   - **普通函数可以使用，箭头函数也可以使用**
   - `function fn(a=100, b=200){...}`
   - `var s = (a=100, b=200) => {...}`

4. 结构赋值

   - 快速从对象或者数组中获取成员

   - 结构赋值分成两种

     - 数组的结构赋值

       ![在这里插入图片描述](E:\typora_pics_savepath\eac2ba045ea34b21919ab54359678a49.png)

     - 对象的结构赋值

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/8423f558e90b4db39a8e2f85ae83d9ce.png)

       - 解构的时候，可以同时解构多个：比如 `let {name, age} = obj`
       - 如果没有该变量名，则为undefined
       - 起别名：`var {name: n} = obj`，把obj.name赋值给n

5. 模板字符串

   - 其实就是ES6内新增的定义字符串的方式

   - 以前：

     - `var str = '...'`
     - `var str = "..."`

   - 现在：

     ```js
     var str = `...`
     ```

   - 区别：

     1. 可以换行书写，保留换行
     2. 可以直接在字符串内解析变量，形式：`${变量}`

6. 展开运算符

   - 就是点点点：`...`

   - 作用：展开数组的[]，或者展开对象的{}

   - `console.log(...arr)`

   - 作用

     1. 合并数组：`arr = [...arr1, ...arr2, ...arrn]`

     2. 给函数传递参数（类似python的*）

        展开数组、展开对象

        ```js
        var obj = {name: 'aa', age: 17}
        var obj2 = {
        	'gender': 'male',
        	...obj
        }
        ```

     3. 注意：展开对象时的顺序问题，需要考虑同名成员的取值的覆盖

7. 类语法

   - 过去新增类的方法：

     ```js
     function Person(name, age){
         this.name = name
         this.age = age
     }
     Person.prototype.sayHi = function () {console.log('hello world')}
     ```

   - 问题：

     1. 构造函数本质还是一个函数，可以不和new关键字联动（*虽然返回值为undefined*）
     2. 原型上的方法跟定义分开来写了（目的都是为了给实例使用）

   - 现在类的书写：

     ```js
     class Person {
         constructor(name, age){
             this.name = name
             this.age = age
         }
         sayHi(){
              console.log('hello world')
         }
         // 书写静态属性和方法
         static a = 100
         static go (){console.log('running')}
     }
     ```
     
   - 注意：必须和new关键字联用，否则会报错

   - 以前：书写静态属性和方法

     ```js
     Person.a = 100
     Person.go = function(){console.log('run')}
     ```

   - 使用静态属性和方法

     ```js
     Person.go()
     console.log(Person.a)
     ```

## 5. ajax

1. 前后端交互

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/d413225cf17b434cb5fb05d18f70d124.png)

2. 接口文档

   - 请求地址
   - 请求方式
   - 携带参数
   - 响应数据

3. 交互方式：ajax

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/6bde480ff8e146dd8eedeac9865d5034.png)

   - 如何拿到后端返回的信息：
     - xhr.responseText
   - 解析json格式的字符串
     - var res = JSON.parse(xhr.responseText)
     - 这里处理后得到 **对象数据类型** （字典）

4. 请求方式

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/efe2f80b42f546008af98f9269f9e9f2.png)

   - get：直接在地址后面拼接参数

     `xxx?name=aa&age=18`

   - post：请求体写在send的括号中

     `xhr.send(name=aa&age=18)`

     - 需要携带参数时还要有特殊说明
     - 语法：`xhr.setRequestHeader('content-type', 你传递参数的格式)`
     - `xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded')`

5. 登录案例

   - 需求分析

     1. 什么时候进行请求发送？

        点击登录按钮的时候，需要给form标签绑定一个表单提交事件

     2. 需要拿到哪些信息？

        用户名和密码

     3. 需要如何发送给后端？

        按照接口文档的规范进行发送

     4. 请求完成以后，我们需要做什么？

        根据后端返回的信息，进行一些后续的操作；如果后端返回的信息是登录成功，那么我们进行页面跳转；如果后端返回的是登录失败，那么我们提示用户错误

   













学到P251


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045/`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome/`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822/`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj/`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_/`
- :potato: 我的豆瓣：`https://www.douban.com/people/lyjun_/`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
