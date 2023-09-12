# VUE速查手册

> 初衷：解决学习vue过程中遇到的各种问题

## 1. eslint

**介绍**

- eslint是一个管理代码风格的包

**问题**

1. 问题：找不到 `.eslintrc.js` 文件，代码跑不起来

   解决：在 `vue.config.js` 中直接 设置 `lintOnSave: false`，直接关闭eslint

2. 问题：启动之后老是报错 `sass` 找不到

   解决：安装的版本不对，在开发依赖（devDependencies）里，`sass` 和 `sass-loader` 的版本导致的，我是用的版本推荐：

   ```json
   "sass": "^1.32.7",
   "sass-loader": "^12.0.0"
   ```



## 2. element-ui

**介绍**

- Element-ui适用于Vue2框架，Element-plus适用于Vue3框架

**问题**

1. 问题：Vue引入element-ui报错【Uncaught TypeError: Cannot read property ‘prototype‘ of undefined】

   解决：不要引入 `element-ui`，改为 `element-plus` ，需要注意的是，`index.css` 的路径里没有 `lib` 哈

   ```js
   import { createApp } from 'vue'
   import ElementUI from 'element-plus'
   import App from './App.vue'
   import router from './router'
   import store from './store'
   import "element-plus/theme-chalk/index.css"
   
   createApp(App).use(ElementUI).use(store).use(router).mount('#app')
   ```

2. 





## 3. vue-router

**问题**

1. 问题：怎么编写vue3的默认路由匹配，如果输入了不存在的路由，自动跳转到某个页面

   解决：

   - 在vue2中，匹配所有要放到最后，因为路由是从上往下匹配，匹配到一个后就会停止，如果把加 * 号的路由写到上边，可能会引发死循环

     ```js
     const needLoginRoutes = [
       {
         path: '/',
         name: 'Home',
         component: () => import('../views/Home.vue')
       },
       {
         path: '/home',
         redirect: '/'
       }
     ]
      
     const routes = [
       {
         path: '/login',
         name: 'Login',
         component: () => import('../views/Login.vue')
       },
       {
         path: '/404',
         name: '404',
         component: () => import('../views/404.vue')
       },
       {
         path: '/manage-*', // 匹配所有以manage开头的路由
         name: 'Manage',
         component: () => import('../views/manage.vue')
       },
       {
         path: '*', // 匹配所有路由
         redirect: '/404'
       }
     ]
     ```

   - 在vue3中，vue-router 把 * 这种写法废弃了，如果需要匹配所有，需要写成这样

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

2. 

