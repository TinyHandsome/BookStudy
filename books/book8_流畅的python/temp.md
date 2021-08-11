## 15. 上下文管理器和else块

> - with 语句会设置一个临时的上下文，交给上下文管理器对象控制，并且负责清理上下文
> - 这么做能避免错误并减少样板代码，因此 API 更安全，而且更易于使用
> - 了自动关闭文件之外，with 块还有很多用途

1. 先做这个，再做那个：if语句之外的else块

   1. else 子句不仅能在if 语句中使用，还能在 for、while 和 try 语句中使用
   2. else-for：仅当 for 循环运行完毕时（即 for 循环没有被 break 语句中止）才运行 else 块
   3. else-while：仅当 while 循环因为条件为假值而退出时（即 while 循环没有被 break 语句中止）才运行 else 块
   4. try-else：仅当 try 块中没有异常抛出时才运行 else 块，else 子句抛出的异常不会由前面的 except 子句处理
   5. 在所有情况下，如果异常或者 return、break 或 continue 语句导致控制权跳到了复合语句的主块之外，else 子句也会被跳过
   6. **这里在尝试理解的时候，可以把else理解为then，即，尝试运行这个，然后做那个，意思就是说，在运行for/while/try没有发生问题时，就运行else**

2. 上下文管理器和with块

   1. with 语句的目的是简化 try/finally 模式

   2. 上下文管理器协议包含 `__enter__` 和 `__exit__` 两个方法

      - with 语句开始运行时，会在上下文管理器对象上调用 `__enter__` 方法
      - with 语句运行结束后，会在上下文管理器对象上调用 `__exit__` 方法

   3. 执行 with 后面的表达式得到的结果是上下文管理器对象

   4. 不过，把值绑定到目标变量上（as 子句）是在上下文管理器对象上调用 `__enter__` 方法的结果

   5. 解释器调用 `__enter__` 方法时，除了隐式的 self 之外，不会传入任何参数

   6. 传给 `__exit__` 方法的三个参数列举如下：

      1. `exc_type`：异常类（例如 ZeroDivisionError）
      2. `exc_value`：异常实例。有时会有参数传给异常构造方法，例如错误消息，这些参数可以使用 exc_value.args 获取
      3. `traceback`：traceback 对象

   7. 例子

      ```python
      class LookingGlass:
          def __enter__(self):
              import sys
              self.original_write = sys.stdout.write
              sys.stdout.write = self.reverse_write
              return 'JABBERWOCKY'
          
          def reverse_write(self, text):
              self.original_write(text[::-1])
              
          def __exit__(self, exc_type, exc_value, traceback):
              import sys
              sys.stdout.write = self.original_write
              if exc_type is ZeroDivisionError:
                  print(exc_type, exc_value, traceback)
                  print('Please DO NOT divide by zero')
                  return True
      ```

3. contextlib模块中的实用工具

   1. closing：如果对象提供了 close() 方法，但没有实现 `__enter__/__exit__` 协议，那么可以使用这个函数构建上下文管理器

   2. suppress：构建临时忽略指定异常的上下文管理器

   3. **@contextmanager**（用得最多）：这个装饰器把简单的生成器函数变成上下文管理器，这样就不用创建类去实现管理器协议了

      **注意：**它与迭代无关，却要使用 yield 语句

   4. ContextDecorator：这是个基类，用于定义基于类的上下文管理器。这种上下文管理器也能用于装饰函数，在受管理的上下文中运行整个函数

   5. ExitStack：这个上下文管理器能进入多个上下文管理器

      - with 块结束时，ExitStack 按照后进先出的顺序调用栈中各个上下文管理器的 `__exit__` 方法
      - 如果事先不知道 with 块要进入多少个上下文管理器，可以使用这个类

