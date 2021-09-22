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
    2. 假如没有协程，我们要写一个并发程序。可能有以下问题：
       - 使用最常规的同步编程要实现异步并发效果并不理想，或者难度极高
       - 由于GIL锁的存在，多线程的运行需要频繁的加锁解锁，切换线程，这极大地降低了并发性能
    3. 而协程的出现，刚好可以解决以上的问题。它的特点有：
       - 协程是在单线程里实现任务的切换的
       - 利用同步的方式去实现异步
       - 不再需要锁，提高了并发性能
    4. [深入理解yield from](https://www.cnblogs.com/wongbingming/p/9085268.html)
    5. 事件驱动型框架（如 Tornado 和 asyncio）的运作方式：
       - 在单个线程中使用一个主循环驱动协程执行并发活动
       - 使用协程做面向事件编程时，协程会不断把控制权让步给主循环，激活并向前运行其他协程，从而执行各个并发活动
       - 这是一种协作式多任务：协程显式自主地把控制权让步给中央调度程序
       - 而多线程实现的是抢占式多任务。调度程序可以在任何时刻暂停线程（即使在执行一个语句的过程中），把控制权让给其他线程。
    6. 宽泛的、不正式的对协程的定义：通过客户调用 .send(...) 方法发送数据或使用 yield from 结构驱动的生成器函数
    7. asyncio 库建构在协程之上，不过采用的协程定义更为严格
       - 在 asyncio 库中，协程（通常）使用 @asyncio.coroutine 装饰器装饰
       - 而且始终使用 yield from 结构驱动
       - 而不通过直接在协程上调用 .send(...) 方法驱动
       - 当然，在 asyncio 库的底层，协程使用 next(...) 函数和 .send(...) 方法驱动，不过在用户代码中只使用 yield from 结构驱动协程运行
    8. SimPy 是使用标准的 Python 开发的基于进程的离散事件仿真框架，事件调度程序基于 Python 的生成器实现，因此还可用于异步网络或实现多智能体系统（即可模拟，也可真正通信）
    9. Python 3.5 已经接受了 PEP 492，增加了两个关键字：async 和 await
    10. [Python Async/Await入门指南](https://zhuanlan.zhihu.com/p/27258289)
        - 在3.5过后，我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器

## 17. 使用期物处理并发

- 期物：future，期物指一种对象，表示异步执行的操作
- 这个概念的作用很大，是 concurrent.futures 模块和 asyncio 包的基础

1. 网络下载的三种风格

   1. 对并发下载的脚本来说，每次下载的顺序都不同

   2. 拒绝服务：Denial-of-Service，DoS

   3. 在 I/O 密集型应用中，如果代码写得正确，那么不管使用哪种并发策略（使用线程或 asyncio 包），吞吐量都比依序执行的代码高很多

   4. 第一种，直接按顺序下载棋子

      ```python
      import os
      import time
      import sys
      
      import requests
      
      POP20_CC = ('CN IN US ID BR P1K NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()
      
      BASE_URL = 'http://flupy.org/data/flags'
      
      DEST_DIR = './downloads/'
      
      def save_flag(img, filename):
          path = os.path.join(DEST_DIR, filename)
          with open(path, 'wb') as fp:
              fp.write(img)
              
      def get_flag(cc):
          url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
          resp = requests.get(url)
          return resp.content
      
      def show(text):
          print(text, end=' ')
          sys.stdout.flush()
          
      def download_many(cc_list):
          for cc in sorted(cc_list):
              image = get_flag(cc)
              show(cc)
              save_flag(image, cc.lower() + '.gif')
              
          return len(cc_list)
      
      def main(download_many):
          t0 = time.time()
          count = download_many(POP20_CC)
          elapsed = time.time() - t0
          msg = '\n{} flags downloaded in {:.2f}s'
          print(msg.format(count, elapsed))
          
      if __name__ == '__main__':
          main(download_many)
          
      # BD BR CD CN DE EG ET FR ID IN IR JP MX NG P1K PH RU TR US VN 
      # 20 flags downloaded in 21.82s
      ```

   5. 第二种，使用`concurrent.futures`模块下载

      ```python
      from concurrent import futures
      
      from flags import save_flag, get_flag, show, main
      
      MAX_WORKERS = 20
      
      def download_one(cc):
          image = get_flag(cc)
          show(cc)
          save_flag(image, cc.lower() + '.gif')
          return cc
      
      def download_many(cc_list):
          # 设定工作的线程数：允许的最大值与要处理的数量之间的 最小值，以免创建多余的线程
          workers = min(MAX_WORKERS, len(cc_list))
          with futures.ThreadPoolExecutor(workers) as executor:
              res = executor.map(download_one, sorted(cc_list))
              
          return len(list(res))
      
      if __name__ == '__main__':
          main(download_many)
      
      # BD CD BR TR IR FR JP IN MX VNET  PH NG EG CN ID DE P1K US RU 
      # 20 flags downloaded in 1.05s
      ```

      - concurrent.futures 模块的主要特色是 ThreadPoolExecutor 和 ProcessPoolExecutor 类
      - 这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象
      - 这两个类在内部维护着一个工作线程或进程池，以及要执行的任务队列

   6. 从 Python 3.4 起，标准库中有两个名为 Future 的类：concurrent.futures.Future 和 asyncio.Future

   7. 期物封装待完成的操作，可以放入队列，完成的状态可以查询，得到结果（或抛出异常）后可以获取结果（或异常）

   8. 通常情况下自己不应该创建期物，而只能由并发框架（concurrent.futures 或 asyncio）实例化

   9. 原因很简单：期物表示终将发生的事情，而确定某件事会发生的唯一方式是执行的时间已经排定

   10. 因此，只有排定把某件事交给 concurrent.futures.Executor 子类处理时，才会创建 concurrent.futures.Future 实例

   11. 客户端代码不应该改变期物的状态，并发框架在期物表示的延迟计算结束后会改变期物的状态，而我们无法控制计算何时结束

   12. `.done()`：这个方法不阻塞，返回值是布尔值，指明期物链接的可调用对象是否已经执行

   13. `.add_done_callback() `：这个方法只有一个参数，类型是可调用的对象，期物运行结束后会调用指定的可调用对象

   14. `.result()`：返回可调用对象的结果，或者重新抛出执行可调用的对象时抛出的异常

       - 如果期物没有运行结束，result 方法在两个 Future 类中的行为相差很大
       - 对concurrency.futures.Future 实例来说，调用 `f.result()` 方法会阻塞调用方所在的线程，直到有结果可返回。此时，result 方法可以接收可选的 timeout 参数，如果在指定的时间内期物没有运行完毕，会抛出 TimeoutError 异常
       - asyncio.Future.result 方法不支持设定超时时间，在那个库中获取期物的结果最好使用 yield from 结构

   15. 这两个库中有几个函数会返回期物，其他函数则使用期物，以用户易于理解的方式实现自身

   16. Executor.map 方法属于后者：返回值是一个迭代器，迭代器的 `__next__` 方法调用各个期物的result 方法，因此我们得到的是各个期物的结果，而非期物本身

   17. `concurrent.futures.as_completed`：这个函数的参数是一个期物列表，返回值是一个迭代器，在期物运行结束后产出期物

   18. 把download_many 函数中的 executor.map 方法换成 executor.submit 方法和 futures.as_completed 函数

       ```python
       def download_many(cc_list):
           cc_list = cc_list[:5]
           with futures.ThreadPoolExecutor(max_workers=3) as executor:
               to_do = []
               for cc in sorted(cc_list):
                   future = executor.submit(download_one, c)
                   to_do.append(future)
                   msg = 'Scheduled for {}: {}'
                   print(msg.format(cc, future))
                   
               results = []
               for future in futures.as_completed(to_do):
                   res = future.result()
                   msg = '{} result: {!r}'
                   print(msg.format(future, res))
                   results.append(res)
                   
           return len(results)
       ```

   19. GIL：Global Interpreter Lock，全局解释器锁
   
   20. GIL 几乎对 I/O 密集型处理无害
   
2. 阻塞型I/O和GIL

   1. CPython 解释器本身就不是线程安全的，因此有全局解释器锁（GIL），一次只允许使用一个线程执行 Python 字节码
   2. 因此，一个 Python 进程通常不能同时使用多个 CPU 核心
   3. 编写 Python 代码时无法控制 GIL；不过，执行耗时的任务时，可以使用一个内置的函数或一个使用 C 语言编写的扩展释放 GIL
   4. 标准库中所有执行阻塞型 I/O 操作的函数，在等待操作系统返回结果时都会释放 GIL，这意味着在 Python 语言这个层次上可以使用多线程，而 I/O 密集型 Python 程序能从中受益
   5. 一个 Python 线程等待网络响应时，阻塞型 I/O 函数会释放 GIL，再运行一个线程

3. 使用concurrent.futures模块启动进程

   1. 如果需要做 CPU 密集型处理，使用这个模块的ProcessPoolExecutor类能绕开 GIL，利用所有可用的 CPU 核心
   2. 对简单的用途来说，ThreadPoolExecutor和ProcessPoolExecutor这两个实现Executor接口的类唯一值得注意的区别是，
      - `ThreadPoolExecutor.__init__`方法需要max_workers参数，制定线程池中线程的数量
      - 在 ProcessPoolExecutor 类中，那个参数是可选的，而且大多数情况下不使用——默认值是 `os.cpu_count()` 函数返回的 CPU 数量

4. 实验Executor.map方法

   1. Executor.map 函数返回结果的顺序与调用开始的顺序一致
   2. 不过，通常更可取的方式是，不管提交的顺序，只要有结果就获取。为此，要把 Executor.submit 方法和 futures.as_completed 函数结合起来使用
   3. executor.submit 和 futures.as_completed 这个组合比executor.map 更灵活，因为 submit 方法能处理不同的可调用对象和参数，而 executor.map 只能处理参数不同的同一个可调用对象
   4. 传给 futures.as_completed 函数的期物集合可以来自多个 Executor 实例

5. 显示下载进度并处理错误

   1. flags2系列示例处理错误的方式
   2. 使用`futures.as_completed`函数
   3. 线程和多进程的替代方案
      1. concurrent.futures 是使用线程的最新方式
      2. 如果 `futures.ThreadPoolExecutor` 类对某个作业来说不够灵活，可能要
         使用 threading 模块中的组件（如 Thread、Lock、Semaphore 等）自行制定方案
      3. 对 CPU 密集型工作来说，要启动多个进程，规避 GIL
      4. 创建多个进程最简单的方式是，使用 futures.ProcessPoolExecutor 类
      5. 如果使用场景较复杂，需要更高级的工具。使用 multiprocessing 模块，API 与 threading 模块相仿，不过作业交给多个进程处理
      6. multiprocessing 模块还能解决协作进程遇到的最大挑战：在进程之间传递数据
   
6. 小结

   1. 为什么尽管有 GIL，Python 线程仍然适合 I/O 密集型应用：准库中每个使用 C 语言编写的 I/O 函数都会释放 GIL，因此，当某个线程在等待 I/O 时， Python 调度程序会切换到另一个线程
   2. 借助 `concurrent.futures.ProcessPoolExecutor` 类使用多进程，以此绕
      开 GIL，使用多个 CPU 核心运行
   3. 对于 CPU 密集型和数据密集型并行处理，现在有个新工具可用——分布式计算引擎 **Apache Spark**，Spark 在大数据领域发展势头强劲，提供了友好的 Python API，支持把 Python 对象当作数据
   4. **`lelo`** 包：定义了一个@parallel 装饰器，可以应用到任何函数上，把函数变成非阻塞：调用被装饰的函数时，函数在一个新进程中执行
   5. **`python-parallelize`** 包提供了一个 parallelize 生成器，能把 for 循环分配给多个 CPU 执行
   6. 这两个包在内部都使用了 multiprocessing 模块
   7. GIL 简化了 CPython 解释器和 C 语言扩展的实现，得益于 GIL，Python 有很多 C 语言扩展
   8.  Python 线程特别适合在 I/O 密集型系统中使用
   9. 在 JavaScript 中，只能通过回调式异步编程实现并发

## 18. 使用asyncio包处理并发

1. 线程与协程对比

   1. spinner_thread.py

      ```python
      import threading
      import itertools
      import time
      import sys
      
      class Signal:
          go = True
          
      
      def spin(msg, signal):
          write, flush = sys.stdout.write, sys.stdout.flush
          for char in itertools.cycle('|/-\\'):
              status = char + ' ' + msg
              write(status)
              flush()
              write('\x08' * len(status))
              time.sleep(.1)
              if not signal.go:
                  break
          write(' ' * len(status) + '\x08' * len(status))
          
      def slow_function():
          # 假装等待I/O一段时间
          time.sleep(3)
          return 42
      
      def supervisor():
          signal = Signal()
          spinner = threading.Thread(target=spin, args=('thinking!', signal))
          print('spinner object:', spinner)
          spinner.start()
          result = slow_function()
          signal.go = False
          spinner.join()
          return result
      
      def main():
          result = supervisor()
          print('Answer:', result)
          
      if __name__ == '__main__':
          main()
      ```

   2. Python 没有提供终止线程的 API，这是有意为之的。若想关闭线程，必须给线程发送消息，这里是signal.go属性

   3. spinner_asyncio.py：通过协程以动画形式显示文本式旋转指针；使用 @asyncio.coroutine 装饰器替代线程，实现相同的行为
   
      ```python
      import asyncio
      import itertools
      import sys
      
      
      @asyncio.coroutine #1
      def spin(msg): #2
          write, flush = sys.stdout.write, sys.stdout, flush
          for char in itertools.cycle('|/-\\'):
              status = char + ' ' + msg
              write(status)
              flush()
              write('\x08' * len(status))
              try:
                  yield from asyncio.sleep(.1) #3
              except asyncio.CancelledError: #4
                  break
          write(' ' * len(status) + '\x08' * len(status))
          
      
      @asyncio.coroutine
      def slow_function(): #5
          # 假装等待I/O一段时间
          yield from asyncio.sleep(3) #6
          return 42
      
      @asyncio.coroutine
      def supervisor(): #7
          spinner = asyncio.async(spin('thinking!')) #8
          print('spinner object:', spinner) #9
          result = yield from slow_function() #10
          spinner.cancel() #11
          return result
      
      def main():
          loop = asyncio.get_event_loop() #12
          result = loop.run_until_complete(supervisor()) #13
          loop.close()
          print('Answer:', result)
          
      
      if __name__ == '__main__':
          main()
      ```
   
      1. 使用 `yield from asyncio.sleep(.1)` 代替 `time.sleep(.1)`，这样的休眠不会阻塞事件循环
      2. `asyncio.async(...)` 函数排定 spin 协程的运行时间，使用一个Task 对象包装 spin 协程，并立即返回
   
   4. 除非想阻塞主线程，从而冻结事件循环或整个应用，否则不要在 asyncio 协程中使用 `time.sleep(...)`。如果协程需要在一段时间内什么也不做，应该使用 `yield from asyncio.sleep(DELAY)`
   
   5. 两种 supervisor 实现之间的主要区别概述如下：
   
      1. asyncio.Task 对象差不多与 threading.Thread 对象等效
      2. Task 对象用于驱动协程，Thread 对象用于调用可调用的对象
      3. Task 对象不由自己动手实例化，而是通过把协程传给 `asyncio.async(...)` 函数或 loop.create_task(...) 方法获取
      4. 获取的 Task 对象已经排定了运行时间（例如，由 `asyncio.async` 函数排定）；Thread 实例则必须调用 start 方法，明确告知让它运行
      5. 在线程版 supervisor 函数中，slow_function 函数是普通的函数，直接由线程调用。在异步版 supervisor 函数中，slow_function 函数是协程，由 yield from 驱动
      6. 没有 API 能从外部终止线程，因为线程随时可能被中断，导致系统处于无效状态。如果想终止任务，可以使用 Task.cancel() 实例方法，在协程内部抛出 CancelledError 异常。协程可以在暂停的yield 处捕获这个异常，处理终止请求
      7. supervisor 协程必须在 main 函数中由 loop.run_until_complete 方法执行
   
   6. `asyncio.Future`：故意不阻塞
   
      1. asyncio.Future 类与 concurrent.futures.Future 类的接口基本一致，不过实现方式不同，不可以互换
      2. asyncio.Future 类的 .result() 方法没有参数，因此不能指定超时时间。此外，如果调用 .result() 方法时期物还没运行完毕，那么.result() 方法不会阻塞去等待结果，而是抛出asyncio.InvalidStateError 异常
      3. 使用 yield from 处理期物与使用 add_done_callback 方法处理协程的作用一样：延迟的操作结束后，事件循环不会触发回调对象，
         而是设置期物的返回值；而 yield from 表达式则在暂停的协程中生成
         返回值，恢复执行协程
      4. 因为 asyncio.Future 类的目的是与 yield from 一起使用，所以通常不需要使用以下方法
         1. 无需调用 my_future.add_done_callback(...)，因为可以直接把想在期物运行结束后执行的操作放在协程中 yield from my_future 表达式的后面。这是协程的一大优势：**协程是可以暂停和恢复的函数**
         2. 无需调用 my_future.result()，因为 yield from 从期物中产出的值就是结果（例如，result = yield from my_future）
   
   7. 从期物、任务和协程中产出
   
      1. 对协程来说，获取 Task 对象有两种主要方式：
   
         1. `asyncio.async(coro_or_future, *, loop=None)`
         2. `BaseEventLoop.create_task(coro)`
   
      2. 测试脚本中试验期物和协程：
   
         ```python
         import asyncio
         def run_sync(coro_or_future):
             loop = asyncio.get_event_loop()
             return loop.run_until_complete(coro_or_future)
         
         a = run_sync(some_coroutine())
         ```
   
2. 使用asyncio和aiohttp包下载

   1. flags_asyncio.py：使用 asyncio 和 aiohttp 包实现的异步下载脚本

      ```python
      import asyncio
      import aiohttp # 1
      from flags import BASE_URL, save_flag, show, main #2
      
      @asyncio.coroutine #3
      def get_flag(cc):
          url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
          resp = yield from aiohttp.request('GET', url) #4
          image = yield from resp.read() #5
          return image
      
      @asyncio.coroutine
      def download_one(cc): #6
          image = yield from get_flag(cc) #7
          show(cc)
          save_flag(image, cc.lower() + '.gif')
          return cc
      
      def download_many(cc_list):
          loop = asyncio.get_event_loop() #8
          to_do = [download_one(cc) for cc in sorted(cc_list)] #9
          wait_coro = asyncio.wait(to_do) #10
          res, _ = loop.run_until_complete(wait_coro) #11
          loop.close() #12
          	
          return len(res)
      
      
      if __name__ == '__main__':
          main(download_many)
      ```

      1. 虽然函数的名称是 asyncio.wait，但它不是阻塞型函数。wait 是一个协程，等传给它的所有协程运行完毕后结束
      2. wait 函数有两个关键字参数，如果设定了可能会返回未结束的期物；这两个参数是timeout 和 return_when
      
   2.  【我的理解】 协程，就是给函数加上了 `@asyncio.coroutine` 装饰器的函数，然后里面需要等待的地方加上了 `yield from` 语句，如果去掉这些语句，就是正常调用的阻塞型流程。
   
   3. `yield from foo` 句法能防止阻塞，是因为当协程（即包含yield from代码的委派生成器）暂停后，控制权回到事件循环手中，再去驱动其他协程；foo期物或协程运行完毕后，把结果返回给暂停的协程，将其恢复。
   
   4. 关于 yield from 的用法的两点陈述：
   
      1. 使用 yield from 链接的多个协程最终必须由不是协程的调用方驱动，调用方显式或隐式（例如，在 for 循环中）在最外层委派生成器上调用 next(...) 函数或 .send(...) 方法
      2. 链条中最内层的子生成器必须是简单的生成器（只使用 yield）或 可迭代的对象
   
   5. 在 asyncio 包的 API 中使用 yield from 时，上述两点都成立，不过要注意下述细节：
   
      1. 我们编写的协程链条始终通过把最外层委派生成器传给 asyncio 包 API 中的某个函数（如 loop.run_until_complete(...)）驱动。也就是说，使用 asyncio 包时，我们编写的代码不通过调用 next(...) 函数或 .send(...) 方法驱动协程——这一点由asyncio 包实现的事件循环去做
   
      2. 我们编写的协程链条最终通过 yield from 把职责委托给 asyncio 包中的某个协程函数或协程方法（例如：yield from asyncio.sleep(...)），或者其他库中实现高层协议的协程（例如：resp = yield from aiohttp.request('GET', url)）
   
         也就是说，最内层的子生成器是库中真正执行 I/O 操作的函数，而
         不是我们自己编写的函数
   
   6. 概括起来就是：使用 asyncio 包时，我们编写的异步代码中包含由 asyncio 本身驱动的协程（即委派生成器），而生成器最终把职责委托给 asyncio 包或第三方库（如 aiohttp）中的协程。这种处理方式相当于架起了管道，让 asyncio 事件循环（通过我们编写的协程）驱动执行低层异步 I/O 操作的库函数
   
3. 避免阻塞型调用

   1. 有两种方法能避免阻塞型调用中止整个应用程序的进程：
      1. 在单独的线程中运行各个阻塞型操作
      2. 把每个阻塞型操作转换成非阻塞的异步调用使用
   2. 为了降低内存的消耗，通常使用回调来实现异步调用
   3. 使用回调时，我们不等待响应，而是注册一个函数，在发生某件事时调用。这样，所有调用都是非阻塞的
   4. 只有异步应用程序底层的事件循环能依靠基础设置的中断、线程、轮询和后台进程等，确保多个并发请求能取得进展并最终完成，这样才能使用回调
   5. 把生成器当作协程使用是异步编程的另一种方式。对事件循环来说，调用回调与在暂停的协程上调用 .send() 方法效果差不多。各个暂停的协程是要消耗内存，但是比线程消耗的内存数量级小。而且，协程能避免可怕的“回调地狱”
   6. [异步和协程](https://www.cnblogs.com/lateink/p/7523011.html)

4. 改进asyncio下载版本

   1. 使用 asyncio.as_completed 函数
   
   2. raise X from Y：链接原来的异常
   
   3. Semaphore对象维护着一个内部计数器，若在对象调用 .acquire() 协程方法，计数器则递减；若在对象上调用 .release() 协程方法，计数器则递增。
   
   4. 如果计数器大于0，那么调用 .acquire() 方法不会阻塞；可是，如果计数器为0，那么 .acquire() 方法会阻塞调用这个方法的协程，直到其他协程在同一个Semaphore对象上调用 .release() 方法，让计数器递增。
   
   5. flags2_asyncio.py
   
      ```python
      import asyncio
      import collections
      
      import aiohttp
      from aiohttp import web
      import tqdm
      
      from flags2_common import main, HTTPStatus, Result, save_flag
      
      # 默认设为较小的值，防止远程网站出错
      # 例如503 - Service Temporarily Unavaliable
      DEFAULT_CONCUR_REQ = 5
      MAX_CONCUR_REQ = 1000
      
      class FetchError(Exception): #1
          def __init__(self, country_code):
              self.country_code = country_code
              
      @asyncio.coroutine
      def get_flag(base_url, cc): #2
          url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
          resp = yield from aiohttp.request('GET', url)
          if resp.status == 200:
              image = yield from resp.read()
              return image
          elif resp.status == 404:
              raise web.HTTPNotFound()
          else:
              raise aiohttp.HttpProcessingError(code=resp.status, message=resp.reason, headers=resp.headers)
      
      @asyncio.coroutine
      def download_one(cc, base_url, semaphore, verbose): #3
          # semaphore: 信号标
          try:
              with (yield from semaphore): #4
                  image = yield from get_flag(base_url, cc) #5
          except web.HTTPNotFound: #6
              status = HTTPStatus.not_found
              msg = 'not found'
          except Exception as exc:
              raise FetchError(cc) from exc #7
          else:
              save_flag(image, cc.lower() + '.gif') #8
              status = HTTPStatus.ok
              msg = 'OK'
              
          if verbose and msg:
              print(cc, msg)
          
          return Result(status, cc)
      
      @asyncio.coroutine
      def downloader_coro(cc_list, base_url, verbose, concur_req): #1
          counter = collections.Counter()
          semaphore = asyncio.Semaphore(concur_req) #2
          to_do = [download_one(cc, base_url, semaphore, verbose) for cc in sorted(cc_list)] #3
          
          to_do_iter = asyncio.as_completed(to_do) #4
          if not verbose:
              to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list)) #5
          for future in to_do_iter: #6
              try:
                  res = yield from future #7
              except FetchError as exc: #8
                  country_code = exc.country_code #9
                  try:
                      error_msg = exc.__cause__.args[0] #10
                  except IndexError:
                      error_msg = exc.__cause__.__class__.__name__ #11
                  if verbose and error_msg:
                      msg = '*** Error for {}: {}'
                      print(msg.format(country_code, error_msg))
                  status = HTTPStatus.error
              else:
                  status = res.status
                  
              counter[status] += 1 #12
              
          return counter #13
      
      def download_many(cc_list, base_url, verbose, concur_req):
          loop = asyncio.get_event_loop()
          coro = downloader_coro(cc_list, base_url, verbose, concur_req)
          counts = loop.run_until_complete(coro) #14
          loop.close() #15
          return counts
      
      if __name__ == '__main__':
          main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
      ```
   
   6. 获取 asyncio.Future 对象的结果，最简单的方法是使用 yield from，而不是调用 future.result() 方法
   
   7. 因为失败时不能以期物为键从字典中获取国家代码，所以实现了自定义的 FetchError 异常，包装网络异常，并关联相应的国家代码，因此在详细模式中报告错误时能显示国家代码。
   
5. 使用Executor对象，防止阻塞事件循环

   1. asyncio 的事件循环在背后维护着一个 ThreadPoolExecutor 对象，我们可以调用 run_in_executor 方法，把可调用的对象发给它执行。

   2. 在 download_one函数中，save_flag函数会阻塞客户代码与 asyncio 事件循环公用的唯一线程，因此保存文件时，整个应用程序都会冻结。

   3. 解决方案：

      1. 之前的 download_one 函数中

         ```python
         @asyncio.coroutine
         def download_one(cc, base_url, semaphore, verbose):
             try:
                 ...
             else:
                 save_flag(image, cc.lower() + '.gif')
                 status = HTTPStatus.ok
                 msg = 'OK'
                 
             if verbose and msg:
                 ...
         ```

      2. 修改之后的代码

         ```python
         @asyncio.coroutine
         def download_one(cc, base_url, semaphore, verbose):
             try:
                 ...
             else:
                 loop = asyncio.get_event_loop()
                 loop.run_in_executor(None, save_flag, image, cc.lower() + '.gif')
                 status = HTTPStatus.ok
                 msg = 'OK'
                 
             if verbose and msg:
                 ...
         ```

      3. run_in_executor 方法的第一个参数是 Executor 实例，如果设为None，使用事件循环的默认 ThreadPoolExecutor 实例。

6. 从回调到期物和协程

   1. 使用协程和yield from结构做异步编程，无需使用回调

      ```python
      @asyncio.coroutine
      def three_stages(request1):
          reponse1 = yield from api_call1(request1)
          request2 = step1(response1)
          response2 = yield from api_call2(request2)
          request3 = step2(response2)
          response3 = yield from api_call3(request3)
          step3(response3)
          
      # 必须显示调度执行
      loop.create_task(three_stages(request1))
      ```

   2. 每次下载发起多次请求

      ```python
      @asyncio.coroutine
      def http_get(url):
          res = yield from aiohttp.request('GET', url)
          if res.status == 200:
              ctype = res.headers.get('Content-type', '').lower()
              if 'json' in ctype or url.endswith('json'):
                  data = yield from res.json() #1
              else:
                  data = yield from res.read() #2
              return data
          
          elif res.status == 404:
              raise web.HTTPNotFound()
          else:
              raise aiohttp.errors.HttpProcessingError(code=res.status, message=res.reason, headers=res.headers)
              
      @asyncio.coroutine
      def get_country(base_url, cc):
          url = '{}/{cc}/metadata.json'.format(base_url, cc=cc.lower())
          metadata = yield from http_get(url) #3
          return metadata['country']
      
      @asyncio.coroutine
      def get_flag(base_url, cc):
          url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
          return (yield from http_get(url)) #4
      
      @asyncio.coroutine
      def download_one(cc, base_url, semaphore, verbose):
          try:
              with (yield from semaphore): #5
                  image = yield from get_flag(base_url, cc)
              with (yield from semaphore):
                  country = yield from get_country(base_url, cc)
          except web.HTTPNotFound:
              status = HTTPStatus.not_found
              msg = 'not found'
          except Exception as exc:
              raise FetchError(cc) from exc
          else:
              country = country.replace(' ', '_')
              filename = '{}-{}.gif'.format(country, cc)
              loop = asyncio.get_event_loop()
              loop.run_in_executor(None, save_flag, image, filename)
              status = HTTPStatus.ok
              msg = 'ok'
          
          if verbose and msg:
              print(cc, msg)
              
          return Result(status, cc)
      ```

7. 使用asyncio包编写服务器

   1. 使用asyncio包编写TCP服务器

      ```python
      import sys
      import asyncio
      
      from charfinder import UnicodeNameIndex #1
      
      CRLF = b'\r\n'
      PROMPT = b'?>'
      
      index = UnicodeNameIndex() #2
      
      @asyncio.coroutine
      def handle_queries(reader, writer): #3
          while True: #4
              writer.write(PROMPT) # 不能使用yield from #5
              yield from writer.drain() # 必须使用 yield from #6
              data = yield from reader.readline() #7
              try:
                  query = data.decode().strip()
              except UnicodeDecodeError: #8
                  query = '\x00'
              client = writer.get_extra_info('peername') #9
              print('Received from {}: {!r}'.format(client, query)) #10
              if query:
                  if ord(query[:1]) < 32: #11
                      break
                  lines = list(index.find_description_strs(query)) #12
                  if lines:
                      writer.writelines(line.encode() + CRLF for line in lines) #13
                  writer.write(index.status(query, len(lines)).encode() + CRLF) #14
                  
                  yield from writer.drain() #15
                  print('Sent {} results'.format(len(lines))) #16
              
              print('Close the client socket') #17
              writer.close() #18
              
      def main(address='127.0.0.1', port=2323): #1
          port = int(port)
          loop = asyncio.get_event_loop()
          server_coro = asyncio.start_server(handle_queries, address, port, loop=loop) #2
          server = loop.run_until_complete(server_coro) #3
          host = server.sockets[0].getsockname() #4
          print('Serving on {}. Hit CTRL-C to stop.'.format(host)) #5
          try:
              loop.run_forever() #6
          except KeyboardInterrupt: # 按CTRL-C键
              pass
          
          print('Server shutting down.')
          server.close() #7
          loop.run_until_complete(server.wait_closed()) #8
          loop.close() #9
      
      if __name__ == '__main__':
          main(*sys.argv[1:]) #10
      ```

   2. 使用aiohttp包编写Web服务器

      1. asyncio.start_server 函数和 loop.create_server 方法都是协程，返回的结果都是 asyncio.Server 对象

      2. 只有驱动协程，协程才能做事。而驱动 asyncio.coroutine 装饰的协程有两种方法：

         - 要么使用 yield from
         - 要么传给 asyncio 包中某个参数为协程或期物的函数，例如 run_until_complete

      3. 更好地支持并发的智能客户端

      4. http_charfinder.py

         ```python
         from aiohttp import web
         import asyncio, sys
         
         
         def home(request): #1
             query = request.GET.get('query', '').strip() # 2
             print('Query: {!r}'.format(query)) # 3
             if query: # 4
                 descriptions = list(index.find_descriptions(query))
                 res = '\n'.join(ROW_TPL.format(**vars(descr)) for descr in descriptions)
                 msg = index.status(query, len(descriptions))
             else:
                 descriptions = []
                 res = ''
                 msg = 'Enter words describing characters.'
                 
             html = template.format(query=query, result=res, message=msg) # 5
             
             print('Sending {} results'.format(len(descriptions))) # 6
             return web.Response(content_type=CONTENT_TYPE, text=html) # 7
         
         @asyncio.coroutine
         def init(loop, address, port): # 1
             app = web.Application(loop=loop) #2
             app.router.add_route('GET', '/', home) #3
             handler = app.make_handler() # 4
             server = yield from loop.create_server(handler, address, port) # 5
             return server.sockets[0].getsockname() # 6
         
         
         def main(address='127.0.0.1', port=8889):
             port = int(port)
             loop = asyncio.get_event_loop()
             host = loop.run_until_complete(init(loop, address, port)) # 7
             print('Serving on {}. Hit CTRL-C to stop.'.format(host))
             try:
                 loop.run_forever() # 8
             except KeyboardInterrupt: # 按CTRL-C键
                 pass
             print('Server shutting down.')
             loop.close() # 9
             
         
         if __name__ == '__main__':
             main(*sys.argv[1:])
         ```

8. 小结：

   1. 尽管有些函数必然会阻塞，但是为了让程序持续运行，有两种解决方案可用：
      - 使用多个线程
      - 异步调用——以回调或协程的形式实现
   2. 异步库依赖于低层线程（直至内核级线程），但是这些库的用户无需创建线程，也无需知道用到了基础设施中的低层线程
   3. 使用 loop.run_in_executor 方法把阻塞的作业（例如保存文件）委托给线程池做
   4. 使用协程解决回调的主要问题：执行分成多步的异步任务时丢失上下文，以及缺少处理错误所需的上下文
   5. 智能的HTTP客户端，例如单页Web应用或智能手机应用，需要快速、轻量级的响应和推送更新。鉴于这样的需求，服务器端最好使用异步框架，不要使用传统的Web框架（如Django）。传统框架的目的是渲染完整的HTML网页，而且不支持异步访问数据库。
   6. Python 和 Node. js 都有一个问题，而 Go 和 Erlang 从一开始就解决了这个问题：我们编写的代码无法轻松地利用所有可用的 CPU 核心。

## 19. 动态属性和特性

1. 引子
   1. property：特性，在不改变类接口的前提下，使用存取方法（即读值方法和设值方法）修改数据属性
   2. attribute：属性，在Python中，数据的属性和处理数据的方法统称属性。
   3. 使用点号访问属性时（如 obj.attr），Python 解释器会调用特殊的方法（如 `__getattr__` 和 `__setattr__`）计算属性
   4. 用户自己定义的类可以通过 `__getattr__` 方法实现“虚拟属性”，当访问不存在的属性时（如 obj.no_such_attribute），即时计算属性的值

2. 使用动态属性转换数据

   1. 使用动态属性访问JSON类数据

      ```python
      from collections import abc
      
      class FrozenJson:
          """一个只读接口，使用属性表示法访问JSON类对象"""
          
          def __init__(self, mapping):
              self.__data = dict(mapping) #1
              
          def __getattr__(self, name): #2
              if hasattr(self.__data, name):
                  return getattr(self.__data, name) #3
              else:
                  return FrozenJson.build(self.__data[name]) #4
          
          @classmethod
          def build(cls, obj): #5
              if isinstance(obj, abc.Mapping): #6
                  return cls(obj)
              elif isinstance(obj, abc.MutableSequence): #7
                  return [cls.build(item) for item in obj]
              else:
                  return obj
      ```

   2. 从随机源中生成或仿效动态属性名的脚本都必须处理一个问题：**原始数据中的键可能不适合作为属性名**

   3. 处理无效属性名

      ```python
      from collections import abc
      import keyword
      
      class FrozenJson:
          """一个只读接口，使用属性表示法访问JSON类对象"""
          
          def __init__(self, mapping):
              self.__data = {}
              for key, value in mapping.items():
                  if keyword.iskeyword(key):
                      key += '_'
                  self.__data[key] = value
              
          def __getattr__(self, name): #2
              if hasattr(self.__data, name):
                  return getattr(self.__data, name) #3
              else:
                  return FrozenJson.build(self.__data[name]) #4
          
          @classmethod
          def build(cls, obj): #5
              if isinstance(obj, abc.Mapping): #6
                  return cls(obj)
              elif isinstance(obj, abc.MutableSequence): #7
                  return [cls.build(item) for item in obj]
              else:
                  return obj
      ```

   4. 使用 `__new__` 方法以灵活的方式创建对象

      使用 `__new__` 方法取代 `build` 方法，构建可能是也可能不是 FrozenJSON 实例的新对象

      ```python
      from collections import abc
      
      class FrozenJSON:
          """一个只读接口，使用属性表示法访问JSON类对象"""
          
          def __new__(cls, arg): #1
              if isinstance(arg, abc.Mapping):
                  return super().__new__(cls) #2
              elif isinstance(arg, abc.MutableSequence): #3
                  return [cls(item) for item in arg]
              else:
                  return arg
              
          def __init__(self, mapping):
              self.__data = {}
              for key, value in mapping.items():
                  if keyword.iskeyword(key):
                      key += '_'
                  self.__data[key] = value
                  
          def __getattr__(self, name):
              if hasattr(self.__data, name):
                  return getattr(self.__data, name)
              else:
                  return FrozenJson(self.__data[name]) #4
      ```

   5. 使用shelve模块调整OSCON数据源的结构

      1. shelve.open 高阶函数返回一个 shelve.Shelf 实例，这是简单的键值对象数据库，背后由 dbm 模块支持，具有下述特点：

         - shelve.Shelf 是 abc.MutableMapping 的子类，因此提供了处理映射类型的重要方法
         - 此外，shelve.Shelf 类还提供了几个管理 I/O 的方法，如 sync 和 close；它也是一个上下文管理器
         - 只要把新值赋予键，就会保存键和值
         - 键必须是字符串
         - 值必须是 pickle 模块能处理的对象

      2. schedule1.py：访问保存在 shelve.Shelf 对象里的 OSCON 日程数据

         ```python
         import warnings
         
         DB_NAME = 'data/schedule1_db'
         CONFERENCE = 'conference.115'
         
         
         class Record:
             def __init__(self, **kwargs):
                 self.__dict__.update(kwargs) #2
                 
             
         def load_db(db):
             raw_data = load() #3
             warnings.warn('loading ' + DB_NAME)
             for collection, rec_list in raw_data['Schedule'].items(): #4
                 record_type = collection[:-1] #5
                 for record in rec_list:
                     key = '{}.{}'.format(record_type, record['serial']) #6
                     record['serial'] = key #7
                     db[key] = Record(**record) #8
         ```

         1. `Record.__init__` 方法展示了一个流行的 Python 技巧。我们知道，对象的 `__dict__` 属性中存储着对象的属性——前提是类中没有声明`__slots__` 属性	
         2. 因此，更新实例的 `__dict__` 属性，把值设为一个映射，能快速地在那个实例中创建一堆属性
      
   6. 使用特性获取链接的记录：schedule2.py
   
      ```python
      import warnings
      import inspect #1
      
      import osconfeed
      
      DB_NAME = 'data/schedule2_db' #2
      CONFERENCE = 'conference.115'
      
      
      class Record:
          def __init__(self, **kwargs):
              self.__dict__.update(kwargs)
              
          def __eq__(self, other): #3
              if isinstance(other, Record):
                  return self.__dict__ == other.__dict__
              else:
                  return NotImplemented
      
      class MissingDatabaseError(RuntimeError):
          """需要数据哭但没有制定数据库时抛出""" #1
          
      
      class DbRecord(Record): #2
          __db = None #3
          
          @staticmethod #4
          def set_db(db):
              DbRecord.__db = db #5
          
          @staticmethod #6
          def get_db():
              return DbRecordc.__db
          
          @classmethod #7
          def fetch(cls, ident):
              db = cls.get_db()
              try:
                  return db[ident] #8
              except TypeError:
                  if db is None: #9
                      msg = "database not set; call '{}.set_db(my_db)'"
                      raise MissingDatabaseError(msg.format(cls.__name__))
                  else: #10
                      raise
          
          def __repr__(self):
              if hasattr(self, 'serial'): #11
                  cls_name = self.__class__.__name__
                  return '<{} serial={!r}>'.format(cls_name, self.serial)
              else:
                  return super().__repr__() #12
              
      
      class Event(DbRecord): #1
          @property
          def venue(self):
              key = 'venue.{}'.format(self.venue_serial)
              return self.__class__.fetch(key) #2
          
          @property
          def speakers(self):
              if not hasattr(self, '_speaker_objs'): #3
                  spkr_serials = self.__dict__['speakers'] #4
                  fetch = self.__class__.fetch #5
                  self._speaker_objs = [fetch('speaker.{}'.format(key)) for key in spkr_serials] #6
                  
              return self._speaker_objs #7
          
          def __repr__(self):
              if hasattr(self, 'name'): #8
                  cls_name = self.__class__.__name__
                  return '<{} {!r}>'.format(cls_name, self.name)
              else:
                  return super().__repr__() #9
              
      def load_db(db):
          raw_data = osconfeed.load()
          warnings.warn('loading ' + DB_NAME)
          for collection, rec_list in raw_data['Schedule'].items():
              record_type = collection[:-1] #1
              cls_name = record_type.capitalize() #2
              cls = globals().get(cls_name, DbRecord) #3
              if inspect.isclass(cls) and issubclass(cls, DbRecord): #4
                  factory = cls #5
              else:
                  factory = DbRecord #6
              for record in rec_list: #7
                  key = '{}.{}'.format(record_type, record['serial'])
                  record['serial'] = key
                  db[key] = factory(**record) #8
      ```
   
3. 使用特性验证属性

   1. LineItem类第1版：表示订单中商品的类

      ```python
      class LineItem:
          def __init__(self, description, weight, price):
              self.description = description
              self.weight = weight
              self.price = price
              
          def subtotal(self):
              return self.weight * self.price
      ```

   2. LineItem类第2版：能验证值的特性

      ```python
      class LineItem:
          def __init__(self, description, weight, price):
              self.description = description
              self.weight = weight
              self.price = price
              
          def subtotal(self):
              return self.weight * self.price
          
          @property
          def weight(self):
              return self.__weight
          
          @weight.setter
          def weight(self, value):
              if value > 0:
                  self.__weight = value
              else:
                  raise ValueError('value must be > 0')
      ```

4. 特性全解析

   1. 特性会覆盖实例属性

      - 如果实例和所属的类有同名数据属性，那么实例属性会覆盖（或称遮盖）类属性——至少通过那个实例读取属性时是这样
      - **属性**：类变量（类属性）、成员变量（实例属性）（我的理解）
      - **特性**：用@property修饰的，特性是类属性（我的理解）
      - 同名变量会导致，成员变量覆盖类变量，特性覆盖属性
      - 删除特性后，类属性和实例属性，都会恢复
      - bj.attr 这样的表达式不会从 obj 开始寻找 attr，而是从 `obj.__class__` 开始，而且，仅当类中没有名为 attr 特性时，Python 才会在 obj 实例中寻找
      - **特性** 其实是 **覆盖型描述符**

   2. 特性的文档

      - 控制台中的 help() 函数或 IDE 等工具需要显示特性的文档时，会从特性的 `__doc__` 属性中提取信息

      - `weight = property(get_weight, set_weight, doc='weight in kilograms')`

        ```python
        class Foo:
            @property
            def bar(self):
                '''The bar attribute'''
                return self.__dict__['bar']
            
            @bar.setter
            def bar(self, value):
                self.__dict__['bar'] = value
        ```

5. 定义一个特性工厂函数

   1. bulkfood_v2prop.py

      ```python
      def quantity(storage_name): #1
          def qty_getter(instance): #2
              return instance.__dict__[storage_name] #3
          
          def qty_setter(instance, value): #4
              if value > 0:
                  instance.__dict__[storage_name] = value #5
              else:
                  raise ValueError('value must be > 0')
                  
          return property(qty_getter, qty_setter) #6
          
          
      class LineItem:
          weight = quantity('weight')
          price = quantity('price')
          
          def __init__(self, description, weight, price):
              self.description = description
              self.weight = weight
              self.price = price
              
          def subtotal(self):
              return self.weight * self.price
      ```

   2. 对 self.weight 或 nutmeg.weight 的每个引用都由特性函数处理

   3. 只有直接存取 `__dict__` 属性才能跳过特性的处理逻辑

6. 处理属性删除操作

   - 使用 Python 编程时不常删除属性，通过特性删除属性更少见

   - 对象的属性可以使用 del 语句删除

     ```python
     class BlackKnight:
         def __init__(self):
             self.members = ['an arm', 'another arm', 'a leg', 'another leg']
             self.phrases = ["'Tis but a scratch.'", "It's just a flesh wound.", "I'm invinvible!", "All right, we'll call it a draw."]
             
         @property
         def member(self):
             print('next member is:')
             return self.members[0]
         
         @member.deleter
         def member(self):
             text = 'BLACK KNIGHT (loses {})\n-- {}'
             print(text.format(self.members.pop(0), self.phrases.pop(0)))
     ```

7. 处理属性的重要属性和函数

   1. 影响属性处理方式的特殊属性

      - `__class__`：对象所属类的引用（即 `obj.__class__` 与 `type(obj)` 的作用相同）。Python 的某些特殊方法，例如 `__getattr__`，只在对象的类中寻找，而不在实例中寻找。

      - `__dict__`：一个映射，存储对象或类的可写属性。有 `__dict__` 属性的对象，任何时候都能随意设置新属性。如果类有 `__slots__` 属性，它的实例可能没有 `__dict__` 属性。

      - `__slots__`：类可以定义这个这属性，限制实例能有哪些属性。`__slots__` 属性的值是一个字符串组成的元组，指明允许有的属性。如果 `__slots__` 中没有 `'__dict__'`，那么该类的实例没有 `__dict__` 属性，实例只允许有指定名称的属性。

        `__slots__` 属性的值虽然可以是一个列表，但是最好始终使用元组，因为处理完类的定义体之后再修改 `__slots__` 列表没有任何作用，所以使用可变的序列容易让人误解

   2. 处理属性的内置函数

      - `dir([object])`：列出对象的大多数属性
        - dir 函数能审查有或没有 `__dict__` 属性的对象
        - dir 函数不会列出 `__dict__` 属性本身，但会列出其中的键
        - dir 函数也不会列出类的几个特殊属性，例如 `__mro__`、`__bases__` 和 `__name__`
      - `getattr(object, name[, default])`：从 object 对象中获取 name 字符串对应的属性
        - 获取的属性可能来自对象所属的类或超类
        - 如果没有指定的属性，getattr 函数抛出 AttributeError 异常，或者返回 default 参数的值
      - `hasattr(object, name)`：如果 object 对象中存在指定的属性，或者能以某种方式（例如继承）通过 object 对象获取指定的属性，返回 True
      - `setattr(object, name, value)`：把 object 对象指定属性的值设为 value，前提是 object 对象能接受那个值
        - 这个函数可能会创建一个新属性，或者覆盖现有的属性
      - `vars([object])`：返回 object 对象的 `__dict__` 属性
        - 如果实例所属的类定义了`__slots__` 属性，实例没有 `__dict__` 属性，那么 vars 函数不能处理那个实例
        - 如果没有指定参数，那么 vars() 函数的作用与 locals() 函数一样：返回表示本地作用域的字典
      
   3. 处理属性的特殊方法

      - 使用点号或内置的 getattr、hasattr 和 setattr 函数存取属性都会触发下述列表中相应的特殊方法

      - 但是，直接通过实例的 `__dict__` 属性读写属性不会触发这些特殊方法

      - 如果需要，通常会使用这种方式跳过特殊方法

      - 要假定特殊方法从类上获取，即便操作目标是实例也是如此。因此，特殊方法不会被同名实例属性遮盖

      - `__delattr__(self, name)`：只要使用 del 语句删除属性，就会调用这个方法

      - `__dir__(self)`：把对象传给 dir 函数时调用，列出属性

      - `__getattr__(self, name)`：仅当获取指定的属性失败，搜索过 obj、Class 和超类之后调用

      - `__getattribute__(self, name)`：尝试获取指定的属性时总会调用这个方法，不过，寻找的属性是特殊属性或特殊方法时除外

        为了在获取 obj 实例的属性时不导致无限递归，`__getattribute__` 方法的实现要使用 `super().__getattribute__(obj, name)`

      - `__setattr__(self, name, value)`：尝试设置指定的属性时总会调用这个方法，点号和 setattr 内置函数会触发这个方法

8. 总结：

   1. [详解Python中的`__init__`和`__new__`](https://zhuanlan.zhihu.com/p/58139772)
   2. 在 Python 中，很多情况下类和函数可以互换。这不仅是因为 Python 没有 new 运算符，还因为有特殊的 `__new__` 方法，可以把类变成工厂方法，生成不同类型的对象，或者返回事先构建好的实例，而不是每次都创建一个新实例
   3. UAP：统一访问原则，Unifrom Access Principle
   4. **new** 方法接受的参数虽然也是和 **init** 一样，但 **init** 是在类实例创建之后调用，而  **new** 方法正是创建这个类实例的方法

## 20. 属性描述符

1. 前言

   1. 描述符是对多个属性运用相同存取逻辑的一种方式
   2. 描述符是实现了特定协议的类，这个协议包括 `__get__`、`__set__` 和
      `__delete__` 方法
   3. 除了特性之外，使用描述符的 Python 功能还有方法及 classmethod 和 staticmethod 装饰器

2. 描述符示例：验证属性

   1. LineItem类第3版：一个简单的描述符

      1. 描述符的用法是，创建一个实例，作为另一个类的类属性

      2. 描述符类：实现描述符协议的类

      3. 托管类：把描述符实例声明为类属性的类

      4. 描述符实例：描述符类的各个实例，声明为托管类的类属性

      5. 托管实例：托管类的实例

      6. 储存属性：托管实例中存储自身托管属性的属性

      7. 托管属性：托管类中由描述符实例处理的公开属性，值存储在储存属性中。也就是说，描述符实例和储存属性为托管属性建立了基础

      8. 代码

         ```python
         class Quantity: #1
             def __init__(self, storage_name):
                 self.storage_name = storage_name #2
             
             def __set__(self, instance, value): #3
                 if value > 0:
                     instance.__dict__[self.storage_name] = value #4
                 else:
                     raise ValueError('value must be > 0')
                     
         
         class LineItem:
             weight = Quantity('weight') #5
             price = Quantity('price') #6
             
             def __init__(self, description, weight, price): #7
                 self.description = description
                 self.weight = weight
                 self.price = price
                 
             def subtotal(self):
                 return self.weight * self.price
         ```

   2. LineItem类第4版：自动获取储存属性的名称

      1. 这里可以使用内置的高阶函数 getattr 和 setattr 存取值，无需使用`instance.__dict__`，因为托管属性和储存属性的名称不同，所以把储存属性传给 getattr 函数不会触发描述符，不会像前面那样出现无限递归

         ```python
         class Quantity:
             __counter = 0 #1
             
             def __init__(self):
                 cls = self.__class__ #2
                 prefix = cls.__name__
                 index = cls.__counter
                 self.storage_name = '_{}#{}'.format(prefix, index) #3
                 cls.__counter += 1 #4
                 
             def __get__(self, instance, owner): #5
                 return getattr(instance, self.storage_name) #6
             
             def __set__(self, instance, value): #6
                 if value > 0:
                     setattr(instance, self.storage_name, value) #7
                 else:
                     raise ValueError('value must be > 0')
                     
         class LineItem:
             weight = Quantity() #9
             price = Quantity()
             
             def __init__(self, description, weight, price):
                 self.description = description
                 self.weight = weight
                 self.price = price
                 
             def subtotal(self):
                 return self.weight * self.price
         ```

      2. 为了给用户提供内省和其他元编程技术支持，通过类访问托管属性时，最好让 `__get__` 方法返回描述符实例

         ```python
         def __get__(self, instance, owner): #5
             if instance is None:
             	return self
             else:
             	return getattr(instance, self.storage_name) #6
         ```

      3. 描述符的常规用法：整洁的 LineItem 类；Quantity 描述符类现在位于导入的 model_v4c 模块中

         ```python
         import model_v4c as model
         
         
         class LineItem:
             weight = model.Quantity()
             price = model.Quantity()
             
             def __init__(self, description, weight, price):
                 self.description = description
                 self.weight = weight
                 self.price = price
                 
             def subtotal(self):
                 return self.weight * self.price
         ```

         1. Django 模型的字段就是描述符

      4. 使用特性工厂函数实现与上述示例中的描述符类相同的功能

         ```python
         def quantity(): #1
             try:
                 quantity.counter += 1 #2
             except AttributeError:
                 quantity.counter = 0 #3
             storage_name = '_{}:{}'.format('quntity', quantity.counter) #4
             
             def qty_getter(instance): #5
                 return getattr(instance, storage_name)
             
             def qty_setter(instance, value):
                 if value > 0:
                     setattr(instance, storage_name, value)
                 else:
                     raise ValueError('value must be > 0')
             
             return property(qty_getter, qty_setter)
         ```

         1. 不能依靠类属性在多次调用之间共享 counter，因此把它定义为 quantity 函数自身的属性
         2. 作者更喜欢描述符类的方式，因为：
            1. 描述符类可以使用子类扩展；若想重用工厂函数中的代码，除了复制粘贴，很难有其他方法
            2. 与使用函数属性和闭包保持状态相比，在类属性和实例属性中保持状态更易于理解
         3. 从某种程度上来讲，特性工厂函数模式较简单，可是描述符类方式更易扩展，而且应用也更广泛

   3. LineItem类第5版：一种新型描述符















看到 P904

