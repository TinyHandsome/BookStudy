# 千锋JavaScript学习笔记

[TOC]

## 写在前面

- 封面 | 摘要

  ![封面](https://img2022.cnblogs.com/blog/1589204/202209/1589204-20220905095739193-1849832512.jpg)

  ```
  js+jQuery+Node.js学习笔记
  ```

- 学习链接：[千锋HTML5前端开发教程1000集](https://www.bilibili.com/video/BV17z4y1D7Yj)：`[184集: 286集]，共103集`

- 感想

  1. [20221008] node.js 这部分讲的真的很难顶，真想直接跳到vue。这个老师思想跳跃很大，讲课基于自己而不是基于受众。且不提我，很多老师体到的东西屏幕里的学生都很懵。前面说着说着就说到一些超纲知识点，说了又不详解，只会说后面会讲，会面会讲就不要体到前面，很多知识点之间跳跃性很大，缺乏逻辑性串讲。
  2. [20221010] 感觉node.js的主讲老师，很多常见的函数api都记不住，动不动就要查，跟着敲代码都要改来改去，脑阔痛。
  2. [20221017] 讲到cors的时候，老师本来想要直接复制代码，还说：“如果这段代码你没有看懂，说明前面的你没有认真听。” 我：？？？直接上PUA了可还行。
  2. [20221020] 讲fs.stat，这老师的基础真是一言难尽，如果不知道函数的使用和功能，你查也行啊，总不能蒙吧。。。
  2. [20221025] 讲express，中间件栈？明明是队列，自己编了个名字可还行，讲得乱七八糟、不知所云。我的评价是：稀烂。不就是路由匹配的问题嘛？加个next可以使得后面的路由继续被匹配到，这么简单的东西我一看就知道要说啥，真是服了。主动增加学习难度了这是。。。

- 摘抄

  1. 父元素设置 `position: relative`；子元素设置 `position: absolute; left: 50%; transform: translateX(-50%)`，可以实现内容的居中显示
  1. 激活当前元素，取消其他兄弟元素的激活：`$(this).addClass('active').siblings().removeClass('active')`
  1. 直接启动http服务器：`npx http-server -p 9000`
  1. 启动node.js服务器：`nodemon cors.js`、`node cors.js`

- 学习时遇到的问题

  1. [CSS中的position:relative理解](https://blog.csdn.net/gamenoover/article/details/90614014)
  1. [『前端大白话』之 “flex:1”](https://juejin.cn/post/6969797532687794183)
  1. [nvm-windows安装教程](https://www.jianshu.com/p/13c0b3ca7c71)
  1. [查找第三方模块](npmjs.com)
  1. [npm 全局安装与本地安装、开发依赖和生产依赖](https://blog.csdn.net/qq_43456781/article/details/120077136)

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

## 6. jQuery

1. 一个大型的简单的第三方类库

2. DOM操作进行封装

   - 获取DOM节点
   - 操作节点文本、样式、类名、属性、尺寸、偏移量、事件
   - 节点动画操作、ajax封装

3. 体验jQuery

   - 当你引入jQuery文件以后，会在全局暴露两个变量名
     - `$`
     - `jQuery`
     - 上述两个变量是一个意思

4. jQuery的选择器：`$('选择器')`

   - 注意：不管使用任何选择器，获取到的元素都是一个元素的集合

   - 代码

     ```html
     <body>
         <ul>
             <li class="a">1</li>
             <li>2</li>
             <li class="b">3</li>
             <li>4</li>
             <li>5</li>
             <li class="a">6</li>
             <li>7</li>
             <li id="box">8</li>
         </ul>
         <script src="../9-package/jquery-3.6.1.js"></script>
         <script>
             // console.log($);
             // console.log(jQuery);
     
             // id选择器
             console.log($('#box'));
     
             // 类名选择器
             console.log($('.a'))
     
             // 标签名选择器
             console.log($('li'));
     
             // 结构选择器
             console.log($('li:nth-child(odd)'));
             console.log($('li:nth-child(even'));
         </script>
     
     </body>
     </html>
     ```

5. jQuery的筛选器：`$('选择器').筛选器名称()`

   - first()：选到结果列表的第一个
   - last()：选到结果列表的最后一个
   - eq(索引)：拿到的是第索引的元素（索引从0开始，依次+1）
   - next()：拿到当前元素的下一个元素
   - nextAll()：拿到当前元素下面所有的元素
   - prev()：拿到当前元素的前一个元素
   - prevAll()：拿到当前元素的前面所有元素
   - parent()：拿到当前元素的父元素
   - parents()：获取到的是该元素的所有父级元素，逐层获取，直到获取html标签为止
   - siblings()：拿到该元素的所有兄弟元素
   - find()：找到该元素的所有后代元素中，满足选择器要求的元素（可以下钻到所有层）

6. jQuery操作文本内容：

   - html()：等价于原生JS的innerHTML，可以获取和设置内容

     - 注意：可以识别并解析html结构字符串

     - 获取和设置

       ```html
       console.log($('div').html())
       $('div').html('<h2>aaa</h2>')
       ```

   - text()：等价于原生JS的innerText

     - 注意：不可以识别并解析html结构字符串
     - 获取和设置大体如上

   - val()

     - 等价于原生JS的value
     - 作用：获取和设置该表单元素的 value 值

7. jQuery操作类名

   1. addClass()
      - 语法：元素集合.addClass(类名)
      - 添加类名
   2. removeClass()
      - 语法：元素集合.removeClass(类名)
      - 删除类名
   3. toggleClass()
      - 语法：元素集合.toggleClass(类名)
      - 切换类名：如果本身有这个类名，就是删除；如果本身没有这个类名，就是添加

8. jQuery操作元素样式

   - 只有一个方法：css()
     1. css获取样式
        - 注意：可以获取到元素的行内样式，也可以获取到元素的非行内样式
        - 语法：元素集合.css(你要获取的样式名称)
        - 返回：该样式的样式值
        - 例如：`console.log($('div').css('width'))`

     2. css设置样式
        - 注意：当你需要给一个元素设置样式值为px单位的时候，可以省略不写
        - 语法：元素集合.css(样式名，样式值)
        - 例如：`$('div').css('width', '300px')`

     3. css 批量设置样式

        - 语法：元素集合.css({ 你所有需要设置的样式 })

        - 我觉得：里面的值可以是字符串也可以不是

          ```js
          $('div').css({
          	width: 260,
          	height: 320,
          	opacity: 0.68,
          	'background-color': 'purple'
          })
          ```

9. jQuery操作属性

   1. attr()
      - 可以进行设置和获取元素的属性
      - 注意：**一般**用于操作元素的**自定义属性**
      - 注意：attr操作的所有属性都会直接出现在元素的标签上
      - 获取：
        - 语法：元素.attr(你要获取的属性名)
        - 返回值：该属性名对应的属性值
      - 设置：
        - 语法：元素.attr(属性名，属性值)
   2. removeAttr()
      - 对元素的属性进行删除操作
      - 语法：元素集合.removeAttr(属性名)
      - attr和removeAttr都可以操作自定义属性和原生属性，但是不建议操作原生属性
   3. prop()
      - 可以获取和设置元素的属性
      - 注意：
        - 当prop设置元素的原生属性时，会直接响应在元素标签身上
        - 当prop设置元素自定义属性时，不会直接响应在元素标签身上，而是会响应在元素对象身上
      - 注意：prop方法不能获取元素标签身上的自定义属性，只能获取到prop方法自己设置的自定义属性
      - prop设置
        - 语法：元素集合.prop(属性名，属性值)
      - prop获取
        - 语法：元素集合.prop(属性名)
        - 返回：该属性对应的值
   4. removeProp()
      - 用来哦删除元素属性的方法
      - 注意：
        - 不能删除原生属性
        - 只能删除由prop方法设置的自定义属性
      - 语法：元素集合.removeProp(属性名)

10. 获取元素尺寸

    1. width() 和 height()
       - 获取到的就是元素内容区域的尺寸
    2. innerWidth() 和 innerHeight()
       - 上述+padding后的尺寸
    3. outerWidth() 和 outerHeight()
       - 上述+border后的尺寸
    4. outerWidth(true) 和 outerHeight(true)
       - 上述+margin后的尺寸
    5. 注意：
       1. 不管该元素是否隐藏，都能获取到该元素的值
       2. 不管盒子模型是什么状态，拿到的尺寸区域不变，尺寸可能变，比如使用怪异盒模型

11. 元素的偏移量

    1. offset()
       - 获取元素相对于页面左上角的坐标位置（**绝对偏移**）
       - 注意：返回值是一个对象数据类型，`{top:yyy, left:xxx}`
    2. position()
       - 获取的就是元素的定位位置（相对位置）
       - 注意：如果你设置的是right和bottom，会自动帮你换算成left和top的值

12. jQuery绑定事件

    1. on()

       1. 基础绑定事件

          - 语法：元素集合.on(‘事件类型’, 事件处理函数)
          - `$('div').on('click', function(){console.log('我是div的点击事件')})`

       2. 事件委托绑定事件

          - 语法：元素集合.on(‘事件类型’, 选择器, 事件处理函数)

          - 把事件绑定给div元素，当你在div内的p元素触发事件的时候，执行处理函数

            ```js
            // 事件委托，把p元素的事件委托给了div元素来绑定，点击div不触发，点击p才会触发
            $('div').on('click', 'p', function(){console.log('我是事件委托形式的事件')})
            ```

       3. 批量绑定事件

          - 语法：元素集合.on({ 事件类型1: 处理函数, 事件类型2: 处理函数 })

          - 注意：不能进行事件委托了

            ```js
            $('div').on({
            	click: function(){console.log('mouse click event')},
            	mouseover: function(){console.log('mouse over event')},
            	mouseout: function(){console.log('mouse out event')}
            })
            ```

    2. one()

       - 用来绑定事件，和on方法绑定事件的方式是一样的
       - 区别：one方法绑定的事件，**只能执行一次**

    3. hover()

       - 注意：jQuery里面一个特殊的事件

       - 语法：元素集合.hover(移入时触发的函数，移出时触发的函数)，当你只传递一个函数的时候，会在移入、移出都触发

         ```js
         $('div').hover(
         	function(){console.log('f1')},
         	function(){console.log('f2')}
         )
         ```

    4. 常用事件函数

       - jQuery把我们常用的一些事件，单独做成了事件函数，我们通过调用这些事件函数，来达到绑定事件的效果

       - click()、mouseover()、mouseout()、change()、…

         ```js
         $('div').click(function(){console.log('点击事件')})
         ```

13. 事件的解绑和触发

    1. off() 事件解绑

       1. 解绑全部事件函数

          - 语法：元素集合.off(事件类型)

            ```js
            // 会把div的click事件对应的所有事件处理函数全部移除
            $('div').off('click')
            ```

       2. 解绑指定的事件处理函数

          - 语法：元素集合.off(事件类型，要解绑的事件处理函数)

            ```js
            $('div').off('click', handlerB)
            ```

    2. trigger() 事件触发

       - 使用代码的方式，来触发事件

       - 语法：元素集合.trigger(事件类型)

       - 就会触发该元素的该事件

         ```js
         // 每1000ms触发一次div的click事件
         setInterval(function(){
         	$('div').trigger('click')
         }, 1000)
         ```

14. jQuery基本动画函数

    1. show()：显示
    2. hide()：隐藏
    3. toggle()：切换，隐藏和显示的切换

    - 对于上面三个运动函数，有共同的参数

      1. 表示运动时间
      2. 表示运动曲线
      3. 表示运动结束的回调函数

    - 样例

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
              div {
                  width: 500px;
                  height: 500px;
                  background-color: skyblue;
              }
          </style>
      </head>
      <body>
          <button>show</button>
          <button>hide</button>
          <button>toggle</button>
          <div></div>
          <script src="../9-package/jquery-3.6.1.js"></script>
          <script>
              $('button:nth-child(1)').click(function() {
                  // 执行 show 动画函数
                  $('div').show(1000, 'linear', function(){console.log('show finished')})
              })
              $('button:nth-child(2)').click(function() {
                  // 执行 hide 动画函数
                  $('div').hide(1000, 'linear', function(){console.log('hide finished')})
              })
              $('button:nth-child(3)').click(function() {
                  // 执行 toggle 动画函数
                  $('div').toggle(1000, 'linear', function(){console.log('toggle finished')})
              })
          </script>
      </body>
      </html>
      ```

15. jQuery折叠动画函数

    1. slideDown()：显示
    2. slideUp()：隐藏
    3. slideToggle()：切换

    - 就是展现形式不同，这个是窗帘上拉下放的形式，所以down是显示，而up是隐藏，其他的函数表现形式基本与上述基本动画一致

16. jQuery渐隐渐显动画函数

    1. fadeIn()：显示
    2. fadeOut()：隐藏
    3. fadeToggle()：切换
    4. fadeTo(运动时间，指定的透明度，运动曲线，回调函数)

    - 展现形式为：渐隐渐显（仅改变opacity），其他一样

17. jQuery综合动画函数

    - animate()

      1. 要运动的样式，以一个对象数据类型传递
      2. 运动时间
      3. 运动曲线
      4. 运动结束的回调函数

    - 注意：

      - 关于颜色相关的样式是不能运动的
      - 关于 transform 相关的样式是不能运动的

    - 样例

      ```js
      $('button').click(function(){
          $('div').animate({
              width: 500,
              height: 600，
              left: 300, 
              top: 200,
              'border-radius': '50%'
          }, 1000, 'linear', function(){console.log('运动结束')})
      })
      ```

18. jQuery结束动画函数

    动画需要结束的原因：如果快速触发动画多次会导致动画不断播放，而触发的动作已经结束了。

    1. stop()

       - 当任何一个元素执行了stop方法以后，就会立刻结束当前的所有运动，目前运动到什么位置，就停留在什么位置

       - 使用场景：利用结束动画书写动画函数；每一次触发的时候，都会把之前的动画停止下来，只执行本次最新的动画

         ```js
         $('div').stop().toggle(2000)
         ```

    2. finish()

       - 当任何一个元素，执行了finish方法后，会直接结束当前的所有运动，**直接去到动画的结束位置**
       - 使用场景：利用完成动画书写动画函数；每一次触发的时候，都会把之前的动画瞬间完成，只执行本次最新的动画

19. jQuery的ajax请求

    - 注意：
      - 因为发送ajax请求，不是操作DOM，不需要依赖选择器去获取到元素
      - 它的使用是直接依赖jQuery或者$变量来使用：`$.ajax({本次发送ajax的配置项})`
    - 配置项：
      - url：必填，请求地址
      - method：选填，默认是 GET，请求方式
      - data：选填，默认是 `''` ，表示携带给后端的参数
      - async：选填，默认是true，表示是否异步
      - success：选填，表示请求成功的回调函数
      - error：选填，表示请求失败的回调函数

## 7. Node.js

- 视频中笔记链接：https://lurongtao.gitee.io/felixbooks-gp19-node.js/

### 7.1 认识Node.js

1. Node.js is a JavaScript runtime built on Chrome’s V8 JavaScript engine.

2. 特性

   Node.js可以解析JS代码，**没有浏览器安全级别的限制**，提供很多系统级别的API

   - 文件的读写 File System

     ```js
     const fs = require('fs')
     
     fs.writeFile('./log.text', 'hello', (err, data) => {
         if (err) {
     
         }else{
             console.log('文件创建成功');
         }
     })
     ```

     运行上述代码：`node index.js`

   - 进程的管理 Process

     ```js
     function main(argv){
         console.log(argv);
     }
     
     main(process.argv)
     ```

     运行：`node process.js 1 2`

   - 网络通信 HTTP/HTTPS

     ```js
     const http = require('http')
     
     const server = http.createServer((request, response) => {
         let url = request.url
         response.write(url)
         response.end()
     })
     
     server.listen(8090, 'localhost', ()=>{
         console.log('localhost:8090');
     })
     ```

   - 。。。

3. Node相关工具

   1. nvm：Node Version Manager
   2. npm：Node Package Manager
   2. nrm：npm registry manager
   2. npx：npm package extention

### 7.2 NVM

- node.js的版本管理工具，windows不支持，需要安装其他的

    ```
    nvm-windows
    nodist
    ```

- 查看软件版本：`npm view node versions`
- 查看node版本：`node -v`
- 查看已安装的node版本：`nvm list`
- 切换node版本：`nvm user 14.15.0`
- 设置默认版本：`nvm alias default 14.15.0`


### 7.2 NPM

- 安装全局包：`npm install jquery -g(--global)`

- 全局安装包的目录：`C:\Users\用户\AppData\Roaming\npm\node_modules`

- 使用package.json可以实现本地包的安装：`npm install xxx --save-dev`
  - `--save`：可以替换为 `-S`
  - `--save-dev`：可以替换为 `-D`
  - 这里如果不加 `-dev` （开发环境），表示的是：将包安装在生产环境中，这样该包的信息会更新到 `package.json` 的 `dependencies` 里
  - 同理，开发环境的话，会把包的信息放到 `devDependencies` 键中
  - 最后使用 `node i` 来安装所有的依赖包
  - 查看特定名称的包：`npm list | grep gulp`
  - 安装 **生产** 环境下的包：`npm i --production`
  - 查看包有哪些版本：`npm view jquery versions`
  - 安装具体版本的包：`npm i jquery@2.2.4`
  - 安装某版本最高版本的包：`npm i jquery@2`
    - MAJOR：表示当前APR的主版本号，它的变化通常意味着APR的巨大的变化，比如体系结构的重新设计，API的重新设计等等，而且这种变化通常会导致APR版本的向前不兼容。 
    - MINOR：称之为APR的次版本号，它通常只反映了一些较大的更改，比如APR的API的增加等等，但是这些更改并不影响与旧版本源代码和二进制代码之间的兼容性。
    - PATCH通常称之为补丁版本，通常情况下如果只是对APR函数的修改而不影响API接口的话都会导致PATCH的变化。 目前为止APR的最高版本是1.2.2，最早遵循这种规则的版本号是0.9.0，不过在0.9.0之前，APR还推出了两个版本a8和a9。
      - 如果为奇数：则是不稳定的patch
      - 所以一般某个major的最高版本为偶数patch
    - `^`：该配置只锁定major版本号
    - `~`：锁定major和minor版本号
    - ` `：什么都不加是最严格的，指定版本号
    - `*`：最新版本
  - 清空npm缓存：`npm cache clean --force`

- loadsh介绍（与underscore是竞品）
  - chunck：数组的分割

- 自己发布包

  - 写一个函数 `myChunk()`

  - 暴露函数的接口：`module.exports = myChunk`

  - 调用：

    ```js
    const myChunk = require('./index.js')
    console.log(myChunk([4, 5, 6, 7]));
    ```

  - 发布

    ```bash
    // npm登录
    npm adduser
    // 查看源
    npm config get registry
    // 切换淘宝源（样例，实际要切回官方的源）
    npm config set registry https://registry.npm.taobao.org
    // 切回官方源
    npm config set registry https://registry.npmjs.org
    // 发布
    npm publish
    // 查看当前项目引用了哪些包
    npm ls
    // 卸载包
    npm unpublish --force
    // 引用包
    var hello = require('pg19-npm')
    hello.sayHello()
    ```

- `package.json` 描述文件

  - name：包名称
  - version：版本号
  - description：描述
  - main：暴露接口的主程序
  - scripts：执行时需要执行的脚本
  - respository：项目库（除了可以从npm官网安装，也可以通过github等安装）
  - keywords：关键词
  - author：作者
  - license：证数，一般为MIT
  - bugs：bug链接
  - homepage：主页地址

- npm脚本

  - npm允许在package.json文件里面，使用scripts字段定义脚本命令

  - npm运行package.json中的脚本

    ```sh
    npm run runjs
    ```

  - 如果脚本中有多个，使用 `&` 或 `&&` 连接

    - `&`：并行运行脚本
    - `&&`：串行运行脚本

  - 如果脚本名为 start 、 test 等特殊的名称时，可以省略 `run`：`npm test`

  - 获取package.json中的信息：

    `console.log(process.env.npm_package_config_env)`

    - 其中：congfig为第一级的key，env为二级key，取到的是config.env的值

    - 注意：如果直接获取的是config，是会报错的

    - 该方法只能通过配置package.json后运行里面的脚本才生效，如果直接运行对应的js会直接显示undefined

    - 在脚本内部也可以直接获取package.json的信息

      ```json
      "scripts": {
      	"build": "echo $npm_package_config_env"
      }
      ```

  - npm安装git上发布的包

    - `npm install git+https://git@xxx`
    - `npm install git+ssh://git@xxx`

- cross-env

  - windows不支持 `NODE_ENV=production` 的设置方式

  - 解决：cross-env使得可以使用单个命令，而不必担心为平台正确设置或使用环境变量。这个迷你的包（cross-env）能够提供一个设置环境变量的scripts，让你能够以Unix方式设置环境变量，然后再Windows上也能兼容运行

  - 安装：`npm install --save-dev cross-env`

  - 可以直接在脚本中设置环境变量的值，比如说

    ```json
    "scripts": {
    	"dev": "NODE_ENV=development gulp -f gulp.config.js",
    	"prod": "NODE_ENV=production gulp -f gulp.config.js"
    }
    ```

  - 如果需要使用cross-env

    ```json
    "scripts": {
    	"dev": "cross-env NODE_ENV=development gulp -f gulp.config.js",
    	"prod": "cross-env NODE_ENV=production gulp -f gulp.config.js"
    }
    ```


### 7.3 NRM

- npm的镜像源管理工具，有时候国外资源太慢，使用这个就可以快速地在npm源之间切换
- 安装：`npm install -g nrm`
- 查看可选的源：`nrm ls`
- 切换nrm：`nrm use taobao`
- 测试速度：`nrm test`

### 7.4 NPX

- npm从5.2开始增加了npx命令，如果没有自带，可以手动安装：`npm install -g npx`
- npx想要解决的主要问题，就是调用项目内部安装的模块
  - 需要使用某个库的时候，要么配置package.json后调用里面的脚本，或者进入到node_modules文件夹中找到对应的库，再运行
  - 比如：`gulp -v` 不行；但是 `npx gulp -v` 就可以了
  - 如果本地没有这个库，npx会自己下载，但不会在本地/全局安装。其实是安装在临时文件夹中，使用完后自动删除
- `npx --no-install http-server`：让npx强制使用本地模块，不下载远程模块，本地不存在就会报错
- `npx --ignore-existing http-server`：忽略本地的同名模块，强制安装使用远程模块

### 7.5 模块/包与CommonJS

1. 分类

   - 内置的模块
   - 第三方的模块
   - 自定义的模块

2. 浏览器是没有require对象的

3. 编写暴露的接口

   ```js
   module.exports = {
   	name,
   	age
   }
   ```

   - 可以通过这种方式，暴露多个接口

   - 也可以使用如下方式，其中exports是 `module.exports` 的引用

     ```js
     exports.name = name
     exports.age = age
     ```

### 7.6 常用内置模块

#### 1. url

- `url.parse(urlString[, parseQueryString[, slashesDenoteHost]])`：将链接解析为一连串的信息

  ```js
  const url = require('url')
  const urlString = 'https://www.baidu.com:443/path/index.html?id=2#tag=3'
  
  logger.debug(url.parse(urlString));
  
  // 输出
  Url {
    protocol: 'https:',
    slashes: true,
    auth: null,
    host: 'www.baidu.com:443',
    port: '443',
    hostname: 'www.baidu.com',
    hash: '#tag=3',
    search: '?id=2',
    query: 'id=2',
    pathname: '/path/index.html',
    path: '/path/index.html?id=2',
    href: 'https://www.baidu.com:443/path/index.html?id=2#tag=3'
  }
  ```

- `url.format(urlObject)`：将结构体的信息转为链接

  ```js
  logger.debug(url.format(
      {
          protocol: 'https:',
          slashes: true,
          auth: null,
          host: 'www.baidu.com:443',
          port: '443',
          hostname: 'www.baidu.com',
          hash: '#tag=3',
          search: '?id=2',
          query: 'id=2',
          pathname: '/path/index.html',
          path: '/path/index.html?id=2',
          href: 'https://www.baidu.com:443/path/index.html?id=2#tag=3'
      }
  ))
  
  // 输出
  https://www.baidu.com:443/path/index.html?id=2#tag=3
  ```

- `url.resolve(from, to)`：实现路径的拼接，前向后向都可以

  ```js
  logger.debug(url.resolve('http://www.abc.com/a', '/b'))
  logger.debug(url.resolve('http://www.abc.com/a', '../'))
  
  // 输出
  http://www.abc.com/b
  http://www.abc.com/
  ```

- `URLSearchParams`：解析url之后得到数据体，然后获取对应的search（*search: '?id=2',*）

  ```js
  const urlParams = new URLSearchParams(url.parse(urlString).search)
  logger.debug(urlParams);
  
  // 输出
  URLSearchParams { 'id' => '2' }
  ```

#### 2. querystring

- `querystring.parse(str[, sep[, eq[, options]]])`：参数的解析，将url中的参数部分解析为数据体（对象）

  ```js
  const querystring = require('querystring')
  var qs = 'x=3&y=4'
  var parsed = querystring.parse(qs)
  console.log(parsed)
  
  // 输出
  [Object: null prototype] { x: '3', y: '4' }
  ```

- `querystring.stringify(obj[, sep[, eq[, options]]])`：将数据体中的参数和值解析为url的参数

  ```js
  const querystring = require('querystring')
  var qo = {
    x: 3,
    y: 4
  }
  var parsed = querystring.stringify(qo)
  console.log(parsed)
  
  // 输出
  x=3&y=4
  ```

- `querystring.escape(str)`：对url的参数进行编码

  ```js
  const querystring = require('querystring')
  var str = 'id=3&city=北京&url=https://www.baidu.com'
  var escaped = querystring.escape(str)
  console.log(escaped)
  
  // 输出
  id%3D3%26city%3D%E5%8C%97%E4%BA%AC%26url%3Dhttps%3A%2F%2Fwww.baidu.com
  ```

- `querystring.unescape(str)`：解码

  ```js
  const querystring = require('querystring')
  var str = 'id%3D3%26city%3D%E5%8C%97%E4%BA%AC%26url%3Dhttps%3A%2F%2Fwww.baidu.com'
  var unescaped = querystring.unescape(str)
  console.log(unescaped)
  
  // 输出
  id=3&city=北京&url=https://www.baidu.com
  ```

#### 3. http

- node的浏览端调试：`node --inspect --inspect-brk server.js`

- node进程管理工具：一直监听，如果代码有修改会自动重启
  - supervisor
  - forever
  - nodemon
  - pm2
  
- `response.end()`中也可以写返回的信息

- `get`：

  ```js
  const http = require('http')
  const querystring = require('querystring')
  const https = require('https');
  
  const server = http.createServer((request, response) => {
      // console.log(response);
  
      // const url = request.url
      // console.log(url);
  
      https.get('https://www.xiaomiyoupin.com/mtop/mf/cat/list', (result) => {
          let data = ''
          result.on('data', (chunk) => {
              data += chunk
          })
          result.on('end', () => {
              response.writeHead(200, {
                  // 'content-type': 'text/html'
                  'content-type': 'application/json;charset=utf-8'
              })
              // response.write('<div>hello</div>')
              // response.write('{"x": 1}')
              // response.end('{"x": 1}')
              // console.log(data);
              // response.write(`{"url": "${url}"}`)
              response.write(JSON.stringify(querystring.parse(data)))
              response.end()
          })
      })
  })
  
  server.listen(8080, () => {
      console.log('localhost:8080');
  })
  ```

- `post`

  ```js
  const http = require('http');
  const querystring = require('querystring');
  
  const postData = querystring.stringify({
      province: '上海',
      city: '上海',
      district: '宝山区',
      address: '同济啊吧啊吧',
      latitude: 43.0,
      longitude: 160.0,
      message: '求购一条小鱼',
      contact: '13666666666',
      type: 'sell',
      time: 1571217561
  })
  
  const options = {
      protocol: 'http:',
      hostname: 'localhost',
      method: 'post',
      port: 3000,
      path: '/data',
      headers: {
          'content-type': 'application/x-www-form-urlencoded',
          'Content-Length': Buffer.byteLength(postData),
      }
  }
  
  const server = http.createServer((req, res) => {
      const request = http.request(options, (result) => {
  
      })
      request.write(postData)
      request.end()
  
      res.end()
  })
  
  server.listen(8080, () => {
      console.log('localhost:8080');
  })
  ```

#### 4. 跨域

- jsonp利用 `script` 标签加载js不跨域的特性，从后端拉取js代码运行，jsonp中的p是padding（包裹数据的函数），拿到callback后，传入数据调用函数；cors就是在后台给前端返回一个首部字段：`Access-Control-Allow-Origin`；middleware：通过http-proxy-middleware实现地址的代理，从而实现了跨域。

##### jsonp

- JSON with Padding，是 json 的一种"使用模式"，可以让网页从别的域名（网站）那获取资料，即跨域读取数据。

- 为什么我们从不同的域（网站）访问数据需要一个特殊的技术( JSONP )呢？这是因为 **同源策略 ** 。

- 同源策略，它是由 Netscape 提出的一个著名的安全策略，现在所有支持 JavaScript 的浏览器都会使用这个策略。所谓同源是指，域名，协议，端口相同。

- 当一个百度浏览器执行一个脚本的时候会检查这个脚本是属于哪个页面的 即检查是否同源，只有和百度同源的脚本才会被执行。

- **核心**：`<script>` 标签的src属性并不被同源策略所约束，所以可以获取任何服务器上脚本并执行。

- 案例：通过访问另一个服务器的api，并通过传参的方式把当前的函数传过去，实现了跨域 传参+调用函数

  - 当前html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>jsonp</title>
    </head>
    
    <body>
        <script>
            function getData(data) {
                console.log(data);
            }
        </script>
        <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.1/jquery.js"></script>
        <script src="http://localhost:8080/api/data?cb=getData"></script>
    </body>
    
    </html>
    ```

  - html中引用的跨域的Node.js

    ```js
    const http = require('http')
    const url = require('url')
    
    const server = http.createServer((req, res) => {
        let urlstr = req.url
    
        // true 是为了解析 url中的query为一个字典
        let urlObj = url.parse(urlstr, true)
        switch(urlObj.pathname) {
            case '/api/data':
                res.write(`${urlObj.query.cb}("hello")`)
                break
            default:
                res.write('page not found.')
        }
        res.end()
    })
    
    server.listen(8080, ()=>{
        console.log('localhost:8080');
    })
    ```

##### cors

- 核心：在请求头中加入：`'Access-Control-Allow-Origin': '*'`

##### middleware（http-proxy-middleware）

- [中间件option详解](https://www.jianshu.com/p/a248b146c55a)

  ```js
  var options = {
          target: 'http://www.example.org', // 目标服务器 host
          changeOrigin: true,               // 默认false，是否需要改变原始主机头为目标URL
          ws: true,                         // 是否代理websockets
          pathRewrite: {
              '^/api/old-path' : '/api/new-path',     // 重写请求，比如我们源访问的是api/old-path，那么请求会被解析为/api/new-path
              '^/api/remove/path' : '/path'           // 同上
          },
          router: {
              // 如果请求主机 == 'dev.localhost:3000',
              // 重写目标服务器 'http://www.example.org' 为 'http://localhost:8000'
              'dev.localhost:3000' : 'http://localhost:8000'
          }
      };
  ```

- 实操：

  ```js
  const http = require('http')
  const url = require('url')
  const { createProxyMiddleware } = require('http-proxy-middleware')
  
  const server = http.createServer((req, res) => {
      let urlStr = req.url
      if (/\/api/.test(urlStr)) {
          // console.log(urlStr);
          const proxy = createProxyMiddleware('/api', {
              target: 'https://silkroad.csdn.net/',
              changeOrigin: true
          })
  
          proxy(req, res)
      } else if (/\/aaa/.test(urlStr)) {
          const proxy2 = createProxyMiddleware('/aaa', {
              target: 'https://blog.csdn.net/',
              changeOrigin: true,
              pathRewrite: {
                  '^/aaa': ''
              }
          })
  
          proxy2(req, res)
  
      } 
      else {
          console.log('error');
      }
  })
  
  server.listen(8070, () => {
      console.log('localhost:8070');
  })
  ```

- 第一种：通过正则表达式匹配，检测到 `api` 路由之后进行代理转发给target的字段中，同时 `api` 的字段以及后面的路由和参数都会保留，进行访问

- 第二种：通过正则表达式匹配，检测到 `aaa` 路由之后进行代理转发给target的字段中，同时 `aaa` 的字段会被重写为 **空**，之后的路由和参数会保留，进行访问

#### 5. 爬虫

- 工具：`cheerio`

- 样例：爬取魅族官网

  ```js
  const http = require('http')
  const https = require('https')
  const cheerio = require('cheerio')
  
  function filterData(data) {
      const $ = cheerio.load(data)
      // console.log(data);
  
      $('.section-item-box p').each((index, el) => {
          console.log(index);
          console.log($(el).text());
      })
  }
  
  const server = http.createServer((req, res) => {
      let data = ''
      https.get('https:www.meizu.com', (result) => {
          result.on('data', (chunk) => {
              data += chunk
          })
          result.on('end', () => {
              filterData(data)
          })
      })
  })
  
  server.listen(8080, () => {
      console.log('localhost:8080');
  })
  ```

#### 6. events

事件触发

```js
const EventEmitter = require('events')

class MyEventEmitter extends EventEmitter { }


const event = new MyEventEmitter()

event.on('play', (value) => {
    console.log(value);
})

event.on('play', (value) => {
    console.log('another' + value);
})


// 触发
event.emit('play', 'movie')
event.emit('play', 'movie')
event.emit('play', 'movie')
```

#### 7. File System

- 文件夹操作

  - 增：`fs.mkdir`
  - 删：`fs.rmdir`
  - 改：`fs.rename`
  - 查：`fs.readdir`

- 回调是异步的，因为函数是传进去的。

- 同步的方法需要在后面加上 `Sync`，比如文件的读取对应的同步函数为：`fs.readFileSync`

- 文件操作

  - 增：`fs.writeFile`

  - 删：`fs.unlink`

  - 改：`fs.appendFile`

  - 查：`fs.readFile`

    - 这样获取到的值是buffer，转换成字符串有两种方法，一种是在参数中增加 `utf-8`；另一种是在输出时增加 `.toString()`

      ```js
      fs.readFile('./logs/log1.log', 'utf-8', (err, result) => {
          console.log(result.toString());
      })
      ```

- `fs.stat`：读取文件（夹）信息，再调用 `.isDirectory()` 判断是否是文件夹

- 递归获取文件目录下所有文档的内容

  ```js
  function readDir(dir) {
      fs.readdir(dir, (err, content) => {
          content.forEach((value, index) => {
              let joinDir = `${dir}/${value}`
              fs.stat(joinDir, (err, stats) => {
                  if (stats.isDirectory()) {
                      readDir(joinDir)
                  } else {
                      fs.readFile(joinDir, 'utf-8', (err, content) => {
                          console.log(content);
                      })
                  }
              })
          })
      })
  }
  ```

- `fs.watch`：监视文件（夹）的变化

#### 8. Stream 和 Zlib

- 读取流和写入流和压缩流

  ```js
  const fs = require('fs')
  const zlib = require('zlib');
  
  const gzip = zlib.createGzip()
  
  const readStream = fs.createReadStream('./logs/log1.log')
  const writeStream = fs.createWriteStream('./logs/logs.gzip')
  
  readStream
  .pipe(gzip)
  .pipe(writeStream)
  ```

####  9. readline

- 逐行读入

  ```js
  const readline = require('readline');
  
  const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
  })
  
  rl.question('你如何看到你爹', (answer) => {
      // 记录
      console.log(`thx for your answer: ${answer}`);
      rl.close()
  })
  ```

####  10. Crypto

- 加密模块，既可以做对称加密，也可以做非对称加密

  ```js
  const crypto = require('crypto');
  const password = 'abc123'
  
  const hash = crypto.createHash('sha1').update(password, 'utf-8').digest('hex')
  
  console.log(hash);
  ```

### 7.7 路由

- 通过url的 switch case，实现路由的分发

  ```js
  const fs = require('fs');
  require('http').createServer((req, res) => {
      // res.end('ok')
      const urlString = req.url
      switch (urlString) {
          case '/':
              res.end('hello')
              break;
          case '/home':
              fs.readFile('./home.html', (err, content) => {
                  res.end(content)
              })
              break;
          case '/home.js':
              fs.readFile('./home.js', (err, content) => {
                  res.end(content)
              })
              break
          case '/pics/a.png':
              fs.readFile('./pics/a.png', (err, content) => {
                  res.end(content)
              })
              break
          default:
              res.end('page 404')
      }
  })
      .listen(8088, () => {
          console.log('localhost: 8088');
      })
  ```

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>home</title>
      <script src="home.js"></script>
  </head>
  <body>
      home
      <img src="./pics/a.png" alt="">
  </body>
  </html>
  ```

- 上述路由的分发存在一个问题：需要对涉及到的资源也要配上路由分发

- 利用package：mime，通过文件类型 设置 content-type，自动获取url对应的静态文件

  ```js
  const fs = require('fs');
  const mime = require('mime')
  
  require('http').createServer((req, res) => {
      const urlString = req.url
      const type = mime.getType(urlString.split('.')[1])
      res.writeHead(200, {
          'content-type': type
      })
  
      const file = fs.readFileSync(`./${urlString}`)
      res.end(file)
  })
      .listen(8088, () => {
          console.log('localhost: 8088');
      })
  ```

### 7.8 静态资源服务

- server.js：

  ```js
  const http = require('http');
  const path = require('path');
  const readStaticFile = require('./fileStatic');
  
  http.createServer(async (req, res) => {
      let urlString = req.url
      let filePathName = path.join(__dirname, './public', urlString)
      console.log(filePathName);
  
      let { data, mimeType } = await readStaticFile(filePathName)
  
      res.writeHead(200, {
          'content-type': `${mimeType}; charset=utf-8`
      })
      res.write(data)
      res.end()
  }).listen(8888, () => {
      console.log('visit success');
  })
  ```

- fileStatic.js

  ```js
  const path = require('path');
  const mime = require('mime');
  const fs = require('fs');
  
  
  function myReadFile(file) {
      return new Promise((resolve, reject) => {
          fs.readFile(file, (err, data) => {
              if (err) {
                  resolve('You visit a folder that index.html not in. / 你访问的文件夹里面没有index.html')
              } else {
                  resolve(data)
              }
          })
      })
  }
  
  async function readStaticFile(filePathName) {
      let ext = path.parse(filePathName).ext
      // 如果前面的值为none，则取后面的值
      let mimeType = mime.getType(ext) || 'text/html'
      let data
  
      // 判断文件是否存在
      if (fs.existsSync(filePathName)) {
          if (ext) {
              // await myReadFile(filePathName).then(result => data = result)
              //     .catch((err) => data = err)
              data = await myReadFile(filePathName)
          } else {
              // await myReadFile(path.join(filePathName, '/index.html')).then(result => data = result)
              //     .catch((err) => data = err)
              data = await myReadFile(path.join(filePathName, '/index.html'))
          }
      } else {
          // console.log('file is not found');
          // res.end('file not found')
          data = 'file or folder not found'
      }
  
      return {
          data,
          mimeType
      }
  }
  
  module.exports = readStaticFile
  ```

### 7.9 Yarn

- Yarn是facebook发布的一款取代npm的包管理工具

  - 速度超快：Yarn 缓存了每个下载过的包，所以再次使用时无需重复下载。 同时利用并行下载以最大化资源利用率，因此安装速度更快。
  - 超级安全：在执行代码之前，Yarn 会通过算法校验每个安装包的完整性。
  - 超级可靠：使用详细、简洁的锁文件格式和明确的安装算法，Yarn 能够保证在不同系统上无差异的工作。

- 参考链接：https://blog.csdn.net/yw00yw/article/details/81354533

- `yarn init`

- `yarn add`

- `yarn add [–-dev –-peer -–optional]`

- `peerDependencies`：同等依赖，也叫同伴依赖，用于指定当前包兼容的宿主版本

- `optionalDependencies`：可选依赖，如果有一些依赖包即使安装失败，项目仍然能够运行或者希望npm继续运行，就可以使用。会覆盖 `dependencies` 中的同名依赖包，不要在两个地方都写

- `bundledDependencies/bundleDependencies`：

- yarn 源：`yarn config get`

  ![](https://img-blog.csdn.net/20180802111644352?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l3MDB5dw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 7.10 Express

- 基于Node.js 平台，快速、开放、极简的Web开发框架

- 创建Express项目

  - 初始化：`yarn init -y`，这里y是yes，只直接跳过交互式对话初始化一个项目
  - 安装生产环境的包：`yarn add express -S`

- 之前是 `res.write(); res.end()`，express是 `res.send()`

- 注意：这里路由的匹配，也是从前往后匹配。`/`和`/api`为例，将永远匹配不到后者；解决方案上，在代码中将 `/api` 放在 `/` 的前面

- 回调函数又被称为中间件

  - 自定义中间件：自己用use写回调函数， 自己调用next
  - 路由中间件：`express.Router()`
  - 第三方中间件：`body-parser`
  - 静态资源服务中间件（内置中间件）：`app.use(express.static('public'))`

- 通过给中间件增加 `next()` 的参数和函数，使得后续的路由依然可以被匹配和执行

- MVC -> MVP：Model-View-Presenter。它们的基本思想有相通的地方：Controller/Presenter负责逻辑的处理，Model提供数据，View负责显示。在MVP里，Presenter完全把Model和View进行了分离，主要的程序逻辑在Presenter里实现。

  - View与Model完全隔离
  - Presenter与View的具体实现技术无关
  - 可以进行View的模拟测试
  - RMVP：R->route，路由

- express路由配置

  - server.js

    ```js
    const express = require('express');
    const app = express()
    
    const router = require('./router/index');
    
    app.use('/', router)
    
    app.listen(8088, () => {
        console.log('assaas');
    })
    ```

  - router/index.js

    ```js
    const express = require('express');
    // 路由中间件
    const router = express.Router()
    
    router.get('/', (req, res, next) => {
        res.send('hello wwww')
    })
    
    router.get('/index', (req, res, next) => {
        res.send('index pages')
    })
    
    module.exports = router
    ```

- 获取前端数据

  - get：`const query = req.query`，获取数据

  - post：添加数据

    ```js
    const bodyParser = require('body-parser');
    const router = require('./router/index');
    app.use(bodyParser.urlencoded({ extended: false }))
    app.use('/', router)
    
    
    router.post('/index', (req, res, next) => {
        const data = req.body
        console.log(data);
        res.send(data)
    })
    ```

  - put、patch、delete：覆盖式修改数据、增量修改数据、删除数据

  - `router.all`：接收上述所有的请求

  - 工具：`body-parser`

    - 解析form：`app.use(bodyParser.urlencoded({ extended: false }))`
    - 解析json：`app.use(bodyParser.json())`

- 服务端渲染与客户端渲染

  - express template
    - ejs
    - pug
    - jade
    - **art-template**
  - 页面 render
    - SSR：Server Side Render，服务端渲染
    - CSR：Client Side Render，客户端渲染

- art-template

  - install：`yarn add art-template express-art-template -S`

- CMS：Content Management System，内容管理系统

### 7.11 MongoDB

- MongoDB是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为WEB应用提供可扩展的高性能数据存储解决方案。

- 特点：高性能、易部署、易使用，存储数据非常方便。

- MongoDB的数据类型

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/b8d3dddafc574eb39cb4955d269888b6.png)

- 数据库的常用命令

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/1b6a49cf1f86443e8f8ca7d3b1e132ba.png)

- mongodb启动服务：`mongod --dbpath D:\mdb_database`，后面的路径是数据存放的路径

- mongodb shell：开启另一个cmd，`mongodb`

- 注意：删除数据库：`db.dropDatabase()` ，是删除当前打开的数据库

- 集合操作：

  - `db.createCollection('collextionName')`：创建一个集合
  - `db.getCollection('account')`：得到指定名称的集合
  - `db.getCollectionNames()`：得到当前db的所有集合
  - `db.printCollectionStats()`：显示当前db所有集合的状态

- 文档操作

  - 插入数据：

    - `db.mabaoguo.insert([{name: 'm1', release: '2020-12-05'}])`
    - ` db.mabaoguo.insert([{name: 'm2', release: '2020-12-06'}, {name: 'm3', release: '2020-12-07'}])`
    - ` db.mabaoguo.save([{name: 'm4', release: '2020-12-06'}, {name: 'm5', release: '2020-12-07'}])`
    - `db.mabaoguo.insert([{name: 'm1', release: '2020-12-05', publishNum: 100}])`

  - 修改数据：

    - `db.mabaoguo.update({name: 'm1'}, {$set: {release: '2022-11-11'}})`：修改name为m1的release为2022-11-11，默认只修改第一个找到的
    - `db.mabaoguo.update({name: 'm1'}, {$inc: {publishNum: 200}})`：找到第一条符合的记录，然后增加记录中对应字段publishNum的值+200
    - ` db.mabaoguo.update({name: 'm12'}, {$inc: {publishNum: 200}}, true)`：后面的true是：找不到就创建该条数据；如果是false，就无事发生
    - ` db.mabaoguo.update({name: 'm1'}, {$inc: {publishNum: 200}}, true, true)`：最后的true是：是否匹配所有，例子中的代码就是找到所有符合条件的，然后都加200

  - 删除数据：

    - ` db.mabaoguo.remove({name: 'm12'})`

  - 查询数据：

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/ba2dc75840254e27aa858959ae4798e5.png)

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/1f3868f7d751402f9bb0b137ea3a7c43.png)

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/07f097801255425282dbac005d2dbf39.png)

    - `db.mabaoguo.find()` 查看所有数据
    - `db.mabaoguo.distinct('name')` 查看name字段的去重数据
    - `db.mabaoguo.find({release: '2020-12-06'})` 查询满足条件的数据
    - `db.mabaoguo.find({release: {$gt: '2020-12-06'}})` 查询数据大于该值的数据；所以小于就是 `lt`；大于等于是 `gte`
    - `db.mabaoguo.find({release: {$gt: '2020-12-05', $lt: '2020-12-07'}})` 查询区间内的数据
    - `db.mabaoguo.find({name: /1/})` 查询name中包含1的 类似`%1%`
    - `db.mabaoguo.find({name: /^1/})` 查询name中包含1，且1开头的，类似 `1%`；同样的 `/1$/`，则是类似 `%1`
    - `db.mabaoguo.find({}, {_id: 0, publishNum: 0})` 查询结果中不显示id和publishNum
    - `db.mabaoguo.find({name: /1$/}, {_id: 0, publishNum: 0})` 查询name以1结尾的数据
    - `db.mabaoguo.find().sort({release: 1})` 排序，按照对应字段的 1：升序；-1：降序 排序
    - `db.mabaoguo.find().limit(3)` 只要查询结果的前3条数据
    - ` db.mabaoguo.find().limit(3).skip(2)` 查询结果跳过前2条后取前3条数据
    - **无论 find limit sort 的顺序如何，都是先sort后find最后limit** 
    - ` db.mabaoguo.find({$or: [{release: '2020-12-05'}, {release: '2020-12-07'}]})` or 或 条件查询
    - `db.mabaoguo.findOne()` 获取第一条记录
    - `db.mabaoguo.find().count()` 输出结果集的记录数


