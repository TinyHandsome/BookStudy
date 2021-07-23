# 《流畅的python》学习笔记

[TOC]

## 写在前面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210427111207381.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 读后感 **优点**：

  1. 翻译满昏！绝对满昏！:100:，你看下面黄色部分，这翻译绝了，感觉我才是文化沙漠，什么“亲者快，仇者痛”，我这辈子没见过这么高级的用法。

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210427111042881.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
     
  2. 我被作者举的例子惊到了（见2.4），真的很有水平，翻译和作者本身都很厉害

     比如下面这一句

     ```python
     t = (1, 2, [30, 40])
     t[2] += [50, 60]
     ```

     这两行代码的执行结果：

     1. 抛出异常：`因为 tuple 不支持对它的元素赋值，所以会抛出 TypeError 异常。`
     2. `t[2]` 的值发生了修改：`t = (1, 2, [30, 40, 50, 60])`
     
  3. 在讲排序的时候，讲到`sorted`和`list.sort`背后使用的排序算法是Timsort，这个算法的作者是Tim Peters

     - 这个算法的相关代码在Google对Sun的侵权案中，当作了呈堂证供。
     - 这个算法的作者也是`import this`，**python之禅**的作者。
     - 我靠，太离谱了，世界线收束，鸡皮疙瘩都起来了。

  4. 每一章的小结真的写的太好了，方便回顾这一章讲了啥，也方便自己查漏补缺。

  5. 延伸阅读也是惊艳啊，作者很明显博览群书，基础扎实。

  6. 作者吹了一波《Python Cookbook（第三版）》和《Python Cookbook（第二版）》，我准备去学习学习！

  7. 作者每章的小结写的很不错，每次因为知识点需要复查书籍的时候，可以先看对应章节的 **本章小结** ，再查。

-  读后感 **缺点**：

   1. 读到11章和12章的时候，就开始有点吃力了，不知道是不是我的知识储备不够。一些抽象的知识点作者和翻译都有点力不从心（作为读者的角度），就是好像作者想把这个点用比喻的方式说清楚，但是又很难把他心中的理解表达出来，甚至很多地方都是直接进行教条化的描述，对于翻译来说，就更困难了。

      【对不起，我面向对象学的太差了呜呜呜】

      比如 P540 中：**优先使用对象组合，而不是类继承**，还有，**组合和委托可以代替混入，把行为提供给不同的类，但是不能取代接口继承去定义类型层次结构。** 

      对于 **组合、委托、混入、继承**等名词的解释不够到位，这几个名词，我就对继承还可以有深入的理解，其他的三个名词出现的时候，一脸懵逼

