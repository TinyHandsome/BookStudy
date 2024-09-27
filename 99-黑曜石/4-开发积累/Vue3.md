# Vue3

[TOC]

## vite

- 新建一个项目：`pnpm create vite [项目名称] --template vue`
- 打包部署和nginx配置[^6][^7]



### 重要配置项

#### @路径配置

1. 安装 `path` 的库：`pnpm install @types/node`

2. 在 `vite.config.ts` 中配置 `resolve` [^3]

   ```typescript
   import { resolve } from "path"
   ...
   
   export default defineConfig({
     ...
     resolve: {
       // 配置路径别名
       alias: {
         '@': resolve(__dirname, './src'),
       },
     },
   })
   
   ```

3. 在 `tsconfig.json` 中配置 `compilerOptions` 以开启@的路径配置

   ```json
   "compilerOptions": {
   	...
       /* 新增：允许@的路径 */
       "baseUrl": ".",
       "paths": {
         "/@/*": ["src/*"],
         "/#/*": ["types/*"],
         "@/*": ["src/*"],
         "#/*": ["types/*"]
       }
       ...
   }
   ```

#### build移除console.log

- 在 `vite.config.ts` 中配置 `build`：[^7]

  ```
  export default defineConfig({
    ...
    build: {
      // 必须开启：使用terserOptions才有效果
      minify: "terser", 
      terserOptions: {
        compress: {
          //生产环境时移除console
          drop_console: true,
          drop_debugger: true,
        },
      },
    },
    ...
  })
  ```

  


## pinia

- 持久化：`pnpm i pinia-plugin-persistedstate`，使用：

  ```typescript
  // main.ts
  import { createPinia } from 'pinia'
  import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
  
  const pinia = createPinia()
  pinia.use(piniaPluginPersistedstate)
  
  // xxxStore.ts
  export const useStore = defineStore('main', ()=>{}, { persist: true })
  ```

  



## 样式

### TailwindCSS

> 一个功能类优先的 CSS 框架，用于快速构建定制的用户界面。这是来自 [TailwindCss](https://tailwindcss.com/) 官方定义。 [中文网站](https://www.tailwindcss.cn/)
>
> Tailwindcss 基于原子化理念，将样式重复性代码降到最小，原本开发最大限度基于类名的声明块不重复，现在Tailwindcss基于单独一句声明不重复。[^1]

1. 安装依赖：`pnpm install -D tailwindcss@latest postcss@latest autoprefixer@latest`。
2. 创建配置文件：`pnpx tailwindcss init -p`，生成两个文件：`tailwind.config.js`和`postcss.config.js`。
3. 配置 Tailwind 来移除生产环境下没有使用到的样式声明：在`tailwind.config.js`文件中，配置 `purge` 选项指定所有的 pages 和 components 文件，使得 Tailwind 的 `purge` 选项可以在生产构建中对未使用的样式进行摇树 **tree-shake** 优化。==注意：purge已经过时了，要用content==
4. 在您的 CSS 中引入 Tailwind：创建 `./src/index.css` 文件 并使用 `@tailwind` 指令来包含 Tailwind的 `base`、 `components` 和 `utilities` 样式，来替换掉原来的文件内容。（阅读我们的文档[添加基础样式](https://www.tailwindcss.cn/docs/adding-base-styles)，[提取组件](https://www.tailwindcss.cn/docs/extracting-components)，和[添加新的功能类](https://www.tailwindcss.cn/docs/adding-new-utilities)，以获得用您自己的自定义 CSS 扩展 Tailwind 的最佳实践。）
5. 最后，确保您的 CSS 文件被导入到您的 `./src/main.js` 文件中：`import './index.css'`
6. vscode插件：**tailwind css intellisense**



## axios

> axios 是什么：[^2]
>
> 1. Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。目前是前端最流行的 ajax 请求库
> 2. react/vue 官方都推荐使用 axios 发 ajax 请求

## npm

1. 源修改[^4]

   ```
   pnpm config set registry https://registry.npm.taobao.org
   pnpm config set registry https://registry.npmjs.org
   ```



### 问题

1. 执行 pnpm install 报错 ERR_PNPM_INVALID_OVERRIDE_SELECTOR [^5]

   ![Image](Vue3.assets/Image.png)

2. 

## 样式模板库

### Element

1. 除了直接使用需要 `pnpm i element-plus`，还有图标库需要下载 `pnpm i @element-plus/icons-vue`



## 前端开发

### 文件下载

- 将文件流包装成blob后下载

  ```typescript
  const handleDownload = async (scope: any) => {
      const row_id = scope.row.id;
      const result = await get_download(row_id);
      if (result) {
          ElMessage.success("文件下载成功...");
      } else {
          ElMessage.error("文件获取失败...");
          return;
      }
  
      // 创建 Blob 对象
      const blob = new Blob([result.data]);
      // 创建下载链接
      const downloadUrl = window.URL.createObjectURL(blob);
      // 创建一个 `<a>` 元素并进行点击操作以触发下载
      const link = document.createElement("a");
      link.href = downloadUrl;
      // 链接的文件下载名称
      link.download = result.headers["content-disposition"].split("=")[1]
      document.body.appendChild(link);
      link.click();
      // 释放 URL 对象占用的内存
      window.URL.revokeObjectURL(downloadUrl);
      // 移除临时创建的 `<a>` 元素
      document.body.removeChild(link);
  };
  ```

- `get_download`：其中axios需要配置 `responseType: 'blob'`

- 后端返回的结果中记得设置 `Content-Type`：`response['Content-Type'] = mimetype_guess(f.title)`







---

[^1]: https://blog.csdn.net/agonie201218/article/details/125762819 "vue3 + Tailwind Css + Vite 搭建快速开发前端样式环境"
[^2]: https://www.cnblogs.com/konglxblog/p/15596135.html "前端异步请求axios的介绍与用法"
[^3]: https://blog.csdn.net/hua_bj/article/details/126181783 "vue3 + vite配置路径别名@"
[^4]: https://juejin.cn/post/7054747440032776199 "npm、yarn、pnpm改源"
[^5]: https://github.com/vbenjs/vue-vben-admin/issues/1479
[^6]: https://blog.csdn.net/qq_19991931/article/details/129667536 "Vite4 + Vue3 项目打包并发布Nginx服务器"
[^7]: https://www.cnblogs.com/yayuya/p/17046666.html "Vite项目打包配置详解"