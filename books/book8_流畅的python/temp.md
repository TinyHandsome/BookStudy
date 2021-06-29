## 6. 使用一等函数实现涉及模式

1. 实现“策略” 模式：

   - 经典“策略”模式
   - 使用函数实现“策略”模式

2. 策略对象通常是很好的享元：

   - 享元：flyweight，享元是可共享的对象，可以同时再多个上下文中使用
   - 可以避免运行时消耗
   - 函数比用户定义的类的实例轻量，而且无需使用“享元”模式，因为各个策略函数在 Python 编译模块时只会创建一次。普通的函数也是“可共享的对象，可以同时在多个上下文中使用”。

3. 在 Python 中，模块也是一等对象，而且标准库提供了几个处理模块的函数

   1. `globals()`：返回一个字典，表示当前的全局符号表。这个符号表始终针对当前模块（对函数或方法来说，是指定义它们的模块，而不是调用它们的模
      块）。

4. 命令模式

   - 可以通过把函数作为参数传递而简化。
   - “命令”模式的目的是解耦调用操作的对象（调用者）和提供实现的对象（接收者）。
   - 这个模式的做法是，在二者之间放一个 Command 对象，让它实现只有一个方法（execute）的接口，调用接收者中的方法执行所需的操作。这样，调用者无需了解接收者的接口，而且不同的接收者可以适应不同的 Command 子类。调用者有一个具体的命令，通过调用 execute 方法执行。

   ```python
   class MacroCommand:
       """一个执行一组命令的命令"""
       def __init__(self, commands):
           self.commands = list(commands)
           
       def __call__(self):
           for command in self.commands:
               command()
   ```

