# 《流畅的python》学习笔记

[TOC]

## 写在前面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210427111207381.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 读后感

  1. 翻译满昏！绝对满昏！:100:，你看下面黄色部分，这翻译绝了，感觉我才是文化沙漠，什么“亲者快，仇者恨”，我这辈子没见过这么高级的用法。

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210427111042881.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)



## 1. Python数据模型

1. `collections.nametuple`：用来构建只有少数属性但是没有方法的对象，比如数据库条目。

2. `__getitem__`：方法可以实现切片效果

   ```python
   def __getitem__(self, position):
           return self._cards[position]
   ```

### 1.1 特殊方法

1. 如何使用特殊方法

   1. 首先，特殊方法的存在是为了被python解析器调用的，而不是被我们调用的

   2. 其次，`my_object.__len__()`这种写法应该修正为`len(my_object)`，在执行`len(my_object)`的时候，如果my_object是一个自定义类的对象，那么python会自己去调用其中的，由我们自己实现的`__len__`方法

   3. 如果是python内置的类型，如列表list、字符串str、字节序列bytearray等，Cpython会抄近道，`__len__`实际上会直接返回PyVarObject里的ob_size属性。其中`PyVarObject`表示内存中长度可变的内置对象的C语言结构体。

      直接读取这个值比调用一个方法要快很多。

   4. 很多时候，特殊方法的调用是隐式的，比如`for i in x`这个语句，背后其实调用的是`iter(x)`，而这个函数的背后则是`x.__iter__()`方法。（前提是这个方法在x中被实现了）

   5. 不要想当然的随意添加特殊方法，说不定以后python会用到这个名字。

2. `repr`：能把一个对象用字符串的形式表达出来以便辨认，「字符串表示形式」。`__repr__` 所返回的字符串应该准确、无歧义，并且尽可能表达出如何用代码创建出这个被打印的对象。

   `__repr__`和`__str__`的区别在于，后者是在`str()`函数被使用，或者是在用`print`函数打印一个对象的时候才能被调用的，并且它返回的字符串对终端用户更友好。

   如果你只想实现这两个特殊方法中的一个，`__repr__` 是更好的选择，因为如果一个对象没有 `__str__` 函数，而 Python 又需要调用它的时候，解释器会用 `__repr__` 作为替代。
   
3. `bool(x)` 的背后是调用 `x.__bool__()` 的结果；如果不存在 `__bool__` 方法，那么 `bool(x)` 会尝试调用 `x.__len__()`。若返回 0，则 bool 会返回 False；否则返回True。

4. 跟运算符无关的特殊方法

   1. 字符串/字节序列表示形式：`__repr__`、`__str__`、`__format__`、`__bytes__`
   2. 数值转换：`__abs__`、`__bool__`、`__complex__`、`__int__`、`__float__`、`__hash__`、`__index__`
   3. 集合模拟：`__len__`、`__getitem__`、`__setitem__`、`__delitem__`、`__contains__`
   4. 迭代枚举：`__iter__`、`__reversed__`、`__next__`
   5. 可调用模拟：`__call__`
   6. 上下文管理器：`__enter__`、`__exit__`
   7. 实例创建和销毁：`__new__`、`__init__`、`__del__`
   8. 属性管理：`__getattr__`、`__getattribute__`、`__setattr__`、`__delattr__`、`__dir__`
   9. 属性描述符：`__get__`、`__set__`、`__delete__`
   10. 跟类相关的服务：`__prepare__`、`__instancecheck__`、`__subclasscheck__`
   
