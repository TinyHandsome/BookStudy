package main

import (
	"errors"
	"fmt"
)

type Stack struct {
	MaxTop int
	Top    int
	Array  [5]int
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

func main() {
	stack := &Stack{MaxTop: 5, Top: -1}
	for i := 0; i < 6; i++ {
		err := stack.Push(i)
		if err != nil {
			println(i, "入栈失败", err.Error())
		} else {
			println(i, "入栈成功")
		}
	}
	stack.List()
	val, _ := stack.Pop()
	fmt.Println("出栈", val)
	stack.List()
}
