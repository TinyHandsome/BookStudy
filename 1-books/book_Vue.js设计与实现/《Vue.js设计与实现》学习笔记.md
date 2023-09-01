# 《Vue.js设计与实现》学习笔记

[TOC]

## 写在前面

- 封面 | 摘要 | 关键词

  ![请添加图片描述](https://img-blog.csdnimg.cn/d94de1e39e59488d965b041c8322b78d.png)

  

- 读后感

  - 写的实在是太太太好了，深入浅出、问答式内容，完全可以看出作者 **霍春阳** 专业水平之高超，知识积累之深厚，框架理解之独到。

- 摘抄

  - <mark>框架设计里到处都体现了权衡的艺术。</mark>

- 传送门

## 1. 框架设计概览

### 1.1  权衡的艺术

1. <mark>Vue.js 的内部实现一定是**命令式**的，而暴露给用户的却更加**声明式**。</mark> 命令式更加关注过程，而声明式更加关注结果。

   命令式在理论上可以做到极致优化，但是用户要承受巨大的心智负担；而声明式能够有
   效减轻用户的心智负担，但是性能上有一定的牺牲，框架设计者要想办法尽量使性能损耗最小化。

2. 声明式代码的性能不优于命令式代码的性能。

   - 声明式代码的更新性能消耗 = 找出差异的性能消耗 + 直接修改的性能消耗
   - 虚拟 DOM，就是为了最小化找出差异这一步的性能消耗而出现的。

3. 为什么 Vue.js 要选择声明式的设计方案呢？

   原因就在于声明式代码的**可维护性更强**。

4. 框架设计者要做的就是：在保持可维护性的同时让性能损失最小化。

5. `div.innerHTML = html`

   - 为了渲染出页面，首先要把字符串解析成 DOM 树，这是一个 DOM 层面的计算。

   - 涉及 DOM 的运算要远比 JavaScript 层面的计算性能差。

   - 可以用一个公式来表达通过 innerHTML 创建页面的性能：

     HTML 字符串拼接的计算量 + innerHTML 的 DOM 计算量

   - 虚拟 DOM 创建页面的过程分为两步：

     - 第一步是创建 JavaScript 对象，这个对象可以理解为真实 DOM 的描述；
     - 第二步是递归地遍历虚拟 DOM 树并创建真实 DOM。
     - 我们同样可以用一个公式来表达：创建 JavaScript 对象的计算量 + 创建真实 DOM 的计算量。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/6ddae40d7eb44d0d87d3833900ee8a2c.png)

6. 使用 innerHTML 更新页面的过程是重新构建 HTML 字符串，再重新设置 DOM 元素的 innerHTML 属性，这其实是在说，哪怕我们只更改了一个文字，也要重新设置 innerHTML 属性。而重新设置innerHTML 属性就等价于销毁所有旧的 DOM 元素，再全量创建新的 DOM 元素。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/17cecd4177614d7cad348a6439775f3a.png)

   - 对于虚拟 DOM 来说，无论页面多大，都只会更新变化的内容，而对于 innerHTML 来说，页面越大，就意味着更新时的性能消耗越大。

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/4b542db00c984c6e86d19e1de98962b3.png)

   - 总结

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/fbce5bbc63ff454997c8a549248056e3.png)

7. 运行时和编译时

   - 分类：
     - 纯运行时
     - 运行时 + 编译时
     - 纯编译时
   - Vue.js 3 仍然保持了运行时 + 编译时的架构，在保持灵活性的基础上能够尽可能地去优化。

### 1.2 框架设计的核心要素

1. 提升用户的开发体验

   - 优化打印输出：以 Chrome 为例，我们可以打开 DevTools 的设置，然后勾选 “Console”→“Enable custom formatters” 选项

2. 控制框架代码的体积

   - Q：提供越完善的警告信息就意味着我们要编写更多的代码，这不是与控制代码体积相悖吗？

     A：每一个 warn 函数的调用都会配合 `__DEV__` 常量的检查。Vue.js 在输出资源的时候，会输出两个版本，其中一个用于开发环境，另一个用于生产环境。当 Vue.js 构建用于开发环境的资源时，会把 `__DEV__` 常量设置为true。这样我们就做到了在开发环境中为用户提供友好的警告信息的同时，不会增加生产环境代码的体积。

