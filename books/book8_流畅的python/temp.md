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

11. 杂谈

    1. java的`==`运算符比较的是对象（不是基本类型）的引用，而不是对象的值。否则的话要用到`.equals`方法，如果调用方法的变量为`null`，会得到一个 **空指针异常** 
    2. 在python中，`==`比较对象的值，`is`比较引用
    3. 最重要的是，python支持重载运算发，`==`能正确处理标准库中的所有对象，包括`None`，与java的null不同

## 9.  符合Python风格的对象

### 9.1 对象的表示形式

1. 获取对象的字符串表示形式的标准方式
   1. `repr()`：开发者理解的方式返回对象的字符串表示形式
   2. `str()`：用户理解的方式返回对象的字符串表示形式
   
2. 在 Python 3 中，`__repr__`、`__str__ `和 `__format__ `都必须返回 Unicode 字符串（str 类型）。只有 `__bytes__ `方法应该返回字节序列（bytes 类型）

3. 定义`__iter__`方法，把类的实例编程可迭代的对象，这样才能拆包。

   `x, y = my_vector`

   > 这一行也可以写成`yield self.x; yield self.y`

4. `eval()` 函数用来执行一个字符串表达式，并返回表达式的值。

5. classmethod：第一个参数是类本身，最常见的用途是定义备选构造方法

6. staticmethod：第一个参数不是特殊的值，其实静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义

7. 作者对staticmethod的态度是：”不是特别有用“，因为如果想定义不需要与类进行交互的函数，只需要在模块中定义就好了。

### 9.2 格式化显示

1. 内置的 `format()` 函数和 `str.format()` 方法把各个类型的格式化方式委托给相应的 `.__format__(format_spec)` 方法

   - `format(my_obj, format_spec)`里的第二个参数

   - `str.format()`方法的格式字符串，`{}`里代换字段中冒号后面的部分

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210706104922610.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. `{0.mass:5.3e}`这样的格式字符串其实包含两部分

   - 冒号左边的`.mass`在代换字段句法中是字段名
   - 冒号后面的`5.3e`是格式说明符
   - 格式说明符使用的表示法叫 **格式规范微语言** ，Format Specification Mini-Language

3. 格式规范微语言为一些内置类型提供了专用的表示代码

   1. b 和 x 分别表示二进制和十六进制的 int 类型
   2. f 表示小数形式的 float 类型
   3. % 表示百分数形式

4. 格式规范微语言是可扩展的，因为各个类可以自行决定如何解释format_spec 参数

5. 如果类没有定义 `__format__ ` 方法，从 object 继承的方法会返回`str(my_object)`

6. 在格式规范微语言中，整数使用的代码有`bcdoxXn`，浮点数使用的代码有`eEfFgGn%`，字符串使用的代码有`s`

7. 使用两个前导下划线（尾部没有下划线，或者有一个下划线），把属性标记为私有的

8. ` @property`装饰器把读值方法标记为属性

9. 要想创建可散列的类型，不一定要实现特性，也不一定要保护实例属性。只需正确地实现 `__hash__` 和 `__eq__` 方法即可

10. 如果定义的类型有标量数值，可能还要实现 `__int__ `和 `__float__ `方法（分别被 `int()` 和 `float()` 构造函数调用），以便在某些情况下用于强制转换类型。此外，还有用于支持内置的 `complex()` 构造函数的 `__complex__ `方法

    ```python
    from array import array
    import math
    
    class Vector2d:
        typecode = 'd'
        
        def __init__(self, x, y):
            self.__x = float(x)
            self.__y = float(y)
        
        @property
        def x(self):
            return self.__x
        
        @property
        def y(self):
            return self.__y
            
        def __iter__(self):
            return (i for i in (self.x, self.y))
            
        def __repr__(self):
            class_name = type(self).__name__
            return '{}({!r}, {!r})'.format(class_name, *self)
        
        def __str__(self):
            return str(tuple(self))
        
        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
        
        def __eq__(self, other):
            return tuple(self) == tuple(other)
        
        def __abs__(self):
            return math.hypot(self.x, self.y)
        
        def __bool__(self):
            return bool(abs(self))
        
        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(*memv)
        
        def angle(self):
            return math.atan2(self.y, self.x)
        
        def __hash__(self):
            return hash(self.x) ^ hash(self.y)
        
        def __format__(self, fmt_spec=''):
            if fmt_spec.endswith('p'):
                fmt_spec = fmt_spec[: -1]
                coords = (abs(self), self.angle())
                outer_fmt = '<{}, {}>'
            else:
                coords = self
                outer_fmt = '({}, {})'
                components = (format(c, fmt_spec) for c in coords)
                return outer_fmt.format(*components)
    ```

### 9.3 Python的私有属性和受保护的属性

1. 私有属性需要在前面加两根下划线，Python 会把属性名存入实例的
   `__dict__` 属性中，而且会在前面加上一个下划线和类名

   - 父类：_Dog__mood
   - 子类：_Beagle__mood
   - 这个语言特性叫 **名称改写** （name mangling）

