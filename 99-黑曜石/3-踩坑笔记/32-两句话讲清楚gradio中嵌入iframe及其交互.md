---
sticker: emoji//1f347
tags:
  - gradio
  - iframe
  - python
  - ketcher
  - jsme
banner: 3-踩坑笔记/32-两句话讲清楚gradio中嵌入iframe及其交互.assets/b260e01e7f4b4ea29778a9cf3d7ab56b.png
---
# 两句话讲清楚gradio中嵌入iframe及其交互

> 我不会设置仅粉丝可见，不需要你关注我，仅仅希望我的踩坑经验能帮到你。如果有帮助，麻烦点个 :+1: 吧，这会让我创作动力+1 :grin:。我发现有的时候会自动要求会员才能看，可以留言告诉我，不是我干的！😠

[TOC]

## 写在前面

- 摘要

  想用gradio快速搭建一个应用，用户可以上传文件保存数据，也可以做数值、字符串和分子smiles的复杂查询，其中核心难点在于检索后分子的渲染，这个好说rdkit能直接出PIL的图，转HTML组件操作一下就行。最难的是怎么嵌入分子画板或者说分子编辑器，用户在上面绘制后拿到smiles码。刚好研究了一波，把iframe嵌入gradio的方案吃了个透，后面类似的问题就好解决了。

- **全网、github、stackoverflow 一顿狂搜，真就搜不到解决方案，急死我了，还得靠自己看源码啊家人们，求个赞不过分吧~** :grin:

## 解决方案

1. **选型**

   先用开源的分子编辑器吧，有 jsme 和 ketcher 两种选择，前者虽然简单一点，但是确实丑，我还是选 [ketcher](https://github.com/epam/ketcher) 吧，最后证明跟 ketcher 死磕到底还是有好的结果的，中间好几次差点半途而废，就是因为 jsme 太丑了~ :sob:

2. **证道**

   - 既然选择了 ketcher，那到底咋用呢。可恶啊这个破玩意儿怎么只有给 react 设计好的东西啊，社区里搜到了 vue-ketcher 类似的，可是版本也太老了吧，纯 js 难道就不能用吗，我不服！

   - 我搜啊搜啊，哦豁，官网给开发者留余地了。提供了 [standalone](https://lifescience.opensource.epam.com/download/ketcher.html) 的打包好的离线可运行的项目包，下下来解压后，双击 `index.html` 就能直接用。*很好！很有精神！* 我直接就搬到我 gradio 项目的根目录下

     ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d32afbb7735e434e82570a6745321acb.png)

     ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b260e01e7f4b4ea29778a9cf3d7ab56b.png)

3. **试错**

   一顿操作猛如虎，直接给结论，gradio没办法直接引入本地的（比如当前目录）的css和js，简单来说就是识别不了本地路径，gradio的服务代理不了本地路径。所以解决这个问题可以是直接用 python 读，然后再传参给 gradio。举个栗子：

   **写个函数读**

   ```python
   def load_local_file(path):
       """读取本地文件内容"""
       with open(path, "r", encoding="utf-8") as f:
           content = f.read()
       return content
   ```

   **在 gradio 中传参**

   ```python
   with gr.Blocks(
       title="🚀 催化剂信息查询",
       css=load_local_file("./standalone/static/css/main.4d24dc9f.css"),
       js=load_local_file("./standalone/static/js/main.f30a1a8f.js"),
   ) as demo:
       ...
   ```

   > [!warning] 这样是有问题的
   >
   > 1. css 这样整还行，没啥问题
   > 2. js 不行，报错什么 } 哪里没闭合啊是的，如果我没理解错，js里面写的字符串得是类似 `() => {这里写你的js内容}`
   > 3. html 和 js、css 分开加载，各写各的，那我就得从 ketcher 的 `index.html` 中把需要加载的 css 和 js 掏出来，太不优雅了哥们儿