3. 框架要做到良好的 Tree-Shaking

   - Q：我们知道 Vue.js 内建了很多组件，例如 `<Transition>` 组件，如果我们的项目中根本就没有用到该组件，那么它的代码需要包含在项目最终的构建资源中吗？

     A：当然不需要。那么如何做到这一点呢？**Tree-Shaking**

   - Tree-Shaking：在前端领域，这个概念因 rollup.js 而普及。简单地说，Tree-Shaking 指的就是消除那些永远不会被执行的代码，也就是排除 dead code，现在无论是 rollup.js 还是 webpack，都支持 Tree-Shaking。

   - 想要实现 Tree-Shaking，必须满足一个条件，即模块必须是 ESM（ES Module），因为 Tree-Shaking 依赖 ESM 的静态结构。

   - Tree-Shaking 中的第二个关键点——副作用。副作用就是，当调用函数的时候会对外部产生影响，例如修改了全局变量。到底会不会产生副作用，只有代码真正运行的时候才能知道，JavaScript 本身是动态语言，因此想要静态地分析哪些代码是 dead code 很有难度。

   - `rollup.js` 中通过注释代码 `/*#__PURE__*/` 来告诉 `rollup.js`，对于foo函数的调用不会产生副作用，可以放心的进行 Tree-Sharking

     ```js
     import {foo} from './utils'
     
     /*#__PURE__*/ foo()
     ```

   - 在 Vue.js 3 的源码中，基本都是在一些顶级调用的函数上使用 `/*#__PURE__*/` 注释。因为对于顶级调用来说，是可能产生副作用的；但对于函数内调用来说，只要函数 bar 没有被调用，那么 foo 函数的调用自然不会产生副作用。

     ```js
     foo() // 顶级调用
     
     function bar() {
     	foo() // 函数内调用
     }
     ```

4. 框架应该输出怎样的构建产物

   IIFE：Immediately Invoked Function Expression，即“立即调用的函数表达式”，易于用 JavaScript 来表达

5. 特性开关

   - 怎么实现特性开关呢？

     本质上是利用 rollup.js 的预定义常量插件来实现。

   - `__VUE_OPTIONS_API__` 特性开关有什么用？

     - 在 Vue.js2 中，编写的组件叫作组件选项 API

       ```js
       export default {
       	data() {}, // data 选项
       	computed: {}, // computed 选项
       	// 其他选项
       }
       ```

     - 但是在 Vue.js 3 中，推荐使用 Composition API 来编写代码

       ```js
       export default {
       	setup() {
       		const count = ref(0)
       		// 相当于Vue.js 2 中的 computed 选项
       		const doubleCount = computed(() => count.value * 2) 
       	}
       }
       ```

   - 如果明确知道自己不会使用选项 API，用户就可以使用 `__VUE_OPTIONS_API__` 开关来关闭该特性，这样在打包的时候Vue.js 的这部分代码就不会包含在最终的资源中，从而减小资源体积。

6. 错误处理

   - 我们提供了 registerErrorHandler 函数，用户可以使用它注册错误处理程序，然后在 callWithErrorHandling 函数内部捕获错误后，把错误传递给用户注册的错误处理程序。
   - 这时错误处理的能力完全由用户控制，用户既可以选择忽略错误，也可以调用上报程序将错误上报给监控系统。
   
7. 良好的 TypeScript 类型支持

   - 使用 TS 编写框架

     ```typescript
     function foo(var: any){
     	return val
     }
     ```

   - 对 TS 类型支持友好

     ```typescript
     function foo<T extends any>(var: T): T {
     	return val
     }
     ```

### 1.3 Vue.js3 的设计思路

1. 声明式地描述 UI

   - 使用与 HTML 标签一致的方式来描述 DOM 元素，例如描述一个div 标签时可以使用 `<div></div>`；
   - 使用与 HTML 标签一致的方式来描述属性，例如 `<div id="app"></div>`；
   - 使用 : 或 v-bind 来描述动态绑定的属性，例如 <`div :id="dynamicId"></div>`；
   - 使用 @ 或 v-on 来描述事件，例如点击事件 `<div @click="handler"></div>`；
   - 使用与 HTML 标签一致的方式来描述层级结构，例如一个具有span 子节点的 div 标签 `<div><span></span></div>`。