4. 使用@contextmanager

   1. @contextmanager 装饰器能减少创建上下文管理器的样板代码量

   2. 只需实现有一个 yield 语句的生成器，生成想让 `__enter__` 方法返回的值

   3. 在使用 @contextmanager 装饰的生成器中，yield 语句的作用是把函数的定义体分成两部分：

      - yield 语句前面的所有代码在 with 块开始时（即解释器调用 `__enter__` 方法时）执行
      - yield 语句后面的代码在 with 块结束时（即调用 `__exit__` 方法时）执行

   4. 使用生成器实现的上下文管理器

      ```python
      import contextlib
      
      @contextlib.contextmanager
      def looking_glass():
          import sys
          original_write = sys.stdout.write
          
          def reverse_write(text):
              original_write(text[::-1])
          
          sys.stdout.write = reverse_write
          yield 'JABBERWOCKY'
          sys.stdout.write = original_write
      ```

   5. 其实，contextlib.contextmanager 装饰器会把函数包装成实现 `__enter__` 和 `__exit__` 方法的类；类的名称是 _GeneratorContextManager

   6. 这个类的 `__enter__` 方法有如下作用：

      1. 调用生成器函数，保存生成器对象（这里把它称为 gen）
      2. 调用 next(gen)，执行到 yield 关键字所在的位置
      3. 返回 next(gen) 产出的值，以便把产出的值绑定到 with/as 语句中的目标变量上

   7. with 块终止时，`__exit__` 方法会做以下几件事

      1. 检查有没有把异常传给 exc_type；如果有，调用 gen.throw(exception)，在生成器函数定义体中包含 yield 关键字的那一行抛出异常
      2. 否则，调用 next(gen)，继续执行生成器函数定义体中 yield 语句之后的代码

   8. 处理异常的代码：

      ```python
      import contextlib
      
      @contextlib.contextmanager
      def looking_glass():
          import sys
          original_write = sys.stdout.write
          
          def reverse_write(text):
              original_write(text[::-1])
          
          sys.stdout.write = reverse_write
          msg = ''
          try:
              yield 'JABBERWOCKY'
          except Exception:
              msg = '出错啦'
          finally:
              sys.stdout.write = original_write
              if msg:
                  print(msg)
      ```

   9. 使用 @contextmanager 装饰器时，要把 yield 语句放在try/finally 语句中（或者放在 with 语句中），这是无法避免的，因为我们永远不知道上下文管理器的用户会在 with 块中做什么

   10. 用于原地重写文件的上下文管理器

5. 在 @contextmanager 装饰器装饰的生成器中，yield 与迭代没有任何关系。在本节所举的示例中，生成器函数的作用更像是**协程**：**执行到某一点时暂停，让客户代码运行，直到客户让协程继续做事**

6. with 不仅能管理资源，还能用于去掉常规的设置和清理代码，或者在另一个过程前后执行的操作

7. @contextmanager 装饰器优雅且实用，把三个不同的 Python 特性结合到了一起：**函数装饰器**、**生成器**和 **with 语句**

## 16. 协程

> - 字典为动词“to yield”给出了两个释义：**产出**和**让步**
> - 对于 Python 生成器中的 yield 来说，这两个含义都成立
> - yield item 这行代码会产出一个值，提供给 next(...) 的调用方；此外，还会作出让步，暂停执行生成器，让调用方继续工作，直到需要使用另一个值时再调用next()

1. 生成器如何进化成协程
   1. 协程是指一个过程，这个过程与调用方协作，产出由调用方提供的值
   2. `.send(...)`：生成器的调用方可以使用 .send(...) 方法发送数据，发送的数据会成为生成器函数中 yield 表达式的值
   3. `.throw(...)`：让调用方抛出异常，在生成器中处理
   4. `.close()`：终止生成器
   