2. Python的私有属性是可以被修改的，通过上述名称修改

3. 受保护属性：

   - Python 解释器不会对使用单个下划线的属性名做特殊处理，不过这是很多 Python 程序员严格遵守的约定，他们不会在类外部访问这种属性。
   - 不过在模块中，顶层名称使用一个前导下划线的话，的确会有影响：对 `from mymod import *` 来说，mymod 中前缀为下划线的名称不会被导入。然而，依旧可以使用 `from mymod import _privatefunc` 将其导入。

4. 使用`__slots__`类属性节省空间

   - 为了使用底层的散列表提升访问速度，字典会消耗大量内存。如果要处理数百万个属性不多的实例，通过 `__slots__ ` 类属性，能节省大量内存，方法是让解释器在元组中存储实例属性，而不用字典。

   - 定义 `__slots__ ` 的方式是，创建一个类属性，使用 `__slots__ ` 这个名字，并把它的值设为一个字符串构成的可迭代对象，其中各个元素表示各个实例属性。

     ```python
     __slots__ = ('__x', '__y')
     ```

   - 在类中定义 `__slots__` 属性的目的是告诉解释器：“这个类中的所有实例属性都在这儿了！”这样，Python 会在各个实例中使用类似元组的结构存储实例变量，从而避免使用消耗内存的 `__dict__` 属性。如果有数百万个实例同时活动，这样做能节省大量内存。

   - 如果类中定义了 `__slots__` 属性，而且想把实例作为弱引用的目标，那么要把 `'__weakref__'` 添加到 `__slots__` 中。

5. 如果使用得当，`__slots__` 能显著节省内存

   - 每个子类都要定义 `__slots__` 属性，因为解释器会忽略继承的 `__slots__` 属性
   - 实例只能拥有 `__slots__` 中列出的属性，除非把 `'__dict__'` 加入 `__slots__` 中（这样做就失去了节省内存的功效）
   - 如果不把 `'__weakref__'` 加入 `__slots__`，实例就不能作为弱引用的目标

6. 覆盖类属性

   - 类属性可用于为实例属性提供默认值
   - 如果为不存在的实例属性赋值，会新建实例属性
   - 假如我们为 `typecode` **实例属性**赋值，那么同名 **类属性** 不受影响
   - 然而，自此之后，实例读取的 `self.typecode` 是实例属性 `typecode`，也就是把同名类属性遮盖了
   - Python风格的修改方法：
     - 类属性是公开的，因此会被子类继承
     - 于是经常会创建一个子类，只用于定制类的数据属性

7. 总结：

   1. 所有用于获取字符串和字节序列表示形式的方法：`__repr__`、`__str__`、`__format__ `和 `__bytes__`。
   2. 把对象转换成数字的几个方法：`__abs__`、`__bool__`和 `__hash__`。
   3. 用于测试字节序列转换和支持散列（连同 `__hash__ `方法）的 `__eq__ `运算符。

## 10. 序列的修改、散列和切片

1. `reprlib.repr`：展示变量的程序员能明白的语句

2. 协议和鸭子类型
   1. 在 Python 中创建功能完善的序列类型无需使用继承，只需实现符合序列协议的方法
   2. 在面向对象编程中，协议是非正式的接口，只在文档中定义，在代码中不定义
   3. 例如，Python 的序列协议只需要 `__len__` 和 `__getitem__` 两个方法
   4. 协议是非正式的，没有强制力，因此如果你知道类的具体使用场景，通常只需要实现一个协议的部分。
   
3. `slice.indices`：indices 方法开放了内置序列实现的棘手逻辑，用于优雅地处理缺失索引和负数索引，以及长度超过目标序列的切片。这个方法会“整顿”元组，把 start、stop 和 stride 都变成非负数，而且都落在指定长度序列的边界内。

4. `__getattr__()`：对 `my_obj.x` 表达式，Python 会检查 `my_obj` 实例有没有名为 `x` 的属性；如果没有，到类（`my_obj.__class__`）中查找；如果还没有，顺着继承树继续查找。如果依旧找不到，调用 `my_obj` 所属类中定义的 `__getattr__` 方法，传入 `self` 和属性名称的字符串形式（如 'x'）

5. 不建议只为了避免创建实例属性而使用 `__slots__` 属性。`__slots__` 属性只应该用于节省内存，而且仅当内存严重不足时才应该这么做。

6. 归约函数（reduce、sum、any、all）把序列或有限的可迭代对象变成一个聚合结果

7. `functools.reduce()` 的关键思想是，把一系列值归约成单个值。`reduce() `函数的第一个参数是接受两个参数的函数，第二个参数是一个可迭代的对象。

   ```python
   import functools
   functools.reduce(lambda a, b: a * b, range(1, 6))
   # 120
   ```