2. 使用 JavaScript 对象来描述 UI ，**其实就是所谓的虚拟 DOM**。

   对应Vue：`<h1 @click="handler"><span></span></h1>`

   ```js
   const title = {
       // 标签名称
       tag: 'h1',
       // 标签属性
       props: {
           onClick: handler
       },
       // 子节点
       children: [
           { tag: 'span' }
       ]
   }
   ```

3. Vue.js 3 除了支持使用模板描述 UI 外，还支持使用虚拟 DOM 描述 UI。

   ```js
   import { h } from 'vue'
   
   export default {
       render() {
           return h('h1', { onClick: handler }) // 虚拟 DOM
       }
   }
   ```

   更复杂的，可以写成

   ```js
   export default {
       render() {
           return {
               tag: 'h1',
               props: { onClick: handler }
           }
       }
   }
   ```

   组件的渲染函数：一个组件要渲染的内容是通过渲染函数来描述的，也就是上面代码中的 render 函数，Vue.js 会根据组件的 render 函数的返回值拿到虚拟 DOM，然后就可以把组件的内容渲染出来了。

4. 初识渲染器

   - 渲染器的作用就是把虚拟 DOM 渲染为真实 DOM

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/95bc33ad189e4afea267c88d44b284b2.png)

   - renderer 的实现思路

     - 创建元素：把 vnode.tag 作为标签名称来创建 DOM 元素。
     - 为元素添加属性和事件：遍历 vnode.props 对象，如果 key 以 on 字符开头，说明它是一个事件，把字符 on 截取掉后再调用 toLowerCase 函数将事件名称小写化，最终得到合法的事件名称，例如 onClick 会变成 click，最后调用addEventListener 绑定事件处理函数。
     - 处理 children：如果 children 是一个数组，就递归地调用 renderer 继续渲染，注意，此时我们要把刚刚创建的元素作为挂载点（父节点）；如果 children 是字符串，则使用 createTextNode 函数创建一个文本节点，并将其添加到新创建的元素内。

5. 组件的本质

   - **组件就是一组 DOM 元素的封装** 

     ```js
     // MyComponent 是一个函数
     const MyComponent = function () {
         return {
             tag: 'div',
             props: {
                 onClick: () => alert('hello')
             },
             children: 'click me'
         }
     }
     
     // MyComponent 是一个对象
     const MyComponent = {
         render() {
             return {
                 tag: 'div',
                 props: {
                     onClick: () => alert('hello')
                 },
                 children: 'click me'
             }
         }
     }
     ```

6. 模板的工作原理

   - 编译器的作用其实就是将**模板**编译为**渲染函数**（我的理解：也就是render()函数，返回的就是一个对象，里面有各种信息，如上5所示）
   - 编译器会把模板内容编译成渲染函数并添加到 `<script>` 标签块的组件对象上
   - 无论是使用模板还是直接手写渲染函数，对于一个组件来说，它要渲染的内容最终都是通过渲染函数产生的，然后渲染器再把渲染函数返回的虚拟 DOM 渲染为真实 DOM，这就是模板的工作原理，也是 Vue.js 渲染页面的流程。

7. Vue.js 是各个模块组成的有机整体

   - 编译器能识别出哪些是静态属性（`id="foo"`），哪些是动态属性（`:class="cls"`），在生成代码的时候完全可以附带这些信息
   - 实现方式：在生成的虚拟 DOM 对象中多出了一个 patchFlags 属性，假设数字 1 代表“ class 是动态的 ”，这样就能知道只有class属性会发生变化

## 2. 响应系统

### 2.1 响应系统的作用与实现

1. 响应式数据与副作用函数

   - 函数改变了dom某个文本的内容，但是其他函数可能会读取或设置该内容，所以这个函数就是副作用函数
   - 函数修改了全局变量，也是副作用函数
   - 响应式数据：某个对象的值发生改变时，副作用函数自动重新执行

