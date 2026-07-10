package main

import (
	"errors"
	"strconv"
)

type Stack struct {
	MaxTop int
	Top    int
	Array  [20]int
}

func (this *Stack) Push(val int) (err error) {
	// 先判断栈是否满了
	if this.Top == this.MaxTop-1 {
		return errors.New("栈已满")
	}
	this.Top++
	// 放入数据
	this.Array[this.Top] = val
	return
}

func (this *Stack) Pop() (val int, err error) {
	// 先判断栈是否为空
	if this.Top == -1 {
		return 0, errors.New("栈为空")
	}
	val = this.Array[this.Top]
	this.Top--
	return
}

func (this *Stack) List() {
	if this.Top == -1 {
		println("栈为空")
		return
	}
	for i := this.Top; i >= 0; i-- {
		println(this.Array[i])
	}
}

// 判断一个字符是否是运算符
func (this *Stack) IsOper(val int) bool {
	return val == 42 || val == 43 || val == 45 || val == 47
}

// 运算的方法
func (this *Stack) Cal(num1 int, num2 int, oper int) (res int) {
	switch oper {
	case 43:
		res = num1 + num2
	case 45:
		res = num2 - num1
	case 42:
		res = num1 * num2
	case 47:
		res = num2 / num1
	default:
		panic("运算符有误")
	}
	return res
}

// 返回运算符的优先级
func (this *Stack) Priority(oper int) int {
	switch oper {
	case 42, 47:
		return 1
	case 43, 45:
		return 0
	default:
		return -1
	}
}
func main() {
	// 数栈
	numStak := &Stack{MaxTop: 20, Top: -1}
	// 符号栈
	operStack := &Stack{MaxTop: 20, Top: -1}

	exp := "302+2*8-2"
	index := 0
	num1 := 0
	num2 := 0
	oper := 0
	result := 0
	keepNum := ""

	for {
		ch := exp[index : index+1]
		// 将字符转为 ASCII码
		temp := int([]byte(ch)[0])
		if operStack.IsOper(temp) {
			if operStack.Top == -1 {
				operStack.Push(temp)
			} else {
				if operStack.Priority(operStack.Array[operStack.Top]) >= operStack.Priority(temp) {
					// 如果栈顶的运算符优先级大于等于当前运算符，pop两个数和一个操作符
					num1, _ = numStak.Pop()
					num2, _ = numStak.Pop()
					oper, _ = operStack.Pop()
					result = operStack.Cal(num1, num2, oper)
					// 将计算结果重新入数栈
					numStak.Push(result)
					operStack.Push(temp)
				} else {
					operStack.Push(temp)
				}
			}
		} else {
			// 说明是数字
			// 处理多位数的思路
			// 1. 定义变量做拼接工作
			keepNum += ch
			// 2. 多往前探一位，判断当前字符是不是数字

			if index == len(exp)-1 {
				val, _ := strconv.ParseInt(keepNum, 10, 64)
				numStak.Push(int(val))
			} else {
				// 探索 index + 1
				if operStack.IsOper(int([]byte(exp[index+1 : index+2])[0])) {
					val, _ := strconv.ParseInt(keepNum, 10, 64)
					numStak.Push(int(val))
					keepNum = ""
				}
			}
		}
		// 先判断index是否已经扫描到计算表达式的最后
		if index+1 == len(exp) {
			break
		}
		index++
	}

	// 把两个栈里面的东西拿出来算
	for {
		if operStack.Top == -1 {
			break
		}
		num1, _ = numStak.Pop()
		num2, _ = numStak.Pop()
		oper, _ = operStack.Pop()
		result = operStack.Cal(num1, num2, oper)
		numStak.Push(result)
	}

	res, _ := numStak.Pop()
	println(exp, "的结果为：", res)
}
