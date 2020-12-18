# leetcode刷题笔记

[TOC]

## 写在前面

leetcode连接：https://leetcode-cn.com/problemset/all/

刷题顺序：从简单->中等->困难

- [简单题库](https://leetcode-cn.com/problemset/all/?difficulty=%E7%AE%80%E5%8D%95)

解题思路：做一个自己的答案，再参考评论中的思路，自己编写更加高效的代码（下面给出两个百分数，分别代表**执行用时**和**内存消耗**击败了%多少的用户）

## [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            one = nums[i]
            two = target - one
            if two in nums:
                two_index = nums.index(two)
                if two_index != i:
                    return [i, two_index]
                else:
                    continue
            else:
                continue
```

## [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)

```python
class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)[::-1].strip('-')
        if int(temp) < 2 ** 31:
            if x > 0:
                return int(temp)
            else:
                return (-1)*int(temp)
        else:
            return 0
```

62.53	82.53

## [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp = str(x)
            l = len(temp)
            for i in range(int(l/2)):
                if temp[i] == temp[l-1-i]:
                    continue
                else:
                    return False
            return True
```

99.38	26.19	我觉得还ok

> 大佬一句话给我整哭了
>
> 方法：转字符串啊。。。

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```

## [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        for i in range(len(str[::-1])):
            未完待续...
```







## [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        length = len(strs[0])
        
        for x in strs[1:]:
            if len(x) < length:
                length = len(x)
        if length == 0:
            return ""
        
        temp = ""       
        for i in range(length):
            for j in range(1, len(strs)):
                if strs[j-1][0:i+1] == strs[j][0:i+1]:
                    continue
                else:
                    return temp
            temp = temp + strs[0][i]
        return temp
```

21.22	5.53	我哭了

> 方法：利用好zip和set
>
> ![img](https://img-blog.csdnimg.cn/20190718221501874.png)

参考文献：[python中zip()与zip(*)的用法解析](https://blog.csdn.net/ezio23/article/details/81414092)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 最后加一个0就可以包含字符创一毛一样问题，即没有False
        temp = [len(set(x)) == 1 for x in zip(*strs)] + [0]
        if strs:
            index = temp.index(False)
            return strs[0][:index]            
        else:
            return ""
```

98.52	45.90	抄大佬作业太可怕了。。。

## [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        one = ['(', '[', '{']
        two = [')', ']', '}']
        kuohao = []
        if len(s) == 0:
            return True
        elif s[0] in two or len(s)%2 == 1:
            return False
        else:
            for x in s:
                if x in one:
                    kuohao.append(x)
                else:
                    index = two.index(x)
                    if kuohao.pop() == one[index]:
                        continue
                    else:
                        return False
            if len(kuohao) == 0:
                return True
            else:
                return False
```

31.05	83.11	我哭了

> 方法：栈
>
> ![img](https://img-blog.csdnimg.cn/20190718215031607.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        one = ['(', '[', '{']
        two = [')', ']', '}']
        mapping = dict(zip(one, two))
        stack = []
        for i in s:
            if len(stack) == 0 or i in one:
                stack.append(i)
            elif (stack[-1] in one) and (mapping[stack[-1]] == i):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
```

99.96	5.51	我很快乐

## [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = list(set(nums))
        x.sort(key=nums.index)
        nums[:len(x)] = x
        return len(x)
```

5.01	19.67	我哭了

> 方法：双指针法
>
> ![img](https://img-blog.csdnimg.cn/20190718213525809.png)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
```

修改后	96.39	8.35	快乐！

## [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:   
        if val not in nums:
            return len(nums)
        i = nums.index(val)
        for j in range(i+1, len(nums)):
            if nums[j] == val:
                continue
            else:
                nums[i] = nums[j]
                i += 1
        return i
```

85.85	8.97	快乐

天啦，我基本上就是官方答案了，还参考个锤子

## [28. 实现strStr()](https://leetcode-cn.com/problems/implement-strstr/)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
```

哇！我一行解决了，我是真的强！	84.72	84.98

第二种解法，find

`return haystack.find(needle)`

第三种解法：实打实搞起

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            try:
                temp = haystack[i:i + len(needle)]
                if temp == needle:
                    return i
                else:
                    continue
            except Exception:
                return -1
        return -1
```

速度慢了好多

## [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        for i in range(len(nums)-1):
            if nums[i] <= target <= nums[i+1]:
                if target == nums[i]:
                    return i
                elif target == nums[i+1]:
                    return i+1
                else:
                    return i+1
        return len(nums)
```

5.49	5.47	鬼知道我经历了什么

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            start = 0
            end = len(nums)
            mid = (start + end) // 2
            while True:
                if end - start == 1:
                    return end
                if target > nums[mid]:
                    start = mid
                    mid = (start + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2
```

17.39	5.47	二分法我也哭了

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        left = 0
        # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度
        right = size
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                # [1,5,7] 2
                right = mid
        # 调试语句
        # print('left = {}, right = {}, mid = {}'.format(left, right, mid))
        return left
```

参考二分法

## [38. 报数](https://leetcode-cn.com/problems/count-and-say/)

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def g(x):
            keys = [x[0]]
            count = [1]
            j = 0
            for i in range(1, len(list(x))):
                if x[i] == keys[j]:
                    count[j] += 1
                else:
                    keys.append(x[i])
                    count.append(1)
                    j += 1
            ss = ""
            for k in range(len(keys)):
                ss = ss + str(count[k]) + keys[k]
            return ss
        
        
        def f(o):
            if o == 1:
                return "1"
            else:
                return g(f(o-1))
                
        
        return f(n)
```

20.43	5.00	递归拯救我哈哈哈

> 一句话解释: 不断由前一个数推下一个数。

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        def next_num(tmp):
            res = ""
            i = 0
            tmp_n = len(tmp)
            while i < tmp_n:
                count = 1
                while i < tmp_n - 1 and tmp[i] == tmp[i+1]:
                    count += 1
                    i += 1
                res += (str(count) + tmp[i])
                i += 1
            return res
        res = "1"
        for i in range(1, n):
            res = next_num(res)
        return res
```

