## 段错误 (核心已转储)

**别名：segmentation fault**

我在使用pandas的时候发现 `read_excel('xxx.xlsx')` 函数老是报错

1. `read_csv` 没问题
2. `read_excel('xxx.xls')` 没问题

最后不断排查，发现这行代码出了问题：`from rdkit.Chem import Draw`，于是我把 rdkit 的库直接回滚到 2024 年的版本 `2024.9.6`，终于解决了呜呜呜~