### 7.12 JWT基础

- cookie和session：前端存cookie，后端存session，通过cookie和session对比或者dict[cookie] == session 来判断用户信息

- token：第一次访问时，后端返回给前端，之后每一次前端访问都带token，通过对token的验证了判断用户信息

- jwt：生成token的方法，json web token

-  密钥生成

  - `openssl`
  - 生成私钥：`genrsa -out rsa_private_key.pem 2048`
  - 根据私钥生成公钥：`rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem`

- 加密解密：

  ```js
  var template = require('art-template');
  var path = require('path');
  var fs = require('fs');
  var jwt = require('jsonwebtoken');
  
  const listModel = require('../model/list');
  
  const list = (req, res, next) => {
      // let data = '<ul>'
      // for (let i = 0; i < 100; i++) {
      //     data += `<li>line ${i}</li>`
      // }
      
      // data += '</ul>'
      // res.send(data)
  
      // let dataObj = {
      //     ret: true,
      //     data: []
      // }
      // for(var i = 0; i<100; i++) {
      //     dataObj.data.push('line' + i)
      // }
      // res.send(dataObj)
  
      // let dataArray = []
      // for (let i = 0; i < 1000; i++) {
      //     dataArray.push('line' + i)
      // }
  
      // res.set('content-type', 'application/json;charset=utf-8')
      // res.header('Content-Type', 'application/json;charset=utf-8')
  
      // res.render('list', {
      //     data: JSON.stringify(dataArray)
      // })
  
      // res.render('list-html', {
      //     data: dataArray
      // })
  
      var html = template(path.join(__dirname, '../view/list-html.art'), {
          data: listModel.dataArray
      })
      fs.writeFileSync(path.join(__dirname, '../public/list.html'), html)
      // console.log(html);
      res.send(html)
  }
  
  const token = (req, res, next) => {
      // res.send('ok')
  
      // 对称加密
      const token = jwt.sign({username: 'admin'}, 'hahaha')
      // res.send(token)
      const result = jwt.verify(token, 'hahaha')
      // res.send(result)
  
      // 非对称加密
      const privateKey = fs.readFileSync(path.join(__dirname, '../keys/rsa_private_key.pem'))
      const tk = jwt.sign({username: 'admin'}, privateKey, {algorithm: 'RS256'})
      const publicKey = fs.readFileSync(path.join(__dirname, '../keys/rsa_public_key.pem'))
      const result2 = jwt.verify(tk, publicKey)
      res.send(result2)
  
  }
      
  exports.list = list
  exports.token = token
  ```

### 7.13 Socket

- 网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/70486d5432f142cd9832429b32bec0fe.png)

- 实现

  - 基于net模块实现socket
  - WebSocket
    - 缺点：浏览器必须支持html5
  - Socket.io
    - 优点：可以兼容ie8

### 7.14 Node.js项目

1. 前端 Frontend
   - 前端工程化环境 webpack
   - CSS 预处理工具 sass
   - JS库 jQuery
   - SPA：single page application，路由：SME-Router
   - JS模块化：ES Module，CommonJS Module
   - UI 组件库：Bootstrap（AdminLTE）
   - RMVC：Art-template
2. 后端 Backend
   - Node.js
   - Express
   - MongoDB（Mongoose）




















学到P333


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