2. 用作协程的生成器的基本行为

   1. 协程使用生成器函数定义：定义体中有 yield 关键字

   2. 协程可以身处四个状态中的一个

   3. 当前状态可以使用 `inspect.getgeneratorstate(...)` 函数确定

      - GEN_CREATED：等待开始执行
      - GEN_RUNNING：解释器正在执行
      - GEN_SUSPENDED：在 yield 表达式处暂停
      - GEN_CLOSED：执行结束

   4. 仅当协程处于暂停状态时才能调用 send 方法

   5. 如果协程还没激活（即，状态是 'GEN_CREATED'）

      - 始终要调用 `next(my_coro)` 激活协程
      - 也可以调用 `my_coro.send(None)`，效果一样

   6. 我对yield在协程中使用的理解

      ```python
      def simple_coro2(a):
          print('-> Started: a =', a)
          b = yield a
          print('-> Received: b =', b)
          c = yield a + b
          print('-> Received: c =', c)
      ```

      - 拿这个例子为例
      - `b = yield a`：也就是说，程序运行到这一行的时候，先执行`yield a`，相当于`return a`，前面的`b = yield`是等待赋值
      - 然后使用`my_cc.send(28)`，就是给b赋值了，这一行才算运行结束
      - 所以这一行的运行，夹在了两个`next(my_cc)`中

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/a83392974a814599b506426723f717f2.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

3. 示例：使用协程计算移动平均值

   ```python
   def averager():
       total = 0.0
       count = 0
       average = None
       while True:
           term = yield average
           total += term
           count += 1
           average = total/count
   ```

   - 使用协程之前必须预激

4. 预激协程的装饰器

   - 为了简化协程的用法，有时会使用一个预激装饰器

     ```python
     from functools import wraps
     
     def coroutine(func):
         """装饰器：向前执行到第一个yield表达式，预激func"""
         @wraps(func)
         def primer(*args, **kwargs):
             gen = func(*args, **kwargs)
             next(gen)
             return gen
         return primer
     ```

   - 需要在协程的函数前面加这个装饰器

     ```python
     @coroutine
     def averager():
         total = 0.0
         count = 0
         average = None
         while True:
             term = yield average
             total += term
             count += 1
             average = total/count
     ```

   - 这样该协程的初始化的状态就是 GEN_SUSPENDED

     ```python
     from inspect import getgeneratorstate
     getgeneratorstate(coro_avg)
     
     # 'GEN_SUSPENDED'
     ```

   - 很多框架都提供了处理协程的特殊装饰器

     - 不是所有装饰器都用于预激协程
     - 有些会提供其他服务，例如勾入事件循环
     - 比如说，异步网络库 Tornado 提供了 tornado.gen 装饰器

   - 使用 yield from 句法调用协程时，会自动预激

   - Python 3.4 标准库里的 asyncio.coroutine 装饰器不会预激协程，因此能兼容 yield from 句法

5. 终止协程和异常处理

   1. 协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）

   2. 终止协程的一种方式：发送某个哨符值，让协程退出

   3. 内置的 None 和 Ellipsis 等常量经常用作哨符值

   4. 客户代码可以在生成器对象上调用两个方法，显式地把异常发给协程

      - generator.throw(exc_type[, exc_value[, traceback]])：致使生成器在暂停的 yield 表达式处抛出指定的异常
      - generator.close()：致使生成器在暂停的 yield 表达式处抛出 GeneratorExit 异常

   5. 学习在协程中处理异常的测试代码

      ```python
      class DemoException(Exception):
          """为这次演示定义的异常类型"""
          
      def demo_exc_handling():
          print('-> coroutine started')
          while True:
              try:
                  x = yield
              except DemoException:
                  print('*** DemoException handled. Continuing...')
              else:
                  print('-> coroutine received: {!r}'.format(x))
      
          raise RuntimeError('This line should never run.')
      ```

      - 最后一行代码不会执行，因为只有未处理的异常才会中止那个无限循环，而一旦出现未处理的异常，协程会立即终止
      - 激活和关闭 demo_exc_handling，没有异常
      - 把 DemoException 异常传入 demo_exc_handling 不会导致协程中止
      - 如果无法处理传入的异常，协程会终止

   6. 使用 try/finally 块在协程终止时执行操作

      ```python
      class DemoException(Exception):
          """为这次演示定义的异常类型"""
          
      def demo_exc_handling():
          print('-> coroutine started')
          try:
              while True:
                  try:
                      x = yield
                  except DemoException:
                      print('*** DemoException handled. Continuing...')
                  else:
                      print('-> coroutine received: {!r}'.format(x))
          finally:
              print('-> coroutine ending...')
      
          raise RuntimeError('This line should never run.')
      ```

   7. Python 3.3 引入 yield from 结构的主要原因

      - 与把异常传入嵌套的协程有关
      - 让协程更方便地返回值