- 传送门：
  
  1. [列表、元组、数组、双向队列的方法和属性](#1)
  2. [`dict`、`collections.defaultdict`和`collections.OrderedDict`的方法列表](#2)
  3. [集合的数学运算、集合的比较运算符、集合类型的其他方法](#3)
  4. [用户定义函数的属性](#4)
  5. [利用`inspect.signature`提取函数签名](#5)

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
   
6. <a name='1'>列表、元组、数组、双向队列的方法和属性</a>

   |        方法和属性         | 列表 | 元组 | 数组 | 双向队列 |                             描述                             |
   | :-----------------------: | :--: | :--: | ---- | -------- | :----------------------------------------------------------: |
   |      `s.__add__(s2)`      |  √   |  √   | √    | ×        |                         `s+s2`，拼接                         |
   |     `s.__iadd__(s2)`      |  √   |  ×   | √    | √        |                      `s+=s2`，就地拼接                       |
   |       `s.append(e)`       |  √   |  ×   | √    | √        |                     在尾部添加一个新元素                     |
   |     `s.appendleft(e)`     |  ×   |  ×   | ×    | √        |           添加一个元素到最左侧（到第一个元素之前）           |
   |       `s.byteswap`        |  ×   |  ×   | √    | ×        |          翻转数组内每个元素的字节序列，转换字节序列          |
   |        `s.clear()`        |  √   |  ×   | ×    | √        |                         删除所有元素                         |
   |    `s.__contains__(e)`    |  √   |  √   | √    | ×        |                          s是否包含e                          |
   |        `s.copy()`         |  √   |  ×   | ×    | ×        |                         列表的浅复制                         |
   |      `s.__copy__()`       |  ×   |  ×   | √    | √        |                对`copy.copy`（浅复制）的支持                 |
   |       `s.count(e)`        |  √   |  √   | √    | √        |                       e在s中出现的次数                       |
   |    `s.__deepcopy__()`     |  ×   |  ×   | √    | ×        |              对`copy.deepcopy`（深复制）的支持               |
   |    `s.__delitem__(p)`     |  √   |  ×   | √    | √        |                      把位于p的元素删除                       |
   |      `s.extend(it)`       |  √   |  ×   | √    | √        |                    把可迭代对象it追加给s                     |
   |     `s.extendleft(i)`     |  ×   |  ×   | ×    | √        |               将可迭代对象i中的元素添加到头部                |
   |     `s.frombytes(b)`      |  ×   |  ×   | √    | ×        |           将压缩成机器值得字节序列读出来添加到尾部           |
   |     `s.fromfile(f,n)`     |  ×   |  ×   | √    | ×        |    将二进制文件f内含有机器值读出来添加到尾部，最多添加n项    |
   |      `s.fromlist(l)`      |  ×   |  ×   | √    | ×        | 将列表里的元素添加到尾部，如果其中任何一个元素导致了`TypeError`异常，那么所有的添加都会取消 |
   |     `s.__getitem__()`     |  √   |  √   | √    | √        |                   `s[p]`，获取位置p的元素                    |
   |   `s.__getnewargs__()`    |  ×   |  √   | ×    | ×        |                在pickle中支持更加优化的序列化                |
   |       `s.index(e)`        |  √   |  √   | √    | ×        |                在s中找到元素e第一次出现的位置                |
   |      `s.insert(p,e)`      |  √   |  ×   | √    | ×        |                     在位置p之前插入元素e                     |
   |       `s.itemsize`        |  ×   |  ×   | √    | ×        |                数组中每个元素的长度是几个字节                |
   |      `s.__iter__()`       |  √   |  √   | √    | √        |                        获取s的迭代器                         |
   |       `s.__len__()`       |  √   |  √   | √    | √        |                     `len(s)`，元素的数量                     |
   |       `s.__mul__()`       |  √   |  √   | √    | ×        |                    `s*n`，n个s的重复拼接                     |
   |      `s.__imul__()`       |  √   |  ×   | √    | ×        |                     `s*=n`，就地重复拼接                     |
   |      `s.__rmul__()`       |  √   |  √   | √    | ×        |                      `n*s`，反向拼接`*`                      |
   |       `s.pop([p])`        |  √   |  ×   | √    | √        | 删除最后或者是（可选的）位于p的元素，并返回它的值（注意，在双向队列中不接受参数） |
   |       `s.popleft()`       |  ×   |  ×   | ×    | √        |                  移除第一个元素并返回它的值                  |
   |       `s.remove(e)`       |  √   |  ×   | √    | √        |                     删除s中第一次出现的e                     |
   |       `s.reverse()`       |  √   |  ×   | √    | √        |                    就地把s的元素倒序排列                     |
   |     `s.__reversed__`      |  √   |  ×   | ×    | √        |                      返回s的倒序迭代器                       |
   |       `s.rotate(n)`       |  ×   |  ×   | ×    | √        |               把n个元素从队列的一段移到另一端                |
   |   `s.__setitem__(p,e)`    |  √   |  ×   | √    | √        |     `s[p]=e`，把元素e放在位置p，替代已经在那个位置的元素     |
   | `s.sort([key],[reverse])` |  √   |  ×   | ×    | ×        | 就地对s中的元素进行排序，可选的参数有键（key）和是否倒序（reverse） |
   |       `s.tobytes()`       |  ×   |  ×   | √    | ×        |           把所有元素的机器值用bytes对象的形式返回            |
   |       `s.tofile(f)`       |  ×   |  ×   | √    | ×        |             把所有元素以机器值的形式写入一个文件             |
   |       `s.tolist()`        |  ×   |  ×   | √    | ×        |         把数组转换成列表，列表里的元素类型是数字对象         |
   |       `s.typecode`        |  ×   |  ×   | √    | ×        |    返回只有一个字符的字符串，代表数组元素在C语言中的类型     |

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

4. 多维切片：如果要得到 `a[i, j]` 的值，Python 会调用 `a.__getitem__((i, j))`

5. `x[i, ...]`：`x[i, :, :, :]`的缩写

6. 给切片赋值：如果把切片放在赋值语句的左边，或把它作为 `del` 操作的对象，我们就可以对序列进行 **嫁接** 、 **切除** 或 **就地修改** 操作。

   1. 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。
   2. 即便只有单独一个值，也要把它转换成可迭代的序列。

### 2.5 增量赋值

1. `+`和`*`的陷阱：如果要生成二维序列：

   1. 不能：`[['_']*3]*3`
   2. 而要：`[['_']*3 for i in range(3)]`

2. `a += b`

   1. 如果a实现了 `__iadd__` 方法，就相当于调用了 `a.extend(b)`
   2. 如果a没有实现 `__iadd__` 的话， `a += b` 就跟 `a = a + b` 一样了。首先计算 `a + b` ，得到一个新的对象，然后赋值给a。
   3. 也就是说，在这个表达式中，变量名会不会被关联到新的对象，完全取决于这个类型有没有实现 `__iadd__` 方法。

3. 对不可变序列进行重复拼接操作的话，效率会很低，因为每次都有一个新对象，而解释器需要把原来对象中的元素先赋值到新的对象里，然后再追加新的元素。

   > `str`是一个例外，因为对字符串做`+=`实在是太普遍了，所以CPython对它做了优化，为str初始化内存的时候，程序会为它留出额外的可扩展空间，因此进行增量操作的时候，并不会涉及复制原有字符串到新位置这类操作。

### 2.6 排序

1. Python中的排序算法：**Timesort** 是稳定的，意思是就算两个元素比不出大小，在每次排序的结果里他们的相对位置是固定的。

2. `list.sort`：就地排序列表，也就是说不会把原列表复制一份，返回值为`None`

3. `sorted`：会新建一个列表作为返回值

4. `key`参数能让你对一个混有数字字符和数值的列表进行排序。

   ```python
   l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
   sorted(l, key=int)
   
   # [0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
   ```

5. `sorted` 和 `list.sort` 背后的排序算法是 Timsort，它是一种自适应算法，会根据原始数据的顺序特点交替使用**插入排序**和**归并排序**，以达到最佳效率。这样的算法被证明是很有效的，因为来自真实世界的数据通常是有一定的顺序特点的。

6. 用`bisect`来管理 **已排序** 的序列：二分法

   1. `bisect` 函数其实是 `bisect_right` 函数的别名，后者还有个姊妹函数叫 `bisect_left`
   2. `bisect_left` 返回的插入位置是原序列中跟被插入元素相等的元素的位置，也就是新元素会被放置于它相等的元素的前面
   3. `bisect_right` 返回的则是跟它相等的元素之后的位置

7. 利用`bisect`进行评价分组

   ```python
   def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
       i = bisect.bisect(breakpoints, score)
       return grades[i]
   [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
   
   # ['F', 'A', 'C', 'C', 'B', 'A', 'A']
   ```

8. `bisect.insort(seq, item)`把变量item插入到序列seq中，并能保持seq的升序顺序。

### 2.7 数组、内存视图、NumPy和队列

1. 如果我们需要一个只包含数字的列表，那么 `array.array` 比 `list` 更高效。通过`array.tofile`和`array.fromfile`进行文件的保存和读取。
2. `memoryview`：是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片。
3. `memoryview.cast`的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容字节不会随意移动。`memoryview.cast`会把同一块内存里的内容打包成一个全新的`memoryview`对象给你。
4. `numpy`：
   1. 将一维数组转化为二维：`array.shape=(x, y)`
   2. 将数组转置：`array.T`、`array.transpose()`
5. `collections.deque`类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。
6. `dq = deque(range(10), maxlen=10)`，`maxlen`是一个可选参数，带别找个队列可以容纳的元素的数量。
7. `dq.rotate(n)`：队列的旋转操作接受一个参数n，当n>0时，队列的最右边的n个元素会被移动到队列的左边。当n<0时，最左边的n个元素会被移动到右边。
8. `append` 和` popleft` 都是原子操作，也就说是 deque 可以在多线程程序中安全地当作先进先出的栈使用，而使用者不需要担心资源锁的问题。
9. 其他队列的实现：
   1. `queue`提供了`Queue`、`LifoQueue`、`PriorityQueue`。在满员的时候，这些类不会扔掉旧的元素来腾出位置。相反，如果队列满了，它就会被锁住，直到另外的线程移除了某个元素而腾出了位置。这一特性让这些类很适合用来控制活跃线程的数量。
   2. `multiprocessing`实现了自己的Queue，跟`queue.Queue`相似，是涉及给进程间通信用的。`multiprocessing.JoinableQueue`可以让任务管理变得更方便。
   3. `asyncio`里面有`Queue`、`LifoQueue`、`PriorityQueue`、`JoinableQueue`，这些类受到`queue`和`multiprocessing`模块的影响，但是为异步编程里的任务管理提供了专门的便利。
   4. `heapq`没有队列类，而是提供了`heappush`和`heappop`方法，让用户可以把可变序列当作堆队列或者优先队列来使用。
10. 列表倾向于存放有通用特性的元素；元组则恰恰相反，经常用来存放不同类型的元素。

## 3. 字典和集合

### 3.1 泛映射类型和字典推导

1. `collections.abc` 模块中有 `Mapping` 和 `MutableMapping` 这两个抽象基类，它们的作用是为 dict 和其他类似的类型定义形式接口

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210518150731924.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 可散列的数据类型（hashable）

   如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现 `__hash__()` 方法。另外可散列对象还要有 `__eq__()` 方法，这样才能跟其他键做比较。如果两个可散列对象是相等的，那么它们的散列值一定是一样的。
   
   简单来说，**如果一个对象是可散列的数据类型的话，那它应是不可变的。**
   
3. list等可变对象是不可散列的，因为随着数据的改变他们的哈希值会变化导致进入错误的哈希表。

4. 元组的话，只有当一个元组包含的所有元素都是可散列类型的情况下，它才是可散列的。

5. 一般用户自定义的类型的对象都是可散列的，散列值就是它们的`id()`函数的返回值，所以所有这些对象在比较的时候都是不相等的。如果一个对象实现了 `__eq__()` 方法，并且在方法中用到了这个对象的内部状态的话，那么只有当所有这些内部状态都是不可变的情况下，这个对象才是可散列的。

6. **~~Python 里所有的不可变类型都是可散列的~~**，这个说法其实是不准确的，比如虽然元组本身是不可变序列，它里面的元素可能是其他可变类型的引用。

7. 字典推导：

   ```python
   {code: country.upper() for country, code in country_code.items() if code < 66}
   ```

### 3.2 常见的映射方法

<a name='2'>`dict`、`collections.defaultdict`和`collections.OrderedDict`的方法列表</a>

|             方法             | dict | defaultdict | OrderedDIct |                             描述                             |
| :--------------------------: | :--: | :---------: | :---------: | :----------------------------------------------------------: |
|         `d.clear()`          |  √   |      √      |      √      |                         移除所有元素                         |
|     `d.__contains__(k)`      |  √   |      √      |      √      |                        检查k是否在d中                        |
|          `d.copy()`          |  √   |      √      |      √      |                            浅复制                            |
|        `d.__copy()__`        |  ×   |      √      |      ×      |                     用于支持`copy.copy`                      |
|     `d.default_factory`      |  ×   |      √      |      ×      | 在`__missing__`函数中被调用的函数，用以给未找到的元素设置值  |
|      `d.__delitem__(k)`      |  √   |      √      |      √      |                 `del d[k]`，移除键位k的元素                  |
| `d.fromkeys(it, [initial])`  |  √   |      √      |      √      | 将迭代器it里的元素设置为映射里的键，如果initial参数，就把它作为这些键对应的值（默认是None） |
|    `d.get(k, [default])`     |  √   |      √      |      √      |  返回键k对应的值，如果字典里没有键k，则返回None或者default   |
|      `d.__getitem__(k)`      |  √   |      √      |      √      |            让字典d能用`d[k]`的形式返回键k对应的值            |
|         `d.items()`          |  √   |      √      |      √      |                     返回d里所有的键值对                      |
|        `d.__iter__()`        |  √   |      √      |      √      |                        获取键的迭代器                        |
|          `d.keys()`          |  √   |      √      |      √      |                         获取所有的键                         |
|        `d.__len__()`         |  √   |      √      |      √      |          可以用`len(d)`的形式得到字典里键值对的数量          |
|      `d.__missing__(k)`      |  ×   |      √      |      ×      |     当`__getitem__`找不到对应键的时候，这个方法会被调用      |
|  `d.move_to_end(k, [last])`  |  ×   |      ×      |      √      | 把键位k的元素移动到最靠前或者最靠后的位置（last的默认值是True） |
|    `d.pop(k, [default])`     |  √   |      √      |      √      | 返回键k所对应的值，然后移除这个键值对。如果没有这个键，返回None或者default |
|        `d.popitem()`         |  √   |      √      |      √      |              随机返回一个键值对并从字典里移除它              |
|      `d.__reversed__()`      |  ×   |      ×      |      √      |                     返回倒序的键的迭代器                     |
| `d.setdefault(k, [default])` |  √   |      √      |      √      | 若字典里有键k，则把它对应的值设置位default，然后返回这个值；若无，则让`d[k]=default`，然后返回default |
|       `d.__setitem__`        |  √   |      √      |      √      |              实现`d[k]=v`操作，把k对应的值设为v              |
|  `d.update(m, [**kwargs])`   |  √   |      √      |      √      |      m可以是映射或者键值对迭代器，用来更新d里对应的条目      |
|          `d.values`          |  √   |      √      |      √      |                      返回字典里的所有值                      |

1. 用setdefault处理找不到的键

   - 使用`d.get(k, default)`来代替`d[k]`，可以防止报错

   - 字典处理优化

     - 好的方法

       ```python
       my_dict.setdefault(key, []).append(new_value)
       ```

     - 差的方法

       ```python
       if key not in my_dict:
       	my_dict[key] = []
       my_dict[key].append(new_value)
       ```

     - 二者的效果是一样的，只不过后者至少要进行两次键查询——如果键不存在的话，就是三次，用`setdefault`只需要一次就可以完成整个操作。

### 3.3 映射的弹性键查询

1. 场景：有时候为了方便起见，就算某个键在映射里不存在，我们也希望在通过这个键读取值的时候能得到一个默认值。

2. 方法：

   1. `collections.defaultdict`类

      - 把list构造方法作为`default_factory`来创建一个`defaultdict`
      - 如果在创建`defaultdict`的时候没有指定`default_factory`，查询不存在的键会触发KeyError
      - `defaultdict`里的`default_factory`只会在`__getitem__`里被调用，在其他的方法里完全不会发挥作用。比如`dd[k]`会创建默认值并返回该默认值，`dd.get(k)`就会返回None
      - 所有这一切的背后是基于特殊方法`__missing__`实现的，它会在`defaultdict`遇到找不到的键的时候调用`default_factory`，而实际上这个特性是所有映射类型都可以选择去支持的

      ```python
      """创建一个从单词到其出现情况的映射"""
      
      import sys
      import re
      from collections import defaultdict
      
      WORD_RE = re.compile(r'\w+')
      
      # index = {}
      index = defaultdict(list)
      with open(sys.argv[1], encoding='utf-8') as fp:
          for line_no, line in enumerate(fp, 1):
              for match in WORD_RE.finditer(line):
                  word = match.group()
                  column_no = match.start() + 1
                  location = (line_no, column_no)
                  
                  ''' 这其实是一种很不好的实现，这样写只是为了证明论点
                  occurrences = index.get(word, [])
                  occurrences.append(location)
                  index[word] = occurrences
                  '''
                  
                  ''' 下面是好的实现，用到了setdefault函数
                  index.setdefault(word, []).append(location)
                  '''
                  
                  ''' 通过collections.defaultdict实现，取得key没有的时候，新建这个key，并赋予默认值'''
                  index[word].append(location)
                  
      # 以字母顺序打印出结果
      for word in sorted(index, key=str.upper):
          print(word, index[word])
      ```

   2. 自定义一个`dict`子类，然后在子类中实现`__missing__`方法

      - 像`k in my_dict.keys()`这种操作在Python3中是很快的，而且即便映射类型对象很庞大也没关系。这是因为`dict.keys()`的返回值是一个**视图**。

      - **视图**就像一个**集合**，而且跟字典类似的是，在视图里查找一个元素的速度很快。

        ```python
        class StrKeyDict0(dict):
            def __missing__(self, key):
                if isinstance(key, str):
                    raise KeyError(key)
                return self[str(key)]
            
            def get(self, key, default=None):
                try:
                    return self[key]
                except KeyError:
                    return default
            def __contains__(self, key):
                return key in self.keys() or str(key) in self.keys()
        ```

### 3.4 字典的变种

1. `collections.OrderedDict`：这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的。`OrderedDict` 的 `popitem `方法默认删除并返回的是字典里的最后一个元素，但是如果像 `my_odict.popitem(last=False)` 这样调用它，那么它删除并返回第一个被添加进去的元素。

2. `collections.ChainMap`：该类型可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当作一个整体被逐个查找，直到键被找到为止。这个功能在给有嵌套作用域的语言做解释器的时候很有用，可以用一个映射对象来代表一个作用域的上下文。

3. `collections.Counter`：这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器。所以这个类型可以用来给可散列表对象计数，或者是当成多重集来用——多重集合就是集合里的元素可以出现不止一次。

4. `my_dict.most_common(n)`：统计字典中出现次数最多的数据

   ```python
   ct = Counter({'a': 10, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 3})
   ct.most_common(2)
   
   # [('a', 10), ('z', 3)]
   ```

5. `colllections.UserDict`：这个类其实就是把标准 `dict` 用纯 Python 又实现了一遍。跟 `OrderedDict`、`ChainMap `和 `Counter `这些开箱即用的类型不同，`UserDict `是让用户继承写子类的。

   - 更倾向于从 `UserDict `而不是从 `dict `继承的主要原因是，后者有时会在某些方法的实现上走一些捷径，导致我们不得不在它的子类中重写这些方法，但是 UserDict 就不会带来这些问题。

6. 不可变映射类型：`types.MappingProxyType`。如果给这个类一个映射，它会返回一个只读的映射视图。虽然是个只读视图，但是它是动态的。这意味着如果对原映射做出了改动，我们通过这个视图可以观察到，但是无法通过这个视图对原映射做出修改。

### 3.5 集合

1. 集合可以去重

2. 集合中的元素必须是可散列的，set 类型本身是不可散列的，但是frozenset 可以。因此可以创建一个包含不同 frozenset 的 set。

3. 求交集：`&`，`intersection`

4. 空集：`set()`，而不是`{}`，因为`{}`是一个空字典

5. 除了空集，集合的字符串表示形式总是以`{...}`的形式出现。

6. `{1, 2, 3}`的速度快于`set([1, 2, 3])`，因为后者的话，Python必须先从set这个名字来查询构造方法，然后新建一个列表，最后再把这个列表传入到构造方法里。但是如果是像 `{1, 2, 3 ` 这样的字面量，Python 会利用一个专门的叫作 BUILD_SET 的字节码来创建集合。

7. MutableSet和它的超类的UML类图

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210521144908383.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

8. <a name='3'>集合的数学运算</a>：这些方法或者会生成新集合，或者会在条件允许的情况下就地修改集合

   |    数学符号     | Python运算符 |                   方法                   |                             描述                             |
   | :-------------: | :----------: | :--------------------------------------: | :----------------------------------------------------------: |
   |   $S \cap Z$    |    `s&z`     |              `s.__and__(z)`              |                          s和z的交集                          |
   |   $S \cap Z$    |    `z&s`     |             `s.__rand__(z)`              |                          反向&操作                           |
   |   $S \cap Z$    |    `z&s`     |        `s.intersection(it, ...)`         |  把可迭代的it和其他所有参数转化为集合，然后求它们与s的交集   |
   |   $S \cap Z$    |    `s&=z`    |             `s.__iand__(z)`              |                     把s更新为s和z的交集                      |
   |   $S \cap Z$    |    `s&=z`    |     `s.intersection_update(it, ...)`     | 把可迭代的it和其他所有参数转化为集合，然后求得它们与s的交集，然后把s更新成这个交集 |
   |   $S \cup Z$    |    `s|z`     |              `s.__or__(z)`               |                          s和z的并集                          |
   |   $S \cup Z$    |    `z|s`     |              `s.__ror__(z)`              |                         \|的反向操作                         |
   |   $S \cup Z$    |    `z|s`     |            `s.union(it, ...)`            |  把可迭代的it和其他所有参数转化为集合，然后求它们和s的并集   |
   |   $S \cup Z$    |    `s|=z`    |              `s.__ior__(z)`              |                     把s更新为s和z的并集                      |
   |   $S \cup Z$    |    `s|=z`    |           `s.update(it, ...)`            | 把可迭代的it和其他所有参数转化为集合，然后求它们和s的并集，并把s更新成这个并集 |
   | $S \setminus Z$ |    `s-z`     |              `s.__sub__(z)`              |                 s和z的差集，或者叫作相对补集                 |
   | $S \setminus Z$ |    `z-s`     |             `s.__rsub__(z)`              |                         -的反向操作                          |
   | $S \setminus Z$ |    `z-s`     |         `s.difference(it, ...)`          |  把可迭代的it和其他所有参数转化为集合，然后求它们和s的差集   |
   | $S \setminus Z$ |    `s-=z`    |             `s.__isub__(z)`              |                     把s更新为它与z的差集                     |
   | $S \setminus Z$ |    `s-=z`    |      `s.difference_update(it, ...)`      | 把可迭代的it和其他所有参数转化为集合，求它们和s的差集，然后把s更新成这个差集 |
   | $S \setminus Z$ |    `s-=z`    |       `s.symmetric_difference(it)`       |                    求s和set(it)的对称差集                    |
   | $S \bigoplus Z$ |    `s^z`     |              `s.__xor__(z)`              |                       求s和z的对称差集                       |
   | $S \bigoplus Z$ |    `z^s`     |             `s.__rxor__(z)`              |                         ^的反向操作                          |
   | $S \bigoplus Z$ |    `z^s`     | `s.symmetric_difference_update(it, ...)` | 把可迭代的it和其他所有参数转化为集合，然后求它们和s的对称差集，最后把s更新成该结果 |
   | $S \bigoplus Z$ |    `s^=z`    |             `s.__ixor__(z)`              |                   把s更新成它与z的对称差集                   |

9. 集合的比较运算符，返回值是布尔类型

   |    数学符号     | Python运算符 |        方法         |                      描述                       |
   | :-------------: | :----------: | :-----------------: | :---------------------------------------------: |
   |                 |              |  `s.isdisjoint(z)`  |       查看s和z是否不相交（没有共同元素）        |
   |    $e \in S$    |   `e in s`   | `s.__contains__(e)` |                 元素e是否属于s                  |
   | $S \subseteq Z$ |   `s <= z`   |    `s.__le__(z)`    |                 s是否为z的子集                  |
   | $S \subseteq Z$ |   `s <= z`   |  `s.issubset(it)`   | 把可迭代的it转化为集合，然后查看s是否为它的子集 |
   |  $S \subset Z$  |   `s < z`    |    `s.__lt__(z)`    |                s是否为z的真子集                 |
   | $S \supseteq Z$ |   `s >= z`   |    `s.__ge__(z)`    |                 s是否为z的父集                  |
   | $S \supseteq Z$ |   `s >= z`   | `s.issuperset(it)`  | 把可迭代的it转化为集合，然后查看s是否为它的父集 |
   |  $S \supset Z$  |   `s > z`    |    `s.__gt__(z)`    |                s是否为z的真父集                 |

10. 集合类型的其他方法

    |      方法      | set  | frozenset |                            描述                            |
    | :------------: | :--: | :-------: | :--------------------------------------------------------: |
    |   `s.add(e)`   |  √   |     ×     |                      把元素e添加到s中                      |
    |  `s.clear()`   |  √   |     ×     |                    移除掉s中的所有元素                     |
    |   `s.copy()`   |  √   |     √     |                         对s浅复制                          |
    | `s.discard(e)` |  √   |     ×     |              如果s里有e这个元素的话，把它移除              |
    | `s.__iter__()` |  √   |     √     |                       返回s的迭代器                        |
    | `s.__len__()`  |  √   |     √     |                           len(s)                           |
    |   `s.pop()`    |  √   |     ×     | 从s中移除一个元素并返回它的值，若s为空，则抛出KeyError异常 |
    | `s.remove(e)`  |  √   |     ×     |     从s中移除e元素，若e元素不存在，则抛出KeyError异常      |

### 3.6 dict和set的背后

1. 如果两个对象在比较的时候相等，那么它们的散列值必须相等。

2. 散列函数用于将键值经过处理后转化为散列值。具有以下特性：

   1. 散列函数计算得到的散列值是非负整数
   2. 如果 key1 == key2，则 hash(key1) == hash(key2)
   3. 如果 key1 != key2，则 hash(key1) != hash(key2)

3. **散列冲突**：简单来说，指的是 key1 != key2 的情况下，通过散列函数处理，hash(key1) == hash(key2)，这个时候，我们说发生了**散列冲突**。设计再好的散列函数也无法避免散列冲突，原因是散列值是非负整数，总量是有限的，但是现实世界中要处理的键值是无限的，将无限的数据映射到有限的集合，肯定避免不了冲突。

4. 从字典中取值的算法流程图

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210521160825883.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

5. 用元组取代字典就能节省空间的原因有两个：

   1. 是避免了散列表所耗费的空间
   2. 无需把记录中字段的名字在每个元素里都存一遍

6. 在用户自定义的类型中，`__slots__`属性可以改变实例属性的存储方式，由dict变成tuple

7. 使用散列表给dict带来的优势和限制都有哪些

   1. 键必须是可散列的

   2. 字典在内存上的开销巨大

   3. 键查询很快

   4. 键的次序取决于添加顺序

   5. 往字典里添加新键可能会改变已有键的顺序

      无论何时往字典里添加新的键，Python 解释器都可能做出为字典扩容的决定。扩容导致的结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化。

8. 集合的特点：

   1. 集合里的元素必须是可散列的
   2. 集合很消耗内存
   3. 可以很高效地判断元素是否存在于某个集合
   4. 元素的次序取决于被添加到集合里的次序
   5. 往集合里添加元素，可能会改变集合里已有元素的次序

## 4. 文本和字节序列

### 4.1 字符和字节

1. 把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是解码。

2. 把字节序列变成人类可读的文本字符串就是解码（`decode`），而把字符串变成用于存储或传输的字节序列就是编码（`encode`）。

3. `bytes`对象可以从`str`对象使用给定的编码构造，各个元素是`range(256)`内的整数。`bytes`对象的切片还是`bytes`对象，即使是只有一个字符的切片。

4. `bytearray`对象没有字面量句法，而是以`bytearray()`和字节序列字面量参数的形式显示。`bytearray`对象的切片还是`bytearray`对象。

5. 这里比较特殊，因为`my_bytes[0]`获取的是一个整数，而`my_bytes[:1]`返回的是一个长度为1的`bytes`对象。

6. 虽然二进制序列其实是整数序列，但是它们的字面量表示法表明其中有ASCII 文本。因此，各个字节的值可能会使用下列三种不同的方式显示。

   1. 可打印的 ASCII 范围内的字节（从空格到 ~），使用 ASCII 字符本身。
   2. 制表符、换行符、回车符和 `\` 对应的字节，使用转义序列`\t`、`\n`、`\r`和 `\\`。
   3. 其他字节的值，使用十六进制转义序列（例如，`\x00`是空字节）。

7. 二进制序列有个类方法是 `str` 没有的，名为 `fromhex`，它的作用是解析十六进制数字对（数字对之间的空格是可选的），构建二进制序列：

   ```python
   bytes.fromhex('31 4B CE A9')
   # b'1K\xce\xa9'
   ```

8.  使用缓冲类对象构建二进制序列是一种低层操作，可能涉及类型转换：

   ```python
   import array
   numbers = array.array('h', [-2, -1, 0, 1, 2])
   octets = bytes(numbers)
   
   # b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
   ```

9. 使用缓冲类对象创建 `bytes` 或 `bytearray` 对象时，始终**复制**源对象中的字节序列。与之相反，`memoryview` 对象允许在二进制数据结构之间**共享内存**。

10. `memoryview `对象的切片是一个新 `memoryview`对象，而且不会
    复制字节序列

11. 如果使用 `mmap` 模块把图像打开为内存映射文件，那么会复制少量字节

### 4.2 编码和解码

1. 某些编码（如 `ASCII` 和多字节的 `GB2312`）不能表示所有 `Unicode` 字符

2. UTF 编码的设计目的就是处理每一个`Unicode` 码位

3. 典型编码：

   1. latin1（即 iso8859_1）：一种重要的编码，是其他编码的基础，例如 cp1252 和Unicode（注意，latin1 与 cp1252 的字节值是一样的，甚至连码位也相同）。
   2. cp1252：Microsoft 制定的 latin1 超集，添加了有用的符号，例如弯引号和€（欧元）；有些 Windows 应用把它称为“ANSI”，但它并不是 ANSI 标准。
   3. cp437：IBM PC 最初的字符集，包含框图符号。与后来出现的 latin1 不兼容。
   4. gb2312：用于编码简体中文的陈旧标准；这是亚洲语言中使用较广泛的多字节编码之一。
   5. utf-8：目前 Web 中最常见的 8 位编码；与 ASCII 兼容（纯 ASCII 文本是有效的 UTF-8 文本）。
   6. utf-16le：UTF-16 的 16 位编码方案的一种形式；所有 UTF-16 支持通过转义序列（称为“代理对”，surrogate pair）表示超过 U+FFFF 的码位。

4. `UnicodeEncodeError`：多数非 UTF 编解码器只能处理 Unicode 字符的一小部分子集。把文本转换成字节序列时，如果目标编码中没有定义某个字符，那就会抛出
   UnicodeEncodeError 异常，除非把 errors 参数传给编码方法或函数，对错误进行特殊处理。

   无法编码时：

   1. `error='ignore'` 处理方式悄无声息地跳过无法编码的字符；这样做通常很是不妥。
   2. 编码时指定 `error='replace'`，把无法编码的字符替换成 '?'；数据损坏了，但是用户知道出了问题。
   3. `error='xmlcharrefreplace'` 把无法编码的字符替换成 XML 实体。
   4. 编解码器的错误处理方式是可扩展的。你可以为 errors 参数注册额外的字符串，方法是把一个名称和一个错误处理函数传给 `codecs.register_error` 函数。

5. `UnicodeDecodeError`：把二进制序列转换成文本时，遇到无法转换的字节序列时会抛出UnicodeDecodeError；另一方面，很多陈旧的 8 位编码——如 'cp1252'、'iso8859_1' 和'koi8_r'——能解码任何字节序列流而不抛出错误，例如随机噪声。因此，如果程序使用错误的 8 位编码，解码过程悄无声息，而得到的是无用输出。

6. 乱码字符称为鬼符（gremlin）或 mojibake（文字化け，“变形文本”的日文）。

7. 使用预期之外的编码加载模块时抛出的SyntaxError

   1. Python 3 为所有平台设置的默认编码都是 UTF-8
   2. Python 3 允许在源码中使用非 ASCII 标识符

8. `Chardet`：识别所支持的30中编码。解决问题：如何找出字节序列的编码？

9. 二进制序列编码文本通常不会明确指明自己的编码，但是 UTF 格式可以在文本内容的开头**添加一个字节序标记**。

10. BOM：字节序标记，byte-order-mark，指明编码时使用 Intel CPU 的小字节序

11. 在小字节序设备中，各个码位的最低有效字节在前面：字母 'E' 的码位是 U+0045（十进制数 69），在字节偏移的第 2 位和第 3 位编码为 69 和0。

12. 在大字节序 CPU 中，编码顺序是相反的；'E' 编码为 0 和 69。

13. 为了避免混淆，UTF-16 编码在要编码的文本前面加上特殊的不可见字符 ZERO WIDTH NO-BREAK SPACE（U+FEFF）。在小字节序系统中，这个字符编码为 b'\xff\xfe'（十进制数 255, 254）。因为按照设计，U+FFFE 字符不存在，在小字节序编码中，字节序列 b'\xff\xfe' 必定是 ZERO WIDTH NO-BREAK SPACE，所以编解码器知道该用哪个字节
    序。

14. UTF-16 有两个变种：UTF-16LE，显式指明使用小字节序；UTF-16BE，显式指明使用大字节序。如果使用这两个变种，不会生成 BOM。

15. 与字节序有关的问题只对一个字（word）占多个字节的编码（如 UTF-16 和 UTF-32）有影响。UTF-8 的一大优势是，不管设备使用哪种字节序，生成的字节序列始终一致，因此不需要 BOM。

16. 尽管如此，某些Windows 应用（尤其是 Notepad）依然会在 UTF-8 编码的文件中添加
    BOM；而且，Excel 会根据有没有 BOM 确定文件是不是 UTF-8 编码，否则，它假设内容使用 Windows 代码页（codepage）编码。UTF-8 编码的 U+FEFF 字符是一个三字节序列：`b'\xef\xbb\xbf'`。因此，如果文件以这三个字节开头，有可能是带有 BOM 的 UTF-8 文件。然而，Python 不会因为文件以 b'\xef\xbb\xbf' 开头就自动假定它是 UTF-8编码的。

### 4.3 处理文本文件

1. 处理文本的最佳实践是 **Unicode三明治** 。

   1. 要尽早把输入（例如读取文件时）的字节序列解码成字符串。
   2. 在程序的业务逻辑中只能处理字符串对象。在其他处理过程中，一定不能编码或解码。
   3. 对输出来说，则要尽量晚地把字符串编码成字节序列。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210525093248627.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 如果打开文件是为了写入，但是没有指定编码参数，会使用区域设置中的默认编码，而且使用那个编码也能正确读取文件。

3. 如果脚本要生成文件，而字节的内容取决于平台或同一平台中的区域设置，那么就可能导致兼容问题。

4. 探索编码默认值

   ```python
   import sys, locale
   
   expressions = """
   locale.getpreferredencoding()
   type(my_file)
   my_file.encoding
   sys.stdout.isatty()
   sys.stdout.encoding
   sys.stdin.isatty()
   sys.stdin.encoding
   sys.stderr.isatty()
   sys.stderr.encoding
   sys.getdefaultencoding()
   sys.getfilesystemencoding()
   """
   
   my_file = open('dummy', 'w')
   
   for expression in expressions.split():
       
       value = eval(expression)
       print(expression.rjust(30), '->', repr(value))
   ```

   输出：

   ```
    locale.getpreferredencoding() -> 'cp936'
                    type(my_file) -> <class '_io.TextIOWrapper'>
                 my_file.encoding -> 'cp936'
              sys.stdout.isatty() -> False
              sys.stdout.encoding -> 'UTF-8'
               sys.stdin.isatty() -> False
               sys.stdin.encoding -> 'cp936'
              sys.stderr.isatty() -> False
              sys.stderr.encoding -> 'UTF-8'
         sys.getdefaultencoding() -> 'utf-8'
      sys.getfilesystemencoding() -> 'utf-8'
   ```

5. 如果打开文件时没有指定`encoding`参数，默认值由`locale.getpreferredencoding()`提供

6. 如果设定了`PYTHONIOENCODING`环境变量，`sys.stdout/stdin/stderr`的编码使用设定的值；否则，继承自所在的控制台；如果输入/输出重定向到文件，则由`locale.getpreferredencoding()`定义

7. Python在二进制数据和字符串之间转换时，内部使用`sys.getdefaultencoding()`获得的编码；Python3很少如此，但仍有发生。这个设置不能修改。

8. `sys.getfilesystemencoding()` 用于编解码文件名（不是文件内容）。把字符串参数作为文件名传给 `open()` 函数时就会使用它；如果传入的文件名参数是字节序列，那就不经改动直接传给 OS API。

### 4.4 规范化Unicode字符串

1. 因为 Unicode 有组合字符（变音符号和附加到前一个字符上的记号，打印时作为一个整体），所以字符串比较起来很复杂。

   ```python
   s1 = 'café'
   s2 = 'cafe\u0301'
   
   s1, s2
   len(s1), len(s2)
   s1 == s2
   
   # ('café', 'café')
   # (4, 5)
   # False
   ```

2. 在Unicode 标准中，'é' 和 'e\u0301' 这样的序列叫“标准等价物”（canonical equivalent），应用程序应该把它们视作相同的字符。但是，Python 看到的是不同的码位序列，因此判定二者不相等。

3. 这个问题的解决方案是使用 `unicodedata.normalize` 函数提供的Unicode 规范化。这个函数的第一个参数是这 4 个字符串中的一个：'NFC'、'NFD'、'NFKC' 和 'NFKD'。

   ```python
   from unicodedata import normalize
   
   len(normalize('NFC', s1)), len(normalize('NFC', s3))
   # (4, 4)
   len(normalize('NFD', s1)), len(normalize('NFD', s3))
   # (5, 5)
   normalize('NFC', s1) == normalize('NFC', s2)
   # True
   normalize('NFD', s1) == normalize('NFD', s3)
   # True
   ```

4. 西方键盘通常能输出组合字符，因此用户输入的文本默认是 NFC 形式。不过，安全起见，保存文本之前，最好使用 `normalize('NFC', user_text)` 清洗字符串。

5. NFC 也是 **W3C** 的“Character Model for the World Wide Web: String Matching and Searching”规范推荐的规范化形式。

6. 使用 NFC 时，有些单字符会被规范成另一个单字符。这两个字符在视觉上是一样的，但是比较时并不相等，因此要规范化，防止出现意外。

7. 在另外两个规范化形式（NFKC 和 NFKD）的首字母缩略词中，字母 K 表示 “compatibility”（兼容性）。这两种是较严格的规范化形式，对“兼容字符”有影响。虽然 Unicode 的目标是为各个字符提供 “规范的” 码位，但是为了兼容现有的标准，有些字符会出现多次。

   微符号是一个 **“兼容字符”**。

8. 使用 NFKC 和 NFKD 规范化形式时要小心，而且只能在特殊情况中使用，例如搜索和索引，而不能用于持久存储，因为这两种转换会导致数据损失。

9. **大小写折叠**：`str.casefold()`，就是把所有文本变成小写，再做些其他转换，与`str.lower()`基本一致，但是存在例外：*微符号 'μ' 会变成小写的希腊字母“μ”（在多数字体中二者看起来一样）；德语 Eszett（“sharp s”，ß）会变成“ss”*

10. 去掉变音符号的优势：

    1. 搜索方便：人们有时很懒，或者不知道怎么正确使用变音符号，而且拼写规则会随时间变化，因此实际语言中的重音经常变来变去。
    2. URL可读性：去掉变音符号还能让 URL 更易于阅读，至少对拉丁语系语言是如此。

11. 变音符号对排序有影响的情况很少发生，只有两个词之间唯有变音符号不同时才有影响。此时，带有变音符号的词排在常规词的后面。

12. 在 Python 中，非 ASCII 文本的标准排序方式是使用 `locale.strxfrm`
    函数，根据 locale 模块的文档，这个函数会“把字符串转换成适合所在区域进行比较的形式”。

13. PyUCA：Unicode 排序算法（Unicode Collation Algorithm，UCA）的纯 Python 实现。PyUCA 没有考虑区域设置。如果想定制排序方式，可以把自定义的排序表路径传给 Collator() 构造方法。PyUCA 默认使用项目自带的`allkeys.txt`。

    ```python
    import pyuca
    
    coll = pyuca.Collator()
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    sorted_fruits = sorted(fruits, key=coll.sort_key)
    sorted_fruits
    ```

14. Unicode 标准提供了一个完整的数据库（许多格式化的文本文件），不仅包括码位与字符名称之间的映射，还有各个字符的**元数据**，以及字符之间的关系。

    Unicode 数据库记录了字符是否可以打印、是不是字母、是不是数字，或者是不是其他数值符号。unicodedata 模块中有几个函数用于获取字符的元数据。例如，字符在标准中的官方名称是不是组合字符（如结合波形符构成的变音符号等），以及符号对应的人类可读数值（不是码位）。

15. ```python
    import unicodedata
    import re
    
    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    
    for char in sample:
        print(
            'U+%04x' % ord(char),
            char.center(6),
            're_dig' if re_digit.match(char) else '-',
            'isdig' if char.isdigit() else '-',
            'isnum' if char.isnumeric() else '-',
            format(unicodedata.numeric(char), '5.2f'),
            unicodedata.name(char),
            sep='\t'
        )
    ```

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210527164001663.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 4.5 支持字符串和字节序列的双模式API

1. 可以使用正则表达式搜索字符串和字节序列，但是在后一种情况中，ASCII 范围外的字节不会当成数字和组成单词的字母。

   1. 字符串模式 r'\d+' 能匹配泰米尔数字和 ASCII 数字。
   2. 字节序列模式 rb'\d+' 只能匹配 ASCII 字节中的数字。
   3. 字符串模式 r'\w+' 能匹配字母、上标、泰米尔数字和 ASCII 数字。
   4. 字节序列模式 rb'\w+' 只能匹配 ASCII 字节中的字母和数字。

2. 字符串正则表达式有个 re.ASCII 标志，它让\w、\W、\b、\B、\d、\D、\s 和 \S 只匹配 ASCII 字符。

3. 为了便于手动处理字符串或字节序列形式的文件名或路径名，os 模块提供了特殊的编码和解码函数。

   1. `fsencode(filename)`：如果 filename 是 str 类型（此外还可能是 bytes 类型），使用 `sys.getfilesystemencoding()` 返回的编解码器把 filename 编码成字节序列；否则，返回未经修改的 filename 字节序列。

   2. `fsdecode(filename)`：如果 filename 是 bytes 类型（此外还可能是 str 类型），使用 `sys.getfilesystemencoding()` 返回的编解码器把 filename 解码成字符串；否则，返回未经修改的 filename 字符串。

   3. `surrogateescape`：在 Unix 衍生平台中，这些函数使用 surrogateescape 错误处理方式以避免遇到意外字节序列时卡住。Windows 使用的错误处理方式是 strict。

      这种错误处理方式会把每个无法解码的字节替换成 Unicode 中 U+DC00 到 U+DCFF 之间的码位（Unicode 标准把这些码位称为“Low Surrogate Area”），这些码位是保留的，没有分配字符，供应用程序内部使用。编码时，这些码位会转换成被替换的字节值。

   4. 在 Python 3.3 之前，编译 CPython 时可以配置在内存中使用 16 位或 32 位存储各个码位。16 位是“窄构建”（narrow build），32 位是“宽构建”（wide build）。如果想知道用的是哪个，要查看 `sys.maxunicode` 的值：65535 表示“窄构建”，不能透明地处理U+FFFF 以上的码位。“宽构建”没有这个限制，但是消耗的内存更多：每个字符占 4 个字节，就算是中文象形文字的码位大多数也只占 2 个字节。这两种构建没有高下之分，应该根据自己的需求选择。

   5. 灵活的字符串表述类似于 Python 3 对 int 类型的处理方式：如果一个整数在一个机器字中放得下，那就存储在一个机器字中；否则解释器切换成变长表述，类似于 Python 2 中的 long 类型。

## 5. 一等函数

1. 在 Python 中，函数是一等对象。一等对象的定义：
   1. 在运行时创建
   2. 能赋值给变量或数据结构中的元素
   3. 能作为参数传给函数
   4. 能作为函数的返回结果
2. 人们经常将“把函数视作一等对象”简称为“一等函数”。这样说并不完美，似乎表明这是函数中的特殊群体。在 Python 中，**所有函数都是一等对象**。

### 5.1 把函数视作对象

1. `__doc__` 是函数对象众多属性中的一个，显示函数的备注

2. `help(f)`：输出的文本来自函数对象的`__doc__`属性

3. 函数对象的 **一等** 本性：

   1. 把 factorial 函数赋值给变量 fact，然后通过变量名调用
   2. 把它作为参数传给map 函数，返回一个可迭代对象，里面的元素是把第一个参数
      （一个函数）应用到第二个参数（一个可迭代对象）中各个元素上得到的结果

4. **高阶函数**：higher-order function，接受函数为参数，或者把函数作为结果返回的函数

   这样的函数例如：map，sorted，reduce，filter，apply（已移除）

   map、filter 和 reduce 这三个高阶函数还能见到，不过多数使用场景下都有更好的替代品。

   1. 列表推导 或 生成器表达式 具有map和filter两个函数的功能，且更易于阅读

      ```python
      list(map(fact, range(6)))
      [fact(n) for n in range(6)]
      ```

      ```python
      list(map(factorial, filter(lambda n: n % 2, range(6))))
      [fact(n) for n in range(7) if n % 2 != 0]
      ```

   2. reduce 是内置函数，最常用于求和，现在最好使用内置的 sum 函数，在可读性和性能方面，这是一项重大改善

      sum 和 reduce 的通用思想是把某个操作连续应用到序列的元素上，累计之前的结果，把一系列值归约成一个值。

      ```python
      from functools import reduce
      from operator import add
      
      reduce(add, range(100))
      sum(range(100))
      ```

   3. all 和 any 也是内置的归约函数

      - `all(iterable)`：如果 iterable 的每个元素都是真值，返回 True；`all([]) `返回True。
      - `any(iterable)`：只要 iterable 中有元素是真值，就返回 True；`any([]) `返回False。

5. **匿名函数**：lambda 关键字在 Python 表达式内创建匿名函数。

   lambda 句法只是语法糖：与 def 语句一样，lambda 表达式会创建函数对象。这是 Python 中几种可调用对象的一种。
   
6. 调用类的时候会运行类的`__new__`方法创建一个实例，然后运行`__init__`方法，初始化实例，最后把实例返回给调用方。

   - 因为Python没有new运算符，所以调用类相当于调用函数。
   - 如果类定义了`__call__`方法，那么它的实例可以作为函数调用。

7. 生成器函数：使用`yield`关键字的函数或方法。调用生成器函数返回的是生成器对象。（生成器函数还可以作为协程）

8. Python 中有各种各样可调用的类型，因此判断对象能否调用，最安全的方法是使用内置的 `callable()` 函数

   ```python
   [callable(obj) for obj in (abs, str, 13)]
   
   # [True, True, False]
   ```

9. 任何 Python 对象都可以表现得像函数。为此，只需实现实例方法 `__call__`

10. **函数内省**：除了`__doc__`，函数对象还有其他属性：`dir(factorial)`

    ```
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    ```

    1. 与用户定义的常规类一样，函数使用`__dict__`属性存储赋予它的用户属性。这相当于一种基本形式的注解。

    2. 列出 **常规对象没有** 而 **函数对象有** 的属性：

       ```python
       class C: pass
       obj = C()
       def func(): pass
       
       str(sorted(set(dir(func)) - set(dir(obj))))
       ```

       ```
       ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
       ```

    3. <a name='4'>用户定义函数的属性</a>：

       |       名称        |      类型      |                   说明                   |
       | :---------------: | :------------: | :--------------------------------------: |
       | `__annotations__` |      dict      |            参数和返回值的注解            |
       |    `__call__`     | method-wrapper |      实现()运算符；即可调用对象协议      |
       |   `__closure__`   |     tuple      | 函数闭包，即自由变量的绑定（通常是None） |
       |    `__code__`     |      code      |   编译成字节码的函数元数据和函数定义体   |
       |  `__defaults__`   |     tuple      |             形式参数的默认值             |
       |     `__get__`     | method-wrapper |            实现只读描述符协议            |
       |   `__globals__`   |      dict      |         函数所在模块中的全局变量         |
       | `__kwdefaults__`  |      dict      |        仅限关键字形式参数的默认值        |
       |    `__name__`     |      str       |                 函数名称                 |
       |  `__qualname__`   |      str       |    函数的限定名称，如`Random.choice`     |

### 5.2 函数的参数和注解

1. 仅限关键字参数：keyword-only argument，调用函数时使用`*`和`**`展开可迭代对象，映射到单个参数。

2. 在传参的时候，将字典加上`**`作为参数传递，实现的是字典中所有元素作为单个参数传入，同名的键回绑定到对应的**具名**参数上，余下的则被`**attrs`捕获。

3. [**仅限关键字参数**](https://blog.csdn.net/littleRpl/article/details/89457557)：它一定不会捕获未命名的定位参数。

   此种参数只能由关键字提供，**绝对不会被位置参数自动填充**。

   - 定义函数时若想指定仅限关键字参数，要把它们放到前面有 `*` 的参数后面。
   - 如果不想支持数量不定的定位参数，但是想支持仅限关键字参数，在签名中放
     一个 `*`
   - **允许常规参数出现在可变参数之后**：此时这个常规参数就是一个仅限关键字参数。强制性的，它只能通过关键字传参
   - 仅限关键字参数不需要有默认值， 由于Python需要将所有的参数都绑定一个值，而且将值绑定到关键字参数的唯一方法是通过这个关键字，因此这种参数是 **需要关键字的参数** 。所以这些参数必须通过调用方提供，且必须通过关键字提供值。
   - 语法上的更改是允许省略可变参数的参数名。这意味着对于一个有仅限关键字参数的函数来说，它不会再接受一个可变参数。

4. 获取关于参数的信息

   1. 使用HTTP微框架Bobo中有个使用函数内省的好例子。

      启动方式：`bobo -f hello.py`

      ```python
      import bobo
      
      @bobo.query('/')
      def hello(person):
          return "Hello %s" % person
      ```

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210608173931143.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   2. 函数对象有个 `__defaults__` 属性，它的值是一个元组，里面保存着定位参数和关键字参数的默认值。仅限关键字参数的默认值在 `__kwdefaults__` 属性中。然而，参数的名称在 `__code__` 属性中，它的值是一个 code 对象引用，自身也有很多属性。
   
5. <a name='5'>通过`inspect.signature`提取函数的签名</a>

   1. `inspect.signature` 函数返回一个 `inspect.Signature` 对象，它有一个 `parameters` 属性，这是一个有序映射，把参数名和 `inspect.Parameter` 对象对应起来。各个`Parameter `属性也有自己的属性，例如 `name`、`default `和 `kind`。特殊的 `inspect._empty` 值表示没有默认值，考虑到 `None `是有效的默认值（也经常这么做），而且这么做是合理的。
   2. `kind`的属性的值，为`_ParameterKind`类中的5个值之一：
      1. `POSITIONAL_OR_KEYWORD`：可以通过定位参数和关键字参数传入的形参（多数 Python 函数的参数属于此类）。
      2. `VAR_POSITIONAL`：定位参数元组。
      3. `VAR_KEYWORD`：关键字参数元组。
      4. `KEYWORD_ONLY`：仅限关键字参数（Python 3 新增）。
      5. `POSITIONAL_ONLY`：仅限定位参数；目前，Python 声明函数的句法不支持，但是有些使用 C 语言实现且不接受关键字参数的函数（如 divmod）支持。

6. 函数注解

   1. 函数声明中的各个参数可以在 : 之后增加注解表达式。如果参数有默认值，注解放在参数名和 = 号之间。
   2. 如果想注解返回值，在 ) 和函数声明末尾的 : 之间添加 -> 和一个表达式。那个表达式可以是任何类型。
   3. 注解中最常用的类型是类（如 str 或 int）和字符串（如 'int > 0'）
   4. 注解不会做任何处理，只是存储在函数的 `__annotations__` 属性中
   5. Python 对注解所做的唯一的事情是，把它们存储在函数的`__annotations__`属性里。仅此而已，Python 不做检查、不做强制、不做验证，什么操作都不做。换句话说，**注解对 Python 解释器没有任何意义。**
   6. 函数注解的最大影响或许不是让 Bobo 等框架自动设置，而是为 IDE 和
      lint 程序等工具中的静态类型检查功能提供额外的类型信息。

### 5.3 支持函数式编程的包

1. operator模块

   1. 使用reduce函数和一个匿名函数计算阶乘

      ```python
      def fact(n):
          return reduce(lambda a,b: a*b, range(1, n+1))
      ```

   2. operator 模块为多个算术运算符提供了对应的函数，从而避免编写 `lambda a, b: a*b` 这种平凡的匿名函数

      ```python
      def fact2(n):
          return reduce(mul, range(1, n+1))
      ```

   3. 使用 itemgetter 排序一个元组列表

      - itemgetter 使用 `[]` 运算符，因此它不仅支持序列，还支持映射和任何实现 `__getitem__` 方法的类。

      - `itemgetter(1)` 的作用与 `lambda fields:fields[1]` 一样

      ```python
      metro_data = [
      ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
      ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
      ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
      ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
      ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
      ]
      
      from operator import itemgetter
      for city in sorted(metro_data, key=itemgetter(2)):
          print(city)
      ```

   4. 如果把多个参数传给 itemgetter，它构建的函数会返回提取的值构成的元组：

      ```python
      cc_name = itemgetter(1, 0)
      
      for city in metro_data:
          print(cc_name(city))
      ```

   5. attrgetter 与 itemgetter 作用类似，它创建的函数根据名称提取对象的属性

      ```python
      from collections import namedtuple
      
      LatLong = namedtuple('LatLong', 'lat long')
      Metropolis = namedtuple('Metropolis', 'name cc pop coord')
      metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
      metro_areas
      metro_areas[0].coord.lat
      
      from operator import attrgetter
      name_lat = attrgetter('name', 'coord.lat')
      for city in sorted(metro_areas, key=attrgetter('coord.lat')):
          print(name_lat(city))
      ```

   6. attrgetter 与 itemgetter 个人总结：

      1. itemgetter：偏向于数组的切片操作
      2. attrgetter：偏向于类的属性获取操作

   7. methodcaller 的作用与 attrgetter 和 itemgetter 类似，它会自行创建函数，methodcaller 创建的函数会在对象上调用参数指定的方法：

      ```python
      from operator import methodcaller
      s = 'The tiem has come'
      
      upcase = methodcaller('upper')
      upcase(s)
      hiphenate = methodcaller('replace', ' ', '-')
      hiphenate(s)
      ```

   8. methodcaller还可以冻结某些参数，也就是部分应用（partial application），这与`functoosl.partial`函数的作用类似。

2. 使用`functools.partial`冻结参数

   - functools.partial 这个高阶函数用于部分应用一个函数。部分应用是指，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定。使用这个函数可以把接受一个或多个参数的函数改编成需要回调的API，这样参数更少。

     ```python
     from operator import mul
     from functools import partial
     triple = partial(mul, 3)
     triple(7)
     
     list(map(triple, range(1, 10)))
     ```

   - 固定nfc函数，标准化字符串编码处理

     ```python
     import unicodedata, functools
     nfc = functools.partial(unicodedata.normalize, 'NFC')
     
     s1 = 'café'
     s2 = 'cafe\u0301'
     
     s1, s2
     s1 == s2
     nfc(s1) == nfc(s2)
     ```

   - `functools.partialmethod` 函数的作用与 `partial`一样，不过是用于处理方法的。

     - 对于类方法，partial就没办法了，所以新引用了`partialmethod`
     - [参考链接](https://www.jianshu.com/p/e9d6bccecb9f)
     - [Python functools 模块](https://blog.windrunner.me/python/functools.html)

   - functools 模块中的 lru_cache 函数令人印象深刻，它会做备忘（memoization），这是一种自动优化措施，它会存储耗时的函数调用结果，避免重新计算。

## 6. 使用一等函数实现涉及模式
























------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
