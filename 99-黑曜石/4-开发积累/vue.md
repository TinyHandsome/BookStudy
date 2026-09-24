# Vue

## 特效

### vue-bits

- 用 jsrepo 安装 vue-bits 插件：`pnpm dlx jsrepo add https://vue-bits.dev/r/Hyperspeed`

- 注意后面的名字得大写，如果有空格，则是 Axx-Bxx

- 查找组件列表：`pnpm dlx jsrepo list https://vue-bits.dev/r`

- 如果却组件，记得：`pnpm add 组件名 -w`

- 如果保存路径到 `apps/web-antd/src/lt-components/bits`，则需要在项目的根目录新建文件 `jsrepo.config.ts`

  ```typescript
  import { defineConfig } from "jsrepo";
  /**
   * jsrepo 安装 vue-bits 插件
   * pnpm dlx jsrepo add https://vue-bits.dev/r/Hyperspeed
   * 路径：apps/web-antd/src/lt-components/bits
   */
  
  export default defineConfig({
  	paths: {
  		component: './apps/web-antd/src/lt-components/bits'
  	}
  });
  ```

### nxui

- 官网给出的是：`pnpm dlx shadcn-vue@latest add "https://nxui.geoql.in/r/dithered-logo.json"`

- 但我发现 jsrepo 依然可以，我更喜欢 jsrepo。所以我直接改：`pnpm dlx jsrepo add https://nxui.geoql.in/r/dithered-logo`，注意这里跟bits就不一样了，不是大写的了，以jsrepo list的结果为准

- 其中cn需要自己处理一下：`  import { cn } from '../lib/utils';` 

  ```typescript
  import type { ClassValue } from 'clsx';
  import { clsx } from 'clsx';
  import { twMerge } from 'tailwind-merge';
  
  export function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
  }
  ```

  - **`clsx`**：处理**条件类名**，自动过滤 `false / null / undefined`，支持对象、数组写法

  - **`twMerge`（tailwind-merge）**：**解决 Tailwind 同类冲突**

    > 重点！普通字符串拼接：`"p-2 p-4"` 两个都会保留，样式结果不可控
    >
    > `cn("p-2", "p-4")` → 自动合并成 `"p-4"`，**后面传入的样式覆盖前面**，所以你在使用组件时传的 `className` 可以覆盖组件默认样式

  - cn 保证**用户写的样式优先级更高，覆盖冲突的 tailwind 类**

    ```ts
    // 基础
    cn("text-sm bg-blue-500")
    
    // 条件
    cn("base-class", isOpen && "opacity-100")
    
    // 冲突自动合并
    cn("px-2 py-2", "px-6") // → "py-2 px-6"
    ```



## 工具

| 维度         | shadcn/ui                                                    | jsrepo                                                       |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **定位**     | 一套 React UI 组件 + 专属 CLI + registry 规范                | **通用 registry 工具链（CLI + 配置 + 更新 + 私有仓库）**，不是组件库 |
| **原生框架** | 原生 React，有社区移植版 shadcn-vue                          | 框架无关：React / Vue / Svelte 全都支持（VueBits 就是 Vue registry） |
| **CLI**      | shadcn 自己写的独立 CLI，只认 shadcn 规范的 registry         | jsrepo 统一 CLI，**可以同时管理多个不同 registry**：shadcn、vue-bits、私有 registry |
| **能力**     | add / 初始化项目；组件更新弱，更新组件容易覆盖，没有 diff 预览 | ✅ add、init、**交互式 update（看 diff 再确认是否更新）**、依赖自动解析、私有 registry、代码转换、prettier 格式化 |
| **组件来源** | 只有 shadcn 官方组件集                                       | 任意 registry：shadcn、vue-bits、react-bits，甚至你自己搭建私有组件注册表 |
| **典型命令** | `npx shadcn@latest add button`                               | `npx jsrepo@latest add vue-bits/components/GradientButton`（就是你刚才 VueBits 用的命令） |
| **配置文件** | `components.json`                                            | `jsrepo.config.ts`，功能更强，支持 transform、多 provider    |

### shadcn

### jsrepo