6. 让协程返回值

   1. 定义一个求平均值的协程，让它返回一个结果

      ```python
      from collections import namedtuple
      
      Result = namedtuple('Result', 'count average')
      
      def averager():
          total = 0.0
          count = 0
          average = None
          while True:
              term = yield
              if term is None:
                  break
              total += term
              count += 1
              average = total/count
          return Result(count, average)
      ```

   2. 最后发送None的时候，协程结束，返回结果。抛出异常StopIteration，并将return的值保存到异常对象的value属性中

   3. 如何获取协程的返回值

      ```python
      try:
          coro_avg.send(None)
      except StopIteration as exc:
          result = exc.value
          
      result
      # Result(count=3, average=15.5)
      ```

   4. yield from 结构会在内部自动捕获 StopIteration 异常

7. 使用yield from

   1. yield from 可用于简化 for 循环中的 yield 表达式

      - 下述：

        ```python
        def gen():
            for c in 'AB':
                yield c
            for i in range(1, 3):
                yield i
        ```

      - 可改写为：

        ```python
        def gen():
            yield from 'AB'
            yield from range(1, 3)
        ```

   2. 相关术语

      1. 委派生成器：包含` yield from <iterable>` 表达式的生成器函数
      2. 子生成器：从 yield from 表达式中 `<iterable>` 部分获取的生成器
      3. 调用方：调用委派生成器的客户端代码

   3. 委派生成器在 yield from 表达式处暂停时，调用方可以直接把数据发给子生成器，子生成器再把产出的值发给调用方

   4. 子生成器返回之后，解释器会抛出 StopIteration 异常，并把返回值附加到异常对象上，此时委派生成器会恢复

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/61c8fb71888a43958bff468b042249dd.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   5. 如果子生成器不终止，委派生成器会在 yield from 表达式处永远暂停

      ```python
      from collections import namedtuple
      
      Result = namedtuple('Result', 'count average')
      
      # 子生成器 
      def averager():
          total = 0.0
          count = 0
          average = None
          while True:
              term = yield
              if term is None:
                  break
              total += term
              count += 1
              average = total/count
          return Result(count, average)
      
      # 委派生成器
      def grouper(results, key):
          while True:
              results[key] = yield from averager()
              
      # 客户端代码，即调用方
      def main(data):
          results = {}
          for key, values in data.items():
              group = grouper(results, key)
              next(group)
              for value in values:
                  group.send(value)
              # 重要
              group.send(None)
              report(results)
              
      # 输出报告
      def report(results):
          for key, result in sorted(results.items()):
              group, unit = key.split(';')
              print('{:2}{:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))
              
      data = {
      'girls;kg':
      [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
      'girls;m':
      [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
      'boys;kg':
      [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
      'boys;m':
      [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
      }
      
      if __name__ == '__main__':
          main(data)
      ```

   6. 委派生成器相当于管道，所以可以把任意数量个委派生成器连接在一起

   7. 一个委派生成器使用 yield from 调用一个子生成器，而那个子生成器本身也是委派生成器，使用 yield from 调用另一个子生成器，以此类推

   8. 最终，这个链条要以一个只使用 yield 表达式的简单生成器结束；不过，也能以任何可迭代的对象结束

   9. 任何 yield from 链条都必须由客户驱动，在最外层委派生成器上调用 next(...) 函数或 .send(...) 方法

