## VSCode终端提示'pnpm'不是内部或外部命令

1. 先检查 nvm 的 node 版本是不是你想要的：`nvm list`
2. 如果是，再装一遍兄弟，如果有版本限制记得加：`npm install -g pnpm[@版本]`
3. :bulb: 重点1，检查当前 npm 的位置在不在系统路径里：`npm prefix -g`，把这个路径加在系统变量的 path 中
4. :bulb: 重点2，管理员打开 powershell，运行：`set-ExecutionPolicy RemoteSigned`，输入 `A（全是）`
5. 重启 vscode 就ok了

> 参考1：https://blog.csdn.net/changchang_/article/details/135066010
>
> 参考2：https://blog.csdn.net/AjaxY/article/details/144589430



