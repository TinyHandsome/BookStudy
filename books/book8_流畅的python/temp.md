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

> 鸭子类型：“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
>
> 程序设计中，**鸭子类型**（英语：**duck typing**）是 **动态类型** 的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法" (计算机科学)和属性的集合决定。
>
> 在鸭子类型中，关注点在于对象的行为，能做什么；而不是关注对象所属的类型。

1. Python文化中的接口和协议

   1. 受保护的属性和私有属性不在接口中
   2. **接口** 的补充定义：对象公开方法的子集，让对象在系统中扮演特定的角色
   3. 协议与继承没有关系。一个类可能会实现多个接口，从而让实例扮演多个角色。
   4. 协议是接口，但不是正式的，因此协议不能像正式接口那样施加限制
   5. 一个类可能只实现部分接口，这是允许的
   6. 对 Python 程序员来说，“X 类对象”、“X 协议”和“X 接口”都是一个意思
   7. 序列协议是 Python 最基础的协议之一。即便对象只实现了那个协议最基本的一部分，解释器也会负责任地处理。

2. Python喜欢序列

   1. 定义为抽象基类的Sequence正式接口

      ```mermaid
      classDiagram
      	Container <|-- Sequence
      	Iterable <|-- Sequence
      	Sized <|-- Sequence
      	
      	class Container {
      		__contains__
      	}
      	class Iterable {
      		__iter__
      	}
      	class Sized {
      		__len__
      	}
      	
      	class Sequence {
      		__getitem__
      		__contains__
      		__iter__
      		__reversed__
      		index
      		count
      	}
      ```

   2. 定义 `__getitem__` 方法，只实现序列协议的一部分，这样足够访问元素、迭代和使用 in 运算符了

      ```python
      class Foo:
          def __getitem__(self, pos):
              return range(0, 30, 10)[pos]
      ```

      - 虽然没有 `__iter__` 方法，但是 Foo 实例是可迭代的对象，因为发现有 `__getitem__` 方法时，Python 会调用它，传入从 0 开始的整数索引，尝试迭代对象
      - 鉴于序列协议的重要性，如果没有 `__iter__` 和 `__contains__`方法，Python 会调用 `__getitem__` 方法，设法让迭代和 in 运算符可用。

   3. shuffle 函数要调换集合中元素的位置，只实现了`__getitem__`即是只实现了不可变的序列协议，可变的序列还必须提供`__setitem__`方法。

   4. **猴子补丁**：在运行时修改类或模块，而不改动源码

   5. **协议是动态的**：`random.shuffle` 函数不关心参数的类型，只要那个对象实现了部分可变序列协议即可。即便对象一开始没有所需的方法也没关系，后来再提供也行。

   6. **“鸭子类型”**：对象的类型无关紧要，只要实现了特定的协议即可。