8. `reduce(function, iterable, initializer)`：使用的时候最好提供第三个参数，这样能避免异常。如果序列为空，`initializer` 是返回的结果；否则，在归约中使用它作为第一个参数，因此应该使用恒等值。比如，对 +、| 和 ^ 来说， `initializer` 应该是 0；而对 * 和 & 来说，应该是 1。

9. `zip`：使用 zip 函数能轻松地并行迭代两个或更多可迭代对象，它返回的元组可以拆包成变量，分别对应各个并行输入中的一个元素。

   - zip 有个奇怪的特性：当一个可迭代对象耗尽后，它不发出警告就停止
   - `itertools.zip_longest` 函数的行为有所不同：使用可选的 `fillvalue`（默认值为 None）填充缺失的值，因此可以继续产出，直到最长的可迭代对象耗尽

   ```python
   from array import array
   import reprlib
   import math
   import numbers
   import functools
   import operator
   import itertools
   
   class Vector:
       typecode = 'd'
       
       def __init__(self, components):
           self._components = array(self.typecode, components)
           
       def __iter__(self):
           return iter(self._components)
       
       def __repr__(self):
           components = reprlib.repr(self._components)
           components = components[components.find('['):-1]
           return 'Vector({})'.format(components)
       
       def __str__(self):
           return str(tuple(self))
       
       def __bytes__(self):
           return (bytes([ord(self.typecode)]) + bytes(self._components))
       
       def __eq__(self, other):
           return tuple(self) == tuple(other)
       
       def __abs__(self):
           return math.sqrt(sum(x * x for x in self))
       
       def __bool__(self):
           return bool(abs(self))
       
       def __len__(self):
           return len(self._components)
       
   #     def __getitem__(self, index):
   #         return self._components[index]
   
       def __getitem__(self, index):
           cls = type(self)
           # 如果传入的参数是切片，就返回改切片生成的Vector类
           if isinstance(index, slice):
               return cls(self._components[index])
           # 如果传入的参数是数，就返回列表中的元素
           elif isinstance(index, numbers.Integral):
               return self._components[index]
           # 否则就报错啦
           else:
               msg = '{cls.__name__} indices must be integers'
               raise TypeError(msg.format(cls=cls))
       
       shortcut_names = 'xyzt'
       def __getattr__(self, name):
           cls = type(self)
           
           if len(name) == 1:
               pos = cls.shortcut_names.find(name)
               if 0 <= pos < len(self._components):
                   return self._components[pos]
           
           msg = '{.__name__!r} object has no attribute {!r}'
           raise AttributeError(msg.format(cls, name))
           
       def __setattr__(self, name, value):
           cls = type(self)
           if len(name) == 1:
               if name in cls.shortcut_names:
                   error = 'readonly attribute {attr_name!r}'
               elif name.islower():
                   error = "can't set attributes 'a' to 'z' in {cls_name!r}"
               else:
                   error = ''
               
               if error:
                   msg = error.format(cls_name=cls.__name__, attr_name=name)
                   raise AttributeError(msg)
           super().__setattr__(name, value)
           
       def __eq__(self, other):
   #         return tuple(self) == tuple(other)
           # 为了提高比较的效率，使用zip函数
   #         if len(self) != len(other):
   #             return False      
   #         for a, b in zip(self, other):
   #             if a != b:
   #                 return False
   #         return True
           
           # 过用于计算聚合值的整个 for 循环可以替换成一行 all 函数调用：
           # 如果所有分量对的比较结果都是 True，那么结果就是 True。
           return len(self) == len(other) and all(a == b for a, b in zip(self, other))
       
       def __hash__(self):
           # 创建一个生成器表达式，惰性计算各个分量的散列值
           # hashes = (hash(x) for x in self._components)
           # 这里换成map方法
           hashes = map(hash, self._components)
           
           # 把hashes提供给reduce函数，第三个参数0是初始值
           return functools.reduce(operator.xor, hashes, 0)
       
       def angle(self, n):
           r = math.sqrt(sum(x * x for x in self[n:]))
           a = math.atan2(r, self[n-1])
           if (n == len(self) - 1) and (self[-1] < 0):
               return math.pi * 2 - a
           else:
               return a
           
       def angles(self):
           return (self.angle(n) for n in range(1, len(self)))
       
       def __format__(self, fmt_spec=''):
           if fmt_spec.endswith('h'):
               # 超球面坐标
               fmt_spec = fmt_spec[:-1]
               coords = itertools.chain([abs(self)], self.angles())
               outer_fmt = '<{}>'
           else:
               coords = self
               outer_fmt = '({})'
           components = (format(c, fmt_spec) for c in coords)
           return outer_fmt.format(', '.join(components))
               
       @classmethod
       def frombytes(cls, octets):
           typecode = chr(octets[0])
           memv = memoryview(octets[1:]).cast(typecode)
           return cls(memv)
   ```

## 11. 接口：从协议到抽象基类











 

学到 p438