5. 跟运算符相关的特殊方pos法

   1. 一元运算符：`__neg__`（`-`）、`__pos__`（`+`）、`__abs__`（`abs()`）
   2. 众多比较运算符：`__lt__`（`<`）、`__le__`（`<=`）、`__eq__`（`==`）、`__ne__`（`!=`）、`__gt__`（`>`）、`__ge__`（`>=`）
   3. 算数运算符：`__add__`（`+`）、`__sub__`（`-`）、`__mul__`（`*`）、`__truediv__`（`/`）、`__floordiv__`（`//`）、`__mod__`（`%`）、`__divmod__`（`divmod()`）、`__pow__`（`**`或`pow()`）、`__round__`（`round()`）
   4. 反向算数运算符：`__radd__`、`__rsub__`、`__rmul__`、`__rtruediv__`、`__rfloordiv__`、`__rmod__`、`__rdivmod__`
   5. 增量赋值算数运算符：`__iadd__`、`__isub__`、`__imul__`、`__itruediv__`、`__ifloordiv__`、`__imod__`、`__ipow__`
   6. 位运算符：`__invert__`（`~`）、`__lshift__`（`<<`）、`__rshift__`（`>>`）、`__and__`（`&`）、`__or__`（`|`）、`__xor__`（`^`）
   7. 反向位运算符：`__rlshift__`、`__rrshift__`、`__rand__`、`__rxor__`、`__ror__`
   8. 增量赋值位运算符：`__ilshift__`、`__irshift__`、`__iand__`、`__ixor__`、`__ior__`
   
6. 为什么len不是一个普通方法：「实用胜于纯粹」，如果 x 是一个内置类型的实例，那么 `len(x)` 的速度会非常快。背后的原因是 CPython 会直接从一个 C 结构体里读取对象的长度，完全不会调用任何方法。获取一个集合中元素的数量是一个很常见的操作，在
    `str、list、memoryview` 等类型上，这个操作必须高效。

  换句话说，len 之所以不是一个普通方法，是为了让 Python 自带的数据结构可以走后门，abs 也是同理。但是多亏了它是特殊方法，我们也可以把 len 用于自定义数据类型

## 2. 序列构成的数组

### 2.1 内置序列类型

1. 容器序列：list、tuple、collections.deque。可以存放不同类型的数据。

2. 扁平序列：str、bytes、bytearray、memoryview、array.array。只能容纳一种类型。

3. 容器序列存放的是它们所包含的任意类型的对象的引用，而扁平序列里存放的是值而不是引用。换句话说，扁平序列其实是一段连续的内存空间。由此可见扁平序列其实更加紧凑，但是它里面只能存放诸如字符、字节和数值这种基础类型。

4. 可变序列：list、bytearray、array.array、collections.deque、memoryview

5. 不可变序列：tuple、str、bytes

6. 可变序列（MutableSequence）和不可变序列（Sequence）的差异

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210511172010476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 2.2 列表推导和生成器表达式

1. Python 会忽略代码里 []、{} 和 () 中的换行，因此如果你的代码里有多行的列表、列表推导、生成器表达式、字典这一类的，可以省略不太好看的续行符 \。

2. 列表推导不会再有变量泄漏的问题

   ```python
   x = 'ABC'
   dummy = [ord(x) for x in x]
   print(x, dummy)
   
   # ABC [65, 66, 67]
   ```

3. 生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已。

### 2.3 元组不仅仅是不可变的列表

1. 除了用作不可变的列表，它还可以用于没有字段名的记录。

2. 元组其实是对数据的记录：元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置。正是这个位置信息给数据赋予了意义。

3. 在元组拆包中使用 `*` 也可以帮助我们把注意力集中在元组的部分元素上。用 `*` 来处理剩下的元素

   ```python
   a, b, *rest = range(5)
   print(a, b, rest)
   
   # 0 1 [2, 3, 4]
   ```

4. 在平行赋值中，`*` 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置

   ```python
   a, *body, c, d = range(5)
   print(a, body, c, d)
   
   # 0 [1, 2] 3 4
   ```

5. `collections.namedtuple`：创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。

   1. `_fields`：一个包含这个类所有字段名称的元组。
   2. `_make()`：通过接受一个可迭代对象来生成这个类的一个实例，它的作用等价于 `类(*参数元组)`是一样的。
   3. `_asdict()`：把具名元组以 `collections.OrderedDict` 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。
   