5. [深入浅出python闭包](https://zhuanlan.zhihu.com/p/22229197)

6. 复习

   1. 一等对象：指的是满足下述条件的程序实体
      1. 在运行时创建
      2. 能赋值给变量或数据结构中的元素
      3. 能作为参数传给函数
      4. 能作为函数的返回结果
   2. 整数、字符串和字典都是一等对象。在面向对象编程中，函数也是对象，并满足以上条件，所以函数也是一等对象，称为"一等函数"
   3. 普通函数 & 高阶函数：接受函数为参数的函数为高阶函数，其余为普通函数
   4. 《设计模式：可复用面向对象软件的基础》书中的两个设计原则：
      1. 对接口编程，而不是对实现编程
      2. 优先使用对象组合，而不是类继承

## 7. 函数装饰器和闭包

1. 函数装饰器用于在源码中“标记”函数，以某种方式增强函数的行为。这是一项强大的功能，但是若想掌握，必须理解闭包。
2. 除了在装饰器中有用处之外，闭包还是回调式异步编程和函数式编程风格的基础。

### 7.1 装饰器基础

1. 装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。

   下述两个代码等价：

   1. 装饰器

      ```python
      @decorate
      def target():
          print('running target()')
      ```

   2. 另一种写法

      ```python
      def target():
          print('running target()')
          
      target = decorate(target)
      ```

2. 两种写法的最终结果一样：上述两个代码片段执行完毕后得到的 target 不一定是原来那个 target 函数，而是 decorate(target) 返回的函数。

3. 装饰器通常把函数替换成另一个函数

   ```python
   def deco(func):
       def inner():
           print('running inner()')
       return inner
       
   @deco
   def target():
       print('running target()')
       
   target()
   # running inner()
   target
   # <function __main__.deco.<locals>.inner()>
   ```

4. 严格来说，装饰器只是语法糖。

5. 装饰器的特性：

   1. 一大特性是，能把被装饰的函数替换成其他函数。
   2. 第二个特性是，装饰器在加载模块时立即执行。

6. Python何时执行装饰器：**在被装饰的函数定义之后立即运行**

   ```python
   registry = []
   
   def register(func):
       print('running register(%s)' % func)
       registry.append(func)
       return func
   
   @register
   def f1():
       print('running f1()')
       
   @register
   def f2():
       print('running f2()')
       
   def f3():
       print('running f3()')
       
   def main():
       print('running main()')
       print('registry ->', registry)
       f1()
       f2()
       f3()
       
   if __name__ == '__main__':
       main()
   ```

   ```
   running register(<function f1 at 0x00000246ABFAC708>)
   running register(<function f2 at 0x00000246AC0D4CA8>)
   running main()
   registry -> [<function f1 at 0x00000246ABFAC708>, <function f2 at 0x00000246AC0D4CA8>]
   running f1()
   running f2()
   running f3()
   ```

7. 如果导入上述代码：`import registration`，函数的装饰器再导入模块时立即执行，而被装饰的函数只再明确调用时运行。

8. 装饰器在真实代码中的常用方式：

   1. 装饰器通常在一个模块中定义，然后应用到其他模块中的函数上
   2. 大多数装饰器会在内部定义函数，然后将其返回

9. register 装饰器原封不动地返回被装饰的函数，但是这种技术并非没有用处。

   1. 很多 Python Web 框架使用这样的装饰器把函数添加到某种中央注册处，例如把 URL 模式映射到生成 HTTP 响应的函数上的注册处。
   2. 这种注册装饰器可能会也可能不会修改被装饰的函数。

10. 使用装饰器改进“策略”模式

    - 多数装饰器会修改被装饰的函数
    - 通常，它们会定义一个内部函数，然后将其返回，替换被装饰的函数
    - 使用内部函数的代码几乎都要靠闭包才能正确运作

### 7.2 闭包

1. 变量作用域规则

   1. Python 不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量
   2. 如果在函数中赋值时想让解释器把 b 当成全局变量，要使用 `global` 声明
   3. 通过`from dis import dis`查看程序的字节码

2. 假如有个名为 avg 的函数，它的作用是计算不断增加的系列值的均值；例如，整个历史中某个商品的平均收盘价。每天都会增加新价格，因此平均值要考虑至目前为止所有的价格

   - avg使用方法：

     ```
     >>> avg(10)
     10.0
     >>> avg(11)
     10.5
     >>> avg(12)
     11.0
     ```

   - 实现方式：

     1. 计算移动平均的类

        ```python
        class Averager():
            def __init__(self):
                self.series = []
                
            def __call__(self, new_value):
                self.series.append(new_value)
                total = sum(self.series)
                return total/len(self.series)
        ```

     2. 计算移动平均值的高阶函数

        ```python
        def make_averager():
            series = []
            
            def averager(new_value):
                series.append(new_value)
                total = sum(series)
                return total/len(series)
            
            return averager
        ```

     3. **注意：**这两个示例有共通之处：调用 `Averager()` 或 `make_averager()` 得到一个可调用对象 avg，它会更新历史值，然后计算当前均值

        1. 在`averager`函数中，`series`时自由变量（free variable），这是一个技术术语，指：**未在本地作用域中绑定的变量**

           ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210615163943998.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

        2. averager 的闭包延伸到那个函数的作用域之外，包含自由变量 series 的绑定

        3. 审查返回的 averager 对象，我们发现 Python 在 `__code__` 属性（表示编译后的函数定义体）中保存局部变量和自由变量的名称

           ```python
           avg.__code__.co_varnames
           # ('new_value', 'total')
           
           avg.__code__.co_freevars
           # ('series',)
           ```

        4. series 的绑定在返回的 avg 函数的 `__closure__ `属性中。`avg.__closure__` 中的各个元素对应于`avg.__code__.co_freevars` 中的一个名称。这些元素是 cell 对象，有个 `cell_contents` 属性，保存着真正的值

           ```python
           avg.__closure__
           # (<cell at 0x00000246AC517108: list object at 0x00000246AC124A88>,)
           
           avg.__closure__[0].cell_contents
           # [10, 11, 12]
           ```

3. 闭包是一种函数，它会保留定义函数时存在的**自由变量的绑定**，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。

4. 注意，只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量。

5. nonlocal声明

   1. 上面的操作时引入了list（可变对象） series，用来保存每一次的值，然后这个series 是 所谓的 自由变量

   2. 但是对数字、字符串、元组等不可变类型来说，只能读取，不能更新，就不是所谓的 自由变量了，因此不会保存在闭包中。

   3. `nonlocal`声明可以把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。

   4. 如果为 `nonlocal `声明的变量赋予新值，闭包中保存的绑定会更新。

   5. 优化后的闭包

      ```python
      def make_averager():
          count = 0
          total = 0
          
          def averager(new_value):
              nonlocal count, total
              count += 1
              total += new_value
              return total/count
          
          return averager
      ```

   6. nonlocal是python3的特性，在python2中需要把内部函数需要修改的变量存储为可变对象（如字典或简单的实例）的元素或属性，并且把那个对象绑定给一个自由变量。

### 7.3 装饰器

1. 实现一个简单的装饰器：定义了一个装饰器，它会在每次调用被装饰的函数时计时，然后把经过的时间、传入的参数和调用的结果打印出来。

   ```python
   import time
   
   def clock(func):
       def clocked(*args):
           # 记录初始时间t0
           t0 = time.perf_counter()
           # 调用原来的 factorial 函数，保存结果
           result = func(*args)
           # 计算经过的时间
           elapsed = time.perf_counter() - t0
           
           # 格式化收集的数据，然后打印出来
           name = func.__name__
           arg_str = ', '.join(repr(arg) for arg in args)
           print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
           # 返回第 2 步保存的结果
           return result
       return clocked
   
   @clock
   def snooze(seconds):
       time.sleep(seconds)
       
   @clock
   def factorial(n):
       return 1 if n < 2 else n * factorial(n - 1)
   
   if __name__ == '__main__':
       print('*' * 40, 'Calling snooze(.123)')
       snooze(.123)
       print('*' * 40, 'Calling factorial(6)')
       print('6! = ', factorial(6))
   ```

   ```
   **************************************** Calling snooze(.123)
   [0.12354480s] snooze(0.123) -> None
   **************************************** Calling factorial(6)
   [0.00000040s] factorial(1) -> 1
   [0.00003500s] factorial(2) -> 2
   [0.00004590s] factorial(3) -> 6
   [0.00005500s] factorial(4) -> 24
   [0.00006390s] factorial(5) -> 120
   [0.00007470s] factorial(6) -> 720
   6! =  720
   ```

2. 这是装饰器的典型行为：把被装饰的函数替换成新函数，二者接受相同的参数，而且（通常）返回被装饰的函数本该返回的值，同时还会做些额外操作。

   > 装饰器：动态地给一个对象添加一些额外的职责
   >
   > ——《设计模式：可复用面向对象软件的基础》

3. 上述实现的clock装饰器有几个缺点：

   1. 不支持关键字参数
   2. 遮盖了被装饰函数的`__name__`和`__doc__`属性

4. 使用`functools.wraps`装饰器把相关属性从func复制到clocked中，同时还可以正确处理关键字参数

   ```python
   import time
   from functools import wraps
   
   def clock(func):
       @wraps(func)
       def clocked(*args, **kwargs):
           t0 = time.perf_counter()
           result = func(*args, **kwargs)
           elapsed = time.perf_counter() - t0
           name = func.__name__
           
           arg_lst = []
           if args:
               arg_lst.append(', '.join(repr(arg) for arg in args))
           if kwargs:
               pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
               arg_lst.append(', '.join(pairs))
           arg_str = ', '.join(arg_lst)
           print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
           return result
       return clocked
   ```

5. 标准库中的装饰器

   1. python 内置了三个用于装饰方法的函数：property、classmethod、staticmethod
   2. functools：wraps、lru_cache、singledispatch

6. 使用`functools.lru_cache`做备忘，memoization，这是一项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。

   - LRU：Least Recently Used，表明缓存不会无限制增长，一段时间不用的缓存条目会被扔掉。
   - 注意，必须像常规函数哪一行调用`lru_cache`：`@functools.lru_cache()`，这是因为`lru_cache`可以接受配置参数。
   - 除了优化递归算法之外，`lru_cache`在从Web中获取信息的应用中也能发挥巨大作用。

7. `functools.lru_cache(maxsize=128, typed=False)`

   - maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，腾出空间。为了得到最佳性能，maxsize 应该设为 2 的幂。
   - typed 参数如果设为 True，把不同参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开。
   - lru_cache 使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所以被 lru_cache 装饰的函数，它的所有参数都必须是可散列的。

8. 单分派泛函数

   1. 因为 Python **不支持重载方法或函数**，所以我们不能使用不同的签名定义htmlize 的变体，也无法使用不同的方式处理不同的数据类型。

   2. 在Python 中，一种常见的做法是把 htmlize 变成一个分派函数，使用一串 if/elif/elif，调用专门的函数，如htmlize_str、htmlize_int，等等。这样不便于模块的用户扩展，还显得笨拙：时间一长，分派函数 htmlize 会变得很大，而且它与各个专门函数之间的耦合也很紧密。

   3. `functools.singledispatch`装饰器可以把整体方案拆分成多个模块，甚至可以为你无法修改的类提供专门的函数。

   4. 使用 `@singledispatch` 装饰的普通函数会变成泛函数（generic function）：根据第一个参数的类型，以不同方式执行相同操作的一组函数。

      > 这才称得上是单分派。如果根据多个参数选择专门的函数，那就是多分派了。

   5. singledispatch 创建一个自定义的htmlize.register 装饰器，把多个函数绑在一起组成一个泛函数

      ```python
      from functools import singledispatch
      from collections import abc
      import numbers
      import html
      
      @singledispatch
      def htmlize(obj):
          content = html.escape(repr(obj))
          return '<pre>{}</pre>'.format(content)
      
      @htmlize.register(str)
      def _(text):
          content = html.escape(text).replace('\n', '<br>\n')
          return '<p>{0}</p>'.format(content)
      
      @htmlize.register(numbers.Integral)
      def _(n):
          return '<pre>{0} (0x{0:x})</pre>'
      
      @htmlize.register(tuple)
      @htmlize.register(abc.MutableSequence)
      def _(seq):
          inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
          return '<ul>\n<li>' + inner + '</li>\n</ul>'
      ```

   6. `numbers.Integral` 是 `int` 的虚拟超类

   7. 可以叠放多个 `register `装饰器，让同一个函数支持不同类型

   8. 只要可能，注册的专门函数应该处理抽象基类（如 numbers.Integral和 abc.MutableSequence），不要处理具体实现（如 int 和 list）。这样，代码支持的兼容类型更广泛。

   9. 使用抽象基类检查类型，可以让代码支持这些抽象基类现有和未来的具体子类或虚拟子类

   10. `@singledispatch` 不是为了把 Java 的那种方法重载带入Python

   11. 在一个类中为同一个方法定义多个重载变体，比在一个函数中使用一长串 if/elif/elif/elif 块要更好。

   12. 但是这两种方案都有缺陷，因为它们让代码单元（类或函数）承担的职责太多。

   13. `@singledispath` 的优点是支持模块化扩展：各个模块可以为它支持的各个类型注册一个专门函数。

   14. 装饰器是函数，因此可以组合起来使用（即，**可以在已经被装饰的函数上应用装饰器**）

9. 叠放装饰器

   下述代码等价

   ```python
   @d1
   @d2
   def f():
   	print('f')
   	
   f = d1(d2(f))
   ```

10. 参数化装饰器

    ```python
    registry = set()
    def register(active=True):
        def decorate(func):
            print('running register(active=%s )->decorate(%s)' % (active, func))
            if active:
                registry.add(func)
            else:
                registry.discard(func)
            
            return func
        return decorate
    
    @register(active=False)
    def f1():
        print('running f1()')
        
    @register()
    def f2():
        print('running f2()')
        
    def f3():
        print('running f3()')
    ```

    1. 这里decorate时装饰器，必须返回一个函数
    2. register是装饰器工厂函数，因此返回的是一个装饰器decorate
    3. 即使不传入参数，register也必须作为函数调用：`@register()`
    4. 如果不使用 @ 句法，那就要像常规函数那样使用 register；若想把 f 添加到 registry 中，则装饰 f 函数的句法是` register()(f)`；不想添加（或把它删除）的话，句法是 `register(active=False)(f)`

11. 参数化clock装饰器

    ```python
    import time
    
    DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
    
    def clock(fmt=DEFAULT_FMT):
        def decorate(func):
            def clocked(*_args):
                t0 = time.time()
                _result = func(*_args)
                elapsed = time.time() - t0
                name = func.__name__
                args = ", ".join(repr(arg) for arg in _args)
                result = repr(_result)
                print(fmt.format(**locals()))
                return _result
            return clocked
        return decorate
    
    if __name__ == '__main__':
        @clock()
        def snooze(seconds):
            time.sleep(seconds)
        
        for i in range(3):
            snooze(.123)
    ```

    ```
    [0.12328148s] snooze(0.123) -> None
    [0.12369442s] snooze(0.123) -> None
    [0.12362432s] snooze(0.123) -> None
    ```

    1. clock：参数化装饰器工厂函数
    2. decorate：真正的装饰器
    3. clocked：包装被装饰的函数
    4. `_result`：被装饰函数返回的真正结果
    5. `_args`：clocked的参数，args用于显示的字符串
    6. result：`_result`的字符串表现形式，用于显示

12. 装饰器的参数

    ```python
    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze(.123)
    ```

    ```
    snooze: 0.12300252914428711s
    snooze: 0.12314867973327637s
    snooze: 0.1238546371459961s
    ```

    ```python
    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze(.123)
    ```

    ```
    snooze(0.123) dt=0.124s
    snooze(0.123) dt=0.123s
    snooze(0.123) dt=0.123s
    ```

## 8. 对象引用、可变性和垃圾回收

### 8.1 变量不是盒子

1. 如果把变量想象为盒子，那么无法解释 Python 中的赋值；应该把变量视作便利贴

2. 对引用式变量来说，说把变量分配给对象更合理

3. `==` 运算符比较两个对象的值（对象中保存的数据），而 `is` 比较对象的标识

4. 元组的相对不可变性：元组的不可变性其实是指 `tuple` 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。

   **元组里面有一个list，这个list就可以append，但是id还是不变。**

   **这也是有些元组不可散列的原因。**

5. str、bytes 和 array.array 等单一类型序列是扁平的，它们保存的不是引用，而是在连续的内存中保存数据本身（字符、字节和数字）。

6. 浅复制（copy.copy）和深复制（copy.deepcopy）的区别：深复制中副本不共享内部对象的引用

### 8.2 函数的参数作为引用

1. 不要使用可变类型作为参数的默认值

   - 不可以默认值为类似于`[]`，因为如果不传参的话，这个`[]`就是类的内部变量，多个实例会共用这个变量

   - 这也是为什么通常使用 None 作为接收可变值的参数的默认值的原因。

2. 防御可变参数

   - 类中的操作可能会修改传入类的可变参数
   - 修正的方法：初始化时，把参数值的副本赋值给成员变量

### 8.3 del、垃圾回收和弱引用

> 注意，这一章节的一些代码要在cmd中才能实现，jupyterlab中的实验结果与书中给的结果不一致。

1. del 语句删除名称，而不是对象

2. del 命令可能会导致对象被当作垃圾回收，但是仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时。

3. 重新绑定也可能会导致对象的引用数量归零，导致对象被销毁。

4. 弱引用：正是因为有引用，对象才会在内存中存在。当对象的引用数量归零后，垃圾回收程序会把对象销毁。但是，有时需要引用对象，而不让对象存在的时间超过所需时间。这经常用在缓存中。
   1. 弱引用不会增加对象的引用数量。引用的目标对象称为所指对象（referent）。因此我们说，弱引用不会妨碍所指对象被当作垃圾回收。
   2. 弱引用在缓存应用中很有用，因为我们不想仅因为被缓存引用着而始终保存缓存对象。
   
5. weakref.ref 类其实是低层接口，供高级用途使用，多数程序最好使用 weakref 集合和 finalize。也就是说，应该使用 `WeakKeyDictionary`、`WeakValueDictionary`、`WeakSet` 和 `finalize`（在内部使用弱引用），不要自己动手创建并处理 weakref.ref 实例。

6. WeakValueDictionary
   - WeakValueDictionary 类实现的是一种可变映射，里面的值是对象的弱引用。
   - 被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从 WeakValueDictionary 中删除。
   - 因此，WeakValueDictionary 经常用于缓存。
   
7. 与 WeakValueDictionary 对应的是 WeakKeyDictionary，后者的键是弱引用

8. WeakSet 类：保存元素弱引用的集合类。元素没有强引用时，集合会把它删除
   - 如果一个类需要知道所有实例，一种好的方案是创建一个WeakSet 类型的类属性，保存实例的引用。
   - 如果使用常规的 set，实例永远不会被垃圾回收，因为类中有实例的强引用，而类存在的时间与 Python 进程一样长，除非显式删除类。
   
9. 弱引用的局限
   - 不是每个 Python 对象都可以作为弱引用的目标（或称所指对象）。基本的 list 和 dict 实例不能作为所指对象，但是它们的子类可以
   - set 实例可以作为所指对象
   - 用户定义的类型也没问题
   - 但是，**int 和 tuple 实例不能作为弱引用的目标**，甚至它们的子类也不行
   - 这些局限基本上是 CPython 的实现细节，在其他 Python 解释器中情况可能不一样。这些局限是内部优化导致的结果
   
10. Python对不可变类型施加的把戏

    1. **对元组 t 来说，`t[:]` 不创建副本，而是返回同一个对象的引用**。此外，`tuple(t)` 获得的也是同一个元组的引用。（str、bytes 和 frozenset 实例也有这种行为）

       - frozenset 实例不是序列，因此不能使用 `fs[:]`（fs 是一个 frozenset 实例），但是，`fs.copy()` 具有相同的效果：返回同一个对象的引用，而不是创建一个副本

    2. **字符串字面量可能会创建共享的对象**

       ```python
       s1 = 'ABC'
       s2 = 'ABC'
       s2 is s1
       
       # True
       ```

       - **共享字符串字面量**是一种优化措施，称为**驻留（interning）**。CPython 还会在小的整数上使用这个优化措施，防止重复创建“热门”数字
       - CPython 不会驻留所有字符串和整数











 

学到 p379 学到杂谈