3. Alex Martelli的水禽

   1. 用isinstance检查对象的类型，而不是`type(foo) is bar`。

   2. 白鹅类型，goose typing，指只要`cls`是抽象基类，即`cls`的元类是`abc.ABCMeta`，就可以使用`isinstance(obj, cls)`

   3. Python 的抽象基类还有一个重要的实用优势：可以使用 `register` 类方法在终端用户的代码中把某个类“声明”为一个抽象基类的“虚拟”子类

   4. 无需注册，`abc.Sized`也能把Struggle识别为自己的子类，只要实现了特殊方法`__len__`即可。要使用正确的句法和语义实现，前者要求没有参数，后者要求返回一个非负整数，指明对象的长度。**如果不使用规范的语法和语义实现特殊方法，如`__len__`，会导致非常严重的问题**

      ```python
      class Struggle:
          def __len__(self):
              return 23
      
      from collections import abc
      isinstance(Struggle(), abc.Sized)
      ```

   5. 在 Python 3.4 中没有能把字符串和元组或其他不可变序列区分开的抽象基类，因此必须测试 str：`isinstance(x, str)`。

   6. EAFP和LBYL

      1. EAFP：**E**asier to **A**sk for **F**orgiveness than **P**ermission，请求宽恕比许可更容易

         - 操作前不检查，出了问题由异常处理来处理

         - 代码表现：try...except...

         ```python
         try:
             x = test_dict["key"]
         except KeyError:
             # key 不存在
         ```

      2. LBYL：**L**ook **B**efore **Y**ou **L**eap，三思而后行

         - 操作前先检查，再执行
         - 代码表现：if...else...

         ```python
         if "key" in test_dict:
             x = test_dict["key"]
         else:
             # key 不存在
         ```

      3. EAFP 的异常处理往往也会影响一点性能，因为在发生异常的时候，程序会进行保留现场、回溯traceback等操作，但在异常发生频率比较低的情况下，性能相差的并不是很大。

      4. 而 LBYL 则会消耗更高的固定成本，因为无论成败与否，总是执行额外的检查。

      5. 相比之下，如果不引发异常，EAFP 更优一些，

      6. Python 的动态类型（duck typing）决定了 EAFP，而 Java等强类型（strong typing）决定了 LBYL

   7. 定义抽象基类的子类

      1. 导入时，Python不会检查抽象方法的实现，在运行时实例化类的时候才会真正检查。因此，如果没有正确实现某个抽象方法，Python会抛出TypeError异常。

      2. MutableSequence 抽象基类和 collections.abc 中它的超类的UML类图（箭头由子类指向祖先；以斜体显示的名称是抽象类和抽象方法）

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210715195644418.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
      
   8. 标准库中的抽象基类

      1. `collections.abc` 模块中各个抽象基类的 UML 类图

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717112728709.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      2. Iterable、Container 和 Sized

         - 各个集合应该继承这三个抽象基类，或者至少实现兼容的协议。
         - Iterable 通过 `__iter__ `方法支持迭代
         - Container 通过 `__contains__ `方法支持 in 运算符
         - Sized 通过 `__len__ `方法支持 `len()` 函数

      3. Sequence、Mapping 和 Set

         - 这三个是主要的不可变集合类型，而且各自都有可变的子类

      4. MappingView

         - 映射方法 .items()、.keys() 和 .values() 返回的对象分别是 ItemsView、KeysView 和 ValuesView 的实例

      5. Callable 和 Hashable

         - 这两个抽象基类与集合没有太大的关系，只不过因为 `collections.abc` 是标准库中定义抽象基类的第一个模块，而它们又太重要了，因此才把它们放到 `collections.abc` 模块中
         - 这两个抽象基类的主要作用是为内置函数 `isinstance `提供支持，以一种安全的方式判断对象能不能调用或散列
         - 若想检查是否能调用，可以使用内置的 callable() 函数；但是没有类似的 hashable() 函数，因此测试对象是否可散列，最好使用 `isinstance(my_obj, Hashable)`

      6. Iterator

         - Iterable 的子类

   9. 抽象基类的金字塔

      1. numbers包定义的是 **数字塔**
         - Number
         - Complex
         - Real
         - Rational
         - Integral
      2. 检查一个数是不是整数：`isinstance(x, numbers.Integral)`，这样代码就可以接受int、bool
      3. 检查一个数是不是浮点数：`isinstance(x, number.Real)`，这样代码就可以接受bool、int、float、fractions.Fraction，还有外部库如Numpy
      4. deciaml.Decimal没有注册为numbers.Real的虚拟子类，是因为，如果你的程序需要Decimal的精度，要防止与其他低精度数字类型混合，尤其是浮点数

   10. 定义并使用一个抽象基类

       1. 抽象方法示例：

          ```python
          import abc
          
          class Tombola(abc.ABC):
              @abc.abstractmethod
              def load(self, iterable):
                  """从可迭代对象中添加元素"""
              
              @abc.abstractmethod
              def pick(self):
                  """随机删除元素，然后将其返回
                  如果实例为空，这个方法应该抛出 LookupError
                  """
              
              def loaded(self):
                  """如果至少有一个元素，返回True，否则返回False"""
                  return bool(self.inspect())
              
              def inspect(self):
                  """返回一个有序元组，由当前元素构成"""
                  items = []
                  while True:
                      try:
                          items.append(self.pick())
                      except LookupError:
                          break
                  self.load(items)
                  return tuple(sorted(items))
          ```

       2. 抽象方法可以有实现代码。即便实现了，子类也必须覆盖抽象方法，但是在子类中可以使用 super() 函数调用抽象方法，为它添加功能，而不是从头开始实现

       3. IndexEror和KeyError是LookupError的子类

          1. IndexError：尝试从序列中获取索引超过最后位置的元素时抛出
          2. KeyError：使用不存在的键从映射中获取元素时，抛出 KeyError 异常

   11. 抽象基类语法详解

       1. 可以通过装饰器堆叠的方式，声明抽象类方法、抽象静态方法、抽象属性等。

          ```python
          class MyABC(abc.ABC):
              @classmethod
              @abc.abstractmethod
              def an_abstract_classmethod(cls, ...):
                  pass
          ```

       2. 与其他方法描述符一起使用时，`abstractmethod()` 应该放在 **最里层**

       3. 唯一推荐使用的抽象基类方法装饰器是@abstractmethod，其他装饰器已经废弃了

   12. 定义Tombola抽象基类的子类

       1. 就算iterable参数始终传入列表，`list(iterable)`会创建参数的副本，这依然是好的做法
       
       2. **白鹅类型** 的重要动态特性：使用register方法声明虚拟子类
       
       3. [Python中的鸭子类型和白鹅类型](https://blog.csdn.net/m0_37579176/article/details/113883461)
       
          > **鸭子类型与继承毫无关系。**
          >
          > - 鸭子类型的定义是：
          >   “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
          > - 言简意赅的理解是：
          >   “对象的类型无关紧要，只要实现了特定的协议即可。忽略对象真正的类型，转而关注对象有没有实现所需的方法、签名和语义。”
          > - 最直接的结果就是：
          >   - 一个用户定义的类型，不需要真正的继承自抽象基类，但是却可以当作其子类一样来使用。
          >   - 比如用户实现了序列协议，就可以当作内置序列类型来用，对其使用`len()`等函数，调用`__len__()`等用于内置类型的方法。
          >   - 比如用户实现了`__getitem__`方法，Python就可以直接去迭代这个类型。
          >   - Python内置库和第三方的库，虽然是针对Python的类型设计的，但是都可以直接用于用户自定义的类型上。
          >
          > **而白鹅类型与此恰好相反。**
          >
          > - 白鹅类型的定义是：
          >   使用抽象基类明确声明接口，子类显示地继承抽象基类，抽象基类会检查子类是否符合接口定义。
          > - 这样做的劣势是：
          >   子类为了经过抽象基类的接口检查，必须实现一些接口，但是这些接口你可能用不到。
          > - 这样做的优势是：
          >   一些直接继承自抽象基类的接口是可以拿来即用的。
       
   13. Tombola的虚拟子类

       ```python
       @Tombola.register
       class TomboList(list):
           def pick(self):
               if self:
                   position = randrange(len(self))
                   return self.pop(position)
               else:
                   raise LookupError('pop from empty TomboList')
               
           load = list.extend
           
           def loaded(self):
               return bool(self)
           
           def inspect(self):
               return tuple(sorted(self))
           
       # Tombola.register(TomTomboList)
       ```

       1. 白鹅类型的一个基本特性：即便不继承，也有办法把一个类注册为抽象基类的虚拟子类。
       2. 注册虚拟子类的方式是在抽象基类上调用 register 方法
       3. 这么做之后，注册的类会变成抽象基类的虚拟子类，而且 issubclass 和isinstance 等函数都能识别
       4. 但是注册的类不会从抽象基类中继承任何方法或属性
       5. 虚拟子类不会继承注册的抽象基类，而且任何时候都不会检查它是否符合抽象基类的接口，即便在实例化时也不会检查。为了避免运行时错误，虚拟子类要实现所需的全部方法。
       6. `load = list.extend`，load跟list的extend一样。

   14. 类的继承关系在一个特殊的类属性中指定—— `__mro__`，即方法解析顺序（Method Resolution Order）

       1. 这个属性的作用很简单，按顺序列出类及其超类，Python 会按照这个顺序搜索方法
       2. 它只列出了“真实的”超类，利用`@类名.register`集成的不在其中，所以也没有从中继承任何方法

   15. Tombola子类的测试方法

       1. `__subclasses__()`：这个方法返回类的直接子类列表，不含虚拟子类
       2. `_abc_registry`：只有抽象基类有这个数据属性，其值是一个 WeakSet 对象，即抽象类注册的虚拟子类的弱引用

   16. **问题**：报错没有找到`_abc_registry`，

       - 这是因为，python3.7版本没有，需要用3.4才行，[参考链接](https://www.cnblogs.com/fanlumaster/p/14461500.html)

       - 并且在3.7的版本中是不能获取到这个属性的

   17. Python使用register的方式

       - 虽然现在可以把 register 当作装饰器使用了，但更常见的做法还是把它当作函数使用，用于注册其他地方定义的类

   18. 鹅的行为有可能像鸭子

       - 即便不注册，抽象基类也能把一个类识别为虚拟子类

       - 比如一个类实现了`__len__()`方法：

         ```python
         class Struggle:
             def __len__(self):
                 return 23
         ```

       - 然后可以看到这个类是Sized抽象基类的虚拟子类

         ```python
         from collections import abc
         
         isinstance(Struggle(), abc.Sized)
         # True
         issubclass(Struggle, abc.Sized)
         # True
         ```

       - 这是因为`abc.Sized`实现了一个特殊的类方法：`__sunclasshook__`

   19. `__subclasshook__ `在白鹅类型中添加了一些鸭子类型的踪迹。

       - 我们可以使用抽象基类定义正式接口，可以始终使用 isinstance 检查
       - 也可以完全使用不相关的类，只要实现特定的方法即可（或者做些事情让`__subclasshook__ `信服）
       - 当然，只有提供 `__subclasshook__ `方法的抽象基类才能这么做。

   20. 在你我自己编写的抽象基类中实现 `__subclasshook__ `方法，可靠性很低

       - 程序员最好让 Spam **继承** Tombola，至少也要**注册**（Tombola.register(Spam)）
       - 自己实现的 `__subclasshook__ `方法还可以检查方法签名和其他特性，但我觉得不值得这么做

   21. 强类型和弱类型

       1. 如果一门语言很少隐式转换类型，说明它是强类型语言；如果经常这么做，说明它是弱类型语言
       2. Java、C++ 和 Python 是强类型语言
       3. PHP、JavaScript 和 Perl 是弱类型语言

   22. 静态类型和动态类型

       1. 在编译时检查类型的语言是静态类型语言，在运行时检查类型的语言是动态类型语言
       2. 静态类型需要声明类型（有些现代语言使用类型推导避免部分类型声明）
       3. Fortran 和 Lisp 是最早的两门语言，现在仍在使用，它们分别是静态类型语言和动态类型语言

   23. 小结

       1. 强类型能及早发现缺陷
       2. 静态类型使得一些工具（编译器和 IDE）便于分析代码、找出错误和提供其他服务（优化、重构，等等）
       3. 动态类型便于代码重用，代码行数更少，而且能让接口自然成为协议而不提早实行
       4. **Python 是动态强类型语言**

   24. 猴子补丁

       1. 猴子补丁的名声不太好。如果滥用，会导致系统难以理解和维护。补丁通常与目标紧密耦合，因此很脆弱。另一个问题是，打了猴子补丁的两个库可能相互牵绊，因为第二个库可能撤销了第一个库的补丁。
       2. 猴子补丁也有它的作用，例如可以在运行时让类实现协议。适配器设计模式通过实现全新的类解决这种问题。
       3. Python 不允许为内置类型打猴子补丁，这一局限能减少外部库打的补丁有冲突的概率

   25. 不把隐喻当作设计范式，而代之以“习惯用法的界面”

## 12. 继承的优缺点

1. 子类化内置类型很麻烦

   1. 内置类型不会调用用户定义的类覆盖的特殊方法
   2. 内置类型的方法不会调用子类覆盖的方法
   3. 直接子类化内置类型（如 dict、list 或 str）容易出错，因为内置类型的方法通常会忽略用户覆盖的方法
   4. 不要子类化内置类型，用户自己定义的类应该继承 collections 模块中的类，例如UserDict、UserList 和 UserString，这些类做了特殊设计，因此易于扩展
   5. 如果子类化使用Python 编写的类，如 UserDict 或 MutableMapping，就不会受此影响

2. 多重继承和方法解析顺序

   1. “菱形问题”：不相关的祖先类实现同名方法引起的冲突
   2. Python 会按照特定的顺序遍历继承图，这个顺序叫方法解析顺序（Method Resolution Order, MRO）
   3. 直接在类上调用实例方法时，必须显式传入 self 参数，因为这样访问的是未绑定方法（unbound method）
   4. 使用 super() 最安全，也不易过时。调用框架或不受自己控制的类层次结构中的方法时，尤其适合使用 super()
   5. 使用 super() 调用方法时，会遵守方法解析顺序
   6. 方法解析顺序不仅考虑继承图，还考虑子类声明中列出超类的顺序，**先声明的先调用你敢信？**没事多看看`__mro__`属性吧，按这个顺序调用。

3. 多重继承的真实应用（以Tkinter为例）

   - Toplevel 是所有图形类中唯一没有继承 Widget 的，因为它是顶层窗口，行为不像小组件，例如不能依附到窗口或窗体上
   - Toplevel 继承自 Wm，后者提供直接访问宿主窗口管理器的函数，例如设置窗口标题和配置窗口边框
   - Widget 直接继承自 BaseWidget，还继承了 Pack、Place 和Grid。后三个类是几何管理器，负责在窗口或窗体中排布小组件。各个类封装了不同的布局策略和小组件位置 API

4. 处理多重继承

   1. 下面是避免把类图搅乱的一些建议

      1. 把接口继承和实现继承区分开

         - 继承接口，创建子类型，实现“是什么”关系
         - 继承实现，通过重用避免代码重复

      2. 使用抽象基类显式表示接口

      3. 通过混入重用代码

         - 如果一个类的作用是为多个不相关的子类提供方法实现，从而实现重用，但不体现“是什么”关系，应该把那个类明确地定义为混入类（mixin class）
         - 从概念上讲，混入不定义新类型，只是打包方法，便于重用
         - 混入类绝对不能实例化，而且具体类不能只继承混
           入类
         - 混入类应该提供某方面的特定行为，只实现少量关系非常紧密的方法

      4. 在名称中明确指明混入

         因为在 Python 中没有把类声明为混入的正规方式，所以强烈推荐在名称中加入 ...Mixin 后缀

      5. 抽象基类可以作为混入，反过来则不成立

      6. 不要子类化多个具体类

         - 具体类可以没有，或最多只有一个具体超类
         - 具体类的超类中除了这一个具体超类之外，其余的都是抽象基类或混入

      7. 为用户提供聚合类

         - 如果抽象基类或混入的组合对客户代码非常有用，那就提供一个类，使用易于理解的方式把它们结合起来。Grady Booch 把这种类称为聚合类（aggregate class）
         - 例如`tkinter.Widget`类中继承了多个抽象基类/混入：`class Widget(BaseWidget, Pack, Place, Grid):pass`
         - Widget 类的定义体是空的，但是这个类提供了有用的服务：把四个超类结合在一起，这样需要创建新小组件的用户无需记住全部混入，也不用担心声明 class 语句时有没有遵守特定的顺序

      8. “优先使用对象组合，而不是类继承”

         组合和委托可以代替混入，把行为提供给不同的类，但是不能取代接口继承去定义类型层次结构

         - [依赖、关联、聚合、组合](https://blog.csdn.net/lwwl12/article/details/82463441)
         - [混入](https://www.cnblogs.com/baxianhua/p/10881599.html)，[python多继承和混入类](https://blog.csdn.net/weixin_51194902/article/details/112605192)，混入类就是多重继承的一种实现技巧，为了防止类的指数增长，为了使具体类具有多个独立、解耦的功能（个人想法）

   2. KISS 原则：KISS 原则是用户体验的高层境界，简单地理解这句话，就是要把一个产品做得连白痴都会用，因而也被称为“懒人原则”。

      - Keep it Simple and Stupid

   3. 内置类型：dict、list 和 str 类型

      1. 是 Python 的底层基础，速度必须快，与这些内置类型有关的任何性能问题几乎都会对其他所有代码产生重大影响
      2. CPython 走了捷径，故意让内置类型的方法行为不当，即不调用被子类覆盖的方法
      3. 解决这一困境的可能方式之一是，为这些类型分别提供两种实现：一种供内部使用，为解释器做了优化；另一种供外部使用，便于扩展（UserDict、UserList 和 UserString）

   4. 多重分派：

      1. 分派就是指根据变量的类型选择相应的方法，单分派指的是指根据第一个参数类型去选择方法。
      2. 函数func()的结果只跟第一个参数的类型有关，跟后面的参数没有关系，这就是单分派。
      3. 使用函数的所有参数，而非只用第一个，来决定调用哪个方法被称为多重分派。

## 13. 正确重载运算符

1. 运算符重载基础

   1. Python 施加了一些限制，做好了灵活性、可用性和安全性方面的平衡：
      1. 不能重载内置类型的运算符
      2. 不能新建运算符，只能重载现有的
      3. 某些运算符不能重载——is、and、or 和 not（不过位运算符 &、| 和 ~ 可以）

2. 一元运算符

   1. 常见的运算符和对应的特殊方法：

      1. `-`：`__neg__`，取负算术运算符
      2. `+`：`__pos__`，取正算术运算符
      3. `~`：`__invert__`，按位取反
         - 定义为 $~x == -(x+1)$
         - 如果x是2，那么~x == -3
      4. `abs()`：`__abs__`，取绝对值

   2. x 和 +x 何时不相等

      1. jupyter和ipython中无法重现例子，但是cmd可以

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/79b23f17557943638fff66adb0edf39c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      2. Counter的例子

         1. Counter 相加时，负值和零值计数会从结果中剔除
         2. 而一元运算符 + 等同于加上一个空 Counter，因此它产生一个新的 Counter 且仅保留大于零的计数器
         3. 什么意思呢，就是说，如果使用Counter对序列进行计数之后，然后给部分key负值为0或者负值，然后在前面使用+算术运算符，就会导致负值和0对应的`key:value`键值对剔除。

3. 重载向量加法运算符+

   1. `__radd__`和`__rsub__`中的r：reflected（反射），reverse（反向），两种皆可，推荐使用反向
   2. r这种特殊的方法，是一种后备机制，如果左操作数没有实现对应的方法，或者实现了，但是返回的是`NotImplemented`表明它不知道如何处理右操作数，那么Python会调用r的方法。

4. 重载标量乘法运算符*

   1. `Vector([1, 2, 3]) * x `：计算标量积（scalar product），结果是一个新Vector实例，各个分量都会乘以x，这也叫元素级乘法（elementwise multiplication）
   2. 在Numpy库中，点积使用`numpy.dot()`计算
   3. Python3.5起，引入`@`用作中缀点击运算符
   4. `__mul__`和`__rmul__`方法
   5. decimal.Decimal 没有把自己注册为 numbers.Real 的虚拟子类。因此，Vector 类不会处理decimal.Decimal 数字。

5. 中缀运算符方法的名称

   |  运算符   |    正向方法    |    反向方法     |    就地方法     |              说明              |
   | :-------: | :------------: | :-------------: | :-------------: | :----------------------------: |
   |     +     |   `__add__`    |   `__radd__`    |   `__iadd__`    |           加法或拼接           |
   |     -     |   `__sub__`    |   `__rsub__`    |   `__isub__`    |              减法              |
   |     *     |   `__mul__`    |   `__rmul__`    |   `__imul__`    |         乘法或重复复制         |
   |     /     | `__truediv__`  | `__rtruediv__`  | `__itruediv__`  |              除法              |
   |    //     | `__floordiv__` | `__rfloordiv__` | `__ifloordiv__` |              整除              |
   |     %     |   `__mod__`    |   `__rmod__`    |   `__imod__`    |              取模              |
   | divmod()  |  `__divmod__`  |  `__rdivmod__`  |  `__idivmod__`  | 返回由整除的商和模数组成的元组 |
   | **, pow() |   `__pow__`    |   `__rpow__`    |   `__ipow__`    |              取幂              |
   |     @     |  `__matmul__`  |  `__rmatmul__`  |  `__imatmul__`  |            矩阵乘法            |
   |     &     |   `__add__`    |   `__radd__`    |   `__iadd__`    |              位与              |
   |    \|     |    `__or__`    |    `__ror__`    |    `__ior__`    |              位或              |
   |     ^     |   `__xor__`    |   `__rxor__`    |   `__ixor__`    |             位异或             |
   |    <<     |  `__lshift__`  |  `__rlshift__`  |  `__ilshift__`  |            按位左移            |
   |    >>     |  `__rshift__`  |  `__rrshift__`  |  `__irshift__`  |            按位右移            |

6. 众多比较运算符

   1. ==、!=、>、<、>=、<=
   2. 正向和反向调用使用的是同一系列方法
   3. 而正向的 `__gt__ `方法调用的是反向的 `__lt__ `方法，并把参数对调
   4. 对 == 和 != 来说，如果反向调用失败，Python 会比较对象的 ID，而不抛出 TypeError
   5. 众多比较运算符：正向方法返回`NotImplemented`的话，调用反向方法

7. 众多比较运算符

   |  分组  | 中缀运算符 | 正向方法调用  | 反向方法调用  |       后备机制       |
   | :----: | :--------: | :-----------: | :-----------: | :------------------: |
   | 相等性 |   a == b   | `a.__eq__(b)` | `b.__eq__(a)` | 返回`id(a) == id(b)` |
   |        |   a != b   | `a.__ne__(b)` | `b.__ne__(a)` |  返回`not(a == b)`   |
   |  排序  |   a > b    | `a.__gt__(b)` | `b.__lt__(a)` |    抛出TypeError     |
   |        |   a < b    | `a.__lt__(b)` | `b.__gt__(a)` |    抛出TypeError     |
   |        |   a >= b   | `a.__ge__(b)` | `b.__le__(a)` |    抛出TypeError     |
   |        |   a < b    | `a.__le__(b)` | `b.__ge__(a)` |    抛出TypeError     |

8. 增量赋值运算符

   1. 如果一个类没有实现上表列出的就地运算符，增量赋值运算符只是语法糖：a += b 的作用与 a = a + b 完全一样
   2. 如果实现了就地运算符方法，例如 `__iadd__`，计算 a += b 的结果时会调用就地运算符方法。这种运算符的名称表明，它们会就地修改左操作数，而**不会创建新对象作为结果**
   3. 不可变类型，一定不能实现就地特殊方法

9. 如果操作数的类型不同，我们要检测出不能处理的操作数。本章使用两种方式处理这个问题：

   1. 一种是鸭子类型，直接尝试执行运算，如果有问题，捕获 TypeError 异常
      - 鸭子类型更灵活，但是显式检查更能预知结果
   2. 另一种是显式使用 isinstance 测试，`__mul__ `方法就是这么做的
      - 如果选择使用 isinstance，要小心，不能测试具体类，而要测试 `numbers.Real `抽象基类，例如 `isinstance(scalar, numbers.Real)`
      - 这在灵活性和安全性之间做了很好的折中
   
10. 在可接受的类型方面，+ 应该比 += 严格

    - 对序列类型来说，+ 通常要求两个操作数属于同一类型
    - 而 += 的右操作数往往可以是任何可迭代对象

## 14. 可迭代的对象、迭代器和生成器

- 迭代器模式（Iterator pattern）：迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。
- 迭代器：用于从集合中取出元素
- 生成器：用于“凭空”生成元素
- 在 Python社区中，大多数时候都把迭代器和生成器视作同一概念

1. 单词序列

   1. 第一版Sentence

      ```python
      import re
      import reprlib
      
      RE_WORD = re.compile('\w+')
      
      class Sentence:
          def __init__(self, text):
              self.text = text
              self.words = RE_WORD.findall(text)
          
          def __getitem__(self, index):
              return self.words[index]
          
          def __len__(self):
              return len(self.words)
          
          def __repr__(self):
              return 'Sentence(%s)' % reprlib.repr(self.text)
      ```

   2. 序列可以迭代的原因：iter函数，解释器需要迭代对象 x 时，会自动调用 iter(x)。

   3. 内置的 iter 函数有以下作用：

      1. 检查对象是否实现了 `__iter__ `方法，如果实现了就调用它，获取一个迭代器
      2. 如果没有实现 `__iter__ `方法，但是实现了 `__getitem__` 方法，Python 会创建一个迭代器，尝试按顺序（从索引 0 开始）获取元素
      3. 如果尝试失败，Python 抛出 TypeError 异常，通常会提示“C object is not iterable”（C 对象不可迭代），其中 C 是目标对象所属的类

   4. 这是鸭子类型（duck typing）的极端形式：不仅要实现特殊的 `__iter__` 方法，还要实现 `__getitem__` 方法，而且 `__getitem__` 方法的参数是从 0 开始的整数（int），这样才认为对象是可迭代的

   5. 白鹅类型（goose typing）理论中，可迭代对象的定义简单一些，不过没那么灵活：如果实现了 `__iter__` 方法，那么就认为对象是可迭代的。此时，不需要创建子类，也不用注册，因为 abc.Iterable 类实现了 `__subclasshook__` 方法

   6. 检查对象 x 能否迭代，最准确的方法是：

      1. 调用 iter(x) 函数，如果不可迭代，再处理 TypeError 异常。
      2. 这比使用 isinstance(x, abc.Iterable) 更准确
      3. 因为 iter(x) 函数会考虑到遗留的 `__getitem__` 方法，而 abc.Iterable 类则
         不考虑

2. 可迭代的对象与迭代器的对比

   1. 可迭代的对象和迭代器之间的关系：Python 从可迭代的对象中获取迭代器
   2. StopIteration 异常表明迭代器到头了
   3. 标准的迭代器接口有两个方法：
      1. `__next__`：返回下一个可用的元素，如果没有元素了，抛出 StopIteration异常
      2. `__iter__`：返回 self，以便在应该使用可迭代对象的地方使用迭代器，例如在 for 循环中
   4. 在`Iterator(Iterable)`源码中，根据`__subclasshook__(cls, C)`函数识别C是不是Iterator的子类。这种方法是通过在`C.__mro__`中找是否同时存在`__next__`和`__iter__`方法
   5. 检查对象 x 是否为迭代器最好的方式是调用 `isinstance(x, abc.Iterator)`
   6. 代器是这样的对象：
      1. 实现了无参数的 `__next__` 方法，返回序列中的下一个元素；
      2. 如果没有元素了，那么抛出 StopIteration 异常
      3. Python 中的迭代器还实现了 `__iter__` 方法，因此迭代器也可以迭代

3. 典型的迭代器

   1. 构建==可迭代的对象==和==迭代器==时经常会出现错误，原因是**混淆了二者**

      1. 可迭代的对象有个 `__iter__` 方法，每次都实例化一个新的迭代器
      2. 而迭代器要实现 `__next__` 方法，返回单个元素，此外还要实现 `__iter__` 方法，返回迭代器本身

   2. **迭代器可以迭代，但是可迭代的对象不是迭代器**

   3. 迭代器模式可用来：

      1. 访问一个聚合对象的内容而无需暴露它的内部表示
      2. 支持对聚合对象的多种遍历
      3. 为遍历不同的聚合结构提供一个统一的接口（即支持多态迭代）

   4. 为了“支持多种遍历”，必须能从同一个可迭代的实例中获取多个**独立的迭代器**，而且各个迭代器要能维护自身的内部状态，因此这一模式正确的实现方式是，每次调用 iter(my_iterable) 都新建一个独立的迭代器。这就是为什么这个示例需要定义 SentenceIterator 类

   5. 可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现 `__iter__` 方法，但不能实现 `__next__ `方法

   6. 另一方面，迭代器应该一直可以迭代。迭代器的 `__iter__` 方法应该返回自身

   7. 第二版Sentence

      ```python
      import re
      import reprlib
      
      RE_WORD = re.compile('\w+')
      
      class Sentence:
          def __init__(self, text):
              self.text = text
              self.words = RE_WORD.findall(text)
          
          def __repr__(self):
              return 'Sentence(%s)' % reprlib.repr(self.text)
          
          def __iter__(self):
              return SentenceIterator(self.words)
          
      
      class SentenceIterator:
          def __init__(self, words):
              self.words = words
              self.index = 0
              
          def __next__(self):
              try:
                  word = self.words[self.index]
              except IndexError:
                  raise StopIteration()
              self.index += 1
              return word
          
          def __iter__(self):
              return self
      ```

4. 生成器函数

   1. 达到 **实现相同功能，但符合Python习惯** 的方式：用生成器函数代替SentenceIterator 类

      ```python
      import re
      import reprlib
      
      RE_WORD = re.compile('\w+')
      
      class Sentence:
          def __init__(self, text):
              self.text = text
              self.words = RE_WORD.findall(text)
          
          def __repr__(self):
              return 'Sentence(%s)' % reprlib.repr(self.text)
          
          def __iter__(self):
              for word in self.words:
                  yield word
              return 
      ```

   2. 这个 return 语句不是必要的；这个函数可以直接“落空”，自动返回。不管有没有 return 语句，生成器函数都不会抛出 StopIteration 异常，而是在生成完全部值之后会直接退出

   3. 生成器函数的工作原理

      1. 只要Python函数的定义体中有yield关键字，该函数就是生成器函数
      2. 调用生成器函数时，会返回一个生成器对象
      3. 也就是说，生成器函数是生成器工厂







 

学到 p610