6. 列表或元组的方法和属性

   |           函数            | 列表 | 元组 |                             描述                             |
   | :-----------------------: | :--: | :--: | :----------------------------------------------------------: |
   |      `s.__add__(s2)`      |  √   |  √   |                         `s+s2`，拼接                         |
   |     `s.__iadd__(s2)`      |  √   |  ×   |                      `s+=s2`，就地拼接                       |
   |       `s.append(e)`       |  √   |  ×   |                     在尾部添加一个新元素                     |
   |        `s.clear()`        |  √   |  ×   |                         删除所有元素                         |
   |    `s.__contains__(e)`    |  √   |  √   |                          s是否包含e                          |
   |        `s.copy()`         |  √   |  ×   |                         列表的浅复制                         |
   |       `s.count(e)`        |  √   |  √   |                       e在s中出现的次数                       |
   |    `s.__delitem__(p)`     |  √   |  ×   |                      把位于p的元素删除                       |
   |      `s.extend(it)`       |  √   |  ×   |                    把可迭代对象it追加给s                     |
   |     `s.__getitem__()`     |  √   |  √   |                   `s[p]`，获取位置p的元素                    |
   |   `s.__getnewargs__()`    |  ×   |  √   |                在pickle中支持更加优化的序列化                |
   |       `s.index(e)`        |  √   |  √   |                在s中找到元素e第一次出现的位置                |
   |      `s.insert(p,e)`      |  √   |  ×   |                     在位置p之前插入元素e                     |
   |      `s.__iter__()`       |  √   |  √   |                        获取s的迭代器                         |
   |       `s.__len__()`       |  √   |  √   |                     `len(s)`，元素的数量                     |
   |       `s.__mul__()`       |  √   |  √   |                    `s*n`，n个s的重复拼接                     |
   |      `s.__imul__()`       |  √   |  ×   |                     `s*=n`，就地重复拼接                     |
   |      `s.__rmul__()`       |  √   |  √   |                      `n*s`，反向拼接`*`                      |
   |       `s.pop([p])`        |  √   |  ×   |      删除最后或者是（可选的）位于p的元素，并返回它的值       |
   |       `s.remove(e)`       |  √   |  ×   |                     删除s中第一次出现的e                     |
   |       `s.reverse()`       |  √   |  ×   |                    就地把s的元素倒序排列                     |
   |     `s.__reversed__`      |  √   |  ×   |                      返回s的倒序迭代器                       |
   |   `s.__setitem__(p,e)`    |  √   |  ×   |     `s[p]=e`，把元素e放在位置p，替代已经在那个位置的元素     |
   | `s.sort([key],[reverse])` |  √   |  ×   | 就地对s中的元素进行排序，可选的参数有键（key）和是否倒序（reverse） |

### 2.4 切片

1. 为什么切片和区间会忽略最后一个元素：

   在切片和区间操作里不包含区间范围的最后一个元素是 Python 的风格，这个习惯符合 Python、C 和其他语言里以 0 作为起始下标的传统。这样做带来的好处如下。

   1. 当只有最后一个位置信息时，我们也可以快速看出切片和区间里有几个元素： `range(3)` 和 `my_list[:3]` 都返回 3 个元素。
   2. 当起止位置信息都可见时，我们可以快速计算出切片和区间的长度，用后一个数减去第一个下标（stop - start）即可。
   3. 这样做也让我们可以利用任意一个下标来把序列分割成不重叠的两部分，只要写成  `my_list[:x]` 和 `my_list[x:]` 就可以了。
   
2. `slice(a, b, c)`：对 `seq[start:stop:step]` 进行求值的时候，Python 会调用 `seq.__getitem__(slice(start, stop, step))`。

3. `slice(start, stop, step)`：使用方法

   ```python
   a = slice(6, 40)
   item[a]
   ```

4. 










学到 p89 2.4.3

------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的Gitee：https://gitee.com/li_yingjun
- :palm_tree: 我的bilibili：https://space.bilibili.com/8182822

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