4. **彻悟**

   - **怎么解决 iframe 的问题**：上面提到了，自己扣出来 js 和 css，然后自己再写 html 太不优雅了，那么用 iframe 嵌入页面总行吧。

     *问题：src里面要是地址，不能是本地的相对路径咋整*

     ```python
     iframe_code = f"""
     <iframe 
         id="ifKetcher"
         src="http://xxx/standalone/index.html" 
         width="100%" 
         height="540px" 
         frameborder="0"
     ></iframe>
     """
     smi = gr.HTML(iframe_code, padding=False)
     ```

   - **启服务，解决 src 里面地址的问题**：先简单写个 HTTPServer，用多线程启动，这就解决了 **本地资源转url** 的问题

     ```python
     from http.server import HTTPServer, SimpleHTTPRequestHandler
     
     KETCHER_DIR = "./"
     KETCHER_PORT = 1234
     def create_local_server(dir=KETCHER_DIR, port=KETCHER_PORT):
         """在当前路径启动一个简单的HTTP服务器"""
         os.chdir(dir)
         server_address = ("", port)
         httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
         # 后台启动
         threading.Thread(target=httpd.serve_forever, daemon=True).start()
     ```

     修改前面的 src，`src="http://xxx/standalone/index.html" `，ip要记得写服务器ip啊，别写什么 `localhost` 之类的，以免部署出错。现在就哦了，能够在界面上看到 `gr.HTML` 组件中嵌入 `iframe`。

   - **解决 gradio 界面和 iframe 界面交互的问题**：都能展示了，但是各玩各的，咋搞？

     :bulb: [浏览器跨域问题解决办法](https://blog.csdn.net/mevicky/article/details/51404610)，核心还是跨域问题，iframe对应的服务和gradio的服务 之间不能交互啊，会被浏览器阻止啊。直接给结论：`contentWindow.postMessage`，用这个接口！那么怎么用呢？事件监听！

     **gradio 监听**：监听到对面的事件类型是我预先定义的 `result`，就从里面拿结果，回填到界面的一个输入组件中，这样就实现了回传数据的显示。

     ```python
     with gr.Blocks(
         title="🚀 催化剂信息查询",
         js="""
             ()=>{
                 window.addEventListener('message', (event) => {
                     if (event.data.type === 'result'){
                         const smiInputComp = document.getElementById('smi-input');
                         smiInputComp.textContent = event.data.value;
                     }
                 })
             }
         """
     ) as demo:
     	...
         smiles = gr.Textbox(show_label=False, placeholder="请输入子片段，比如：COC", scale=8, elem_id="smi-input")
         ...
     ```

     **iframe 界面监听**：在 `index.html` 中加一个 `script` 的 tag，在里面编辑监听事件

     ```html
     <script>
         window.addEventListener('message', async (event) => {
             if (event.source === parent) {
                 const smi = await ketcher.getSmiles();
                 parent.postMessage({type: 'result', value: smi}, '*');
             }
         })
     </script>
     ```

     **按钮逻辑实现**：两边都监听，干活的在哪儿呢？肯定是有一个触发事件的操作，比如按钮，点了之后触发iframe的事件，并传参。

     ```python
     ketcher_btn = gr.Button("从画布中获取", size='lg', variant='primary', min_width=1, scale=1)
     js_content = """
                 async () => {await document.getElementById('ifKetcher').contentWindow.postMessage({'a': 1}, '*')}
                 """
     ketcher_btn.click(js=js_content, inputs=[], outputs=[], fn=lambda x: x)
     ```

     > [!warning] 注意这里的 js 和 fn 参数
     >
     > - js：Optional frontend js method to run before running 'fn'. Input arguments for js method are values of 'inputs' and 'outputs', return should be a list of values for output components. 
     >
     >   就是需要执行的 js 代码
     >
     > - fn：the function to call when this event is triggered. Often a machine learning model's prediction function. Each parameter of the function corresponds to one input component, and the function should return a single value or a tuple of values, with each element in the tuple corresponding to one output component.
     >
     >   直接做一个函数映射就行，即直接返回输入的值（js的内容），没法省略哦。

5. **结果**

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e430060ae4654afba99498cee3b22ed1.png)

**gradio 相关的稍微高级、复杂一点的教程真的啥也找不到啊，太难摸索了，点个赞不过分吧~** :kissing_smiling_eyes:


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