8. yield from 的意义（6点 yield from 的行为）

   1. 子生成器产出的值都直接传给委派生成器的调用方（即客户端代码）
   2. 使用 send() 方法发给委派生成器的值都直接传给子生成器。如果发送的值是 None，那么会调用子生成器的 `__next__()` 方法。如果发送的值不是 None，那么会调用子生成器的 send() 方法。如果调用的方法抛出 StopIteration 异常，那么**委派生成器恢复运行**。任何其他异常都会向上冒泡，传给委派生成器
   3. 生成器退出时，生成器（或子生成器）中的 return expr 表达式会触发 StopIteration(expr) 异常抛出
   4. yield from 表达式的值是子生成器终止时传给 StopIteration 异常的第一个参数

   >  yield from 结构的另外两个特性与异常和终止有关

   5. 传入委派生成器的异常，除了 GeneratorExit 之外都传给子生成器的 throw() 方法。如果调用 throw() 方法时抛出 StopIteration 异常，委派生成器恢复运行。StopIteration 之外的异常会向上冒泡，传给委派生成器

   6. 如果把 GeneratorExit 异常传入委派生成器，或者在委派生成器上调用 close() 方法，那么在子生成器上调用 close() 方法，如果它有的话。

      如果调用 close() 方法导致异常抛出，那么异常会向上冒泡，传给委派生成器；否则，委派生成器抛出 GeneratorExit 异常

   - 通过阅读 yield from 的伪代码，我们可以看到代码里已经 预激了子生成器，这说明，用于自动预激的装饰器与 yield from 不兼容

9. 使用案例：使用协程做离散时间仿真

   1. 在计算机科学领域，仿真是协程的经典应用

   2. 通过仿真系统能说明如何使用协程代替线程实现并发的活动

   3. 离散事件仿真：Discrete Event Simulation，DES，是一种把系统建模成一系列事件的仿真类型

   4. 为了实现连续仿真，在多个线程中处理实时并行的操作更自然。而协程恰好为实现离散事件仿真提供了合理的抽象

   5. 一个示例：说明如何在一个主循环中处理事件，以及如何通过发送数据驱动协程

      ```python
      sim = Simulator(taxis)
      sim.run(end_time)
      ```

      ```python
      import queue
      
      class Simulator:
          def __init__(self, procs_map):
              self.events = queue.PriorityQueue()
              self.procs = dict(procs_map)
              
          def run(self, end_time): #1
              """排定并显示事件，直到时间结束"""
              # 排定各辆出租车的第一个事件
              for _, proc in sorted(self.procs.items()): #2
                  first_event = next(proc) #3
                  self.events.put(first_event) #4
              
              # 这个仿真系统的主循环
              sim_time = 0 #5
              while sim_time < end_time: #6
                  if self.events.empty(): #7
                      print('*** end of events ***')
                      break
                  
                  current_event = self.events.get() #8
                  sim_time, proc_id, previous_action = current_event #9
                  print('taxi:', proc_id, proc_id * '  ', current_event) #10
                  active_proc = self.procs[proc_id] #11
                  # 传入前一个动作，把结果加到sim_time上，获得下一次活动的时刻
                  next_time = sim_time + compute_duration(previous_action) #12
                  try:
                      next_event = active_proc.send(next_time) #13
                  except StopIteration:
                      del self.procs[proc_id] #14
                  else:
                      self.events.put(next_event) #15
              
              else: #16
                  msg = '*** end of simulation time: {} events pending ***'
                  print(msg.format(self.events.qsize()))            
      ```

10. 本章小结：

    1. 生成器有三种不同代码编写风格：
       - 传统的拉取式，迭代器
       - 推送式，计算平均值
       - 任务式，协程
    2. 









看到 P697