2. 响应式数据的基本实现

   - 如果我们能拦截一个对象的读取和设置操作，事情就变得简单了，当读取字段 obj.text 时，我们可以把副作用函数 effect 存储到一个“桶”里

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/53041497879c4ad883cba1d3b7e0aaf5.png)

   - 如何才能拦截一个对象属性的读取和设置操作？

     - 在 ES2015 之前，只能通过 Object.defineProperty 函数实现，这也是 Vue.js 2 所采用的方式

     - 在 ES2015+ 中，我们可以使用代理对象 Proxy 来实现，这也是 Vue.js 3 所采用的方式

       ```js
       // 存储副作用函数的桶
       const bucket = new Set()
       
       // 原始数据
       const data = { text: 'hello world' }
       // 对原始数据的代理
       const obj = new Proxy(data, {
           // 拦截读取操作
           get(target, key) {
               // 将副作用函数 effect 添加到存储副作用函数的桶中
               bucket.add(effect)
               // 返回属性值
               return target[key]
           },
           // 拦截设置操作
           set(target, key, newVal) {
               // 设置属性值
               target[key] = newVal
               // 把副作用函数从桶里取出并执行
               bucket.forEach(fn => fn())
               // 返回 true 代表设置操作成功
               return true
           }
       }
       ```

     - 当读取属性时将副作用函数 effect 添加到桶里，然后返回属性值

     - 当设置属性值时先更新原始数据，再将副作用函数从桶里取出并重新执行，这样我们就实现了响应式数据

   - *TODO：副作用函数的名字可以任意取，我们完全可以把副作用函数命名为myEffect，甚至是一个匿名函数，因此我们要想办法去掉这种硬编码的机制*

3. 设计一个完善的响应系统

   - 首先，定义了一个全局变量 activeEffect，初始值是 undefined，它的作用是存储被注册的副作用函数。接着重新定义了 effect 函数，它变成了一个用来注册副作用函数的函数，effect 函数接收一个参数 fn，即要注册的副作用函数。
   
     ```js
     // 用一个全局变量存储被注册的副作用函数
     let activeEffect
     // effect 函数用于注册副作用函数
     function effect(fn) {
         // 当调用 effect 注册副作用函数时，将副作用函数 fn 赋值给 activeEffect
         activeEffect = fn
         // 执行副作用函数
         fn()
     }
     ```
   
   - 使用
   
     ```js
     effect(
         // 一个匿名的副作用函数
         () => {
             document.body.innerText = obj.text
         }
     )
     ```
   
   - 问题：没有在副作用函数与被操作的目标字段之间建立明确的联系。
   
      解决：用一个树形结构，来建立起对象的属性和副作用函数之间的关系：`text: effectFn`
   
      ![在这里插入图片描述](https://img-blog.csdnimg.cn/d0192899566a432090ed18f422feae42.png)
   
      - Set 数据结构所存储的副作用函数集合称为 key 的依赖集合
      - WeakMap 对 key 是弱引用，不影响垃圾回收器的工作
   
   - 封装
   
      ```js
      const obj = new Proxy(data, {
          // 拦截读取操作
          get(target, key) {
              // 将副作用函数 activeEffect 添加到存储副作用函数的桶中
              track(target, key)
              // 返回属性值
              return target[key]
          },
          // 拦截设置操作
          set(target, key, newVal) {
              // 设置属性值
              target[key] = newVal
              // 把副作用函数从桶里取出并执行
              trigger(target, key)
          }
      })
      
      // 在 get 拦截函数内调用 track 函数追踪变化
      function track(target, key) {
          // 没有 activeEffect，直接 return
          if (!activeEffect) return
          let depsMap = bucket.get(target)
          if (!depsMap) {
              bucket.set(target, (depsMap = new Map()))
          }
          let deps = depsMap.get(key)
          if (!deps) {
              depsMap.set(key, (deps = new Set()))
          }
          deps.add(activeEffect)
      }
      // 在 set 拦截函数内调用 trigger 函数触发变化
      function trigger(target, key) {
          const depsMap = bucket.get(target)
          if (!depsMap) return
          const effects = depsMap.get(key)
          effects && effects.forEach(fn => fn())
      }
      ```
   
4. 分支切换与cleanup



















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
