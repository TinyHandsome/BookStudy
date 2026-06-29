package main

import (
	"errors"
	"fmt"
)

type CircleQueue struct {
	maxSize int
	array   [5]int
	head    int
	tail    int
}

// 入队
func (this *CircleQueue) Push(val int) (err error) {
	if this.IsFull() {
		fmt.Println("队列已满")
		return errors.New("队列已满")
	}

	this.array[this.tail] = val
	this.tail = (this.tail + 1) % this.maxSize
	return
}

// 出队
func (this *CircleQueue) Pop() (val int, err error) {
	if this.IsEmpty() {
		fmt.Println("队列为空")
		return -1, errors.New("队列为空")
	}
	// 取出
	val = this.array[this.head]
	this.head = (this.head + 1) % this.maxSize
	return
}

// 显示队列
func (this *CircleQueue) ListQueue() {
	if this.IsEmpty() {
		fmt.Println("队列为空")
		return
	}
	fmt.Println("队列的情况如下：")
	tempHead := this.head
	for i := 0; i < this.Size(); i++ {
		fmt.Printf("arr[%d]=%d\n", tempHead, this.array[tempHead])
		tempHead = (tempHead + 1) % this.maxSize
	}
}

// 判断环形队列为空
func (this *CircleQueue) IsFull() bool {
	return (this.tail+1)%this.maxSize == this.head
}

// 判断环形列表是否满
func (this *CircleQueue) IsEmpty() bool {
	return this.tail == this.head
}

// 取出环形队列有多少个元素
func (this *CircleQueue) Size() int {
	return (this.tail + this.maxSize - this.head) % this.maxSize
}

func main() {
	queue := &CircleQueue{maxSize: 5, head: 0, tail: 0}
	for i := 0; i < 5; i++ {
		err := queue.Push(i)
		if err != nil {
			fmt.Println(err.Error())
			break
		}
	}
	queue.ListQueue()

	for i := 0; i < 5; i++ {
		val, err := queue.Pop()
		if err != nil {
			fmt.Println(err.Error())
			break
		}
		fmt.Println("取出的元素是：", val)
	}
}
