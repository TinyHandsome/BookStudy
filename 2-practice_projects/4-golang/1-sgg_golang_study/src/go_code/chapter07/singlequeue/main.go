package main

import (
	"errors"
	"fmt"
)

type Queue struct {
	maxSize int
	array   [5]int
	front   int // 不含队首
	rear    int // 含队尾
}

// 添加队列
func (this *Queue) addQueue(val int) (err error) {
	// 先判断队列是否已满
	if this.rear == this.maxSize-1 {
		// 含最后一个元素
		return errors.New("队列已满")
	}

	this.rear++
	this.array[this.rear] = val
	return
}

// 显示队列
func (this *Queue) showQueue() {
	if this.front == this.rear {
		fmt.Println("队列为空")
		return
	}

	for i := this.front + 1; i <= this.rear; i++ {
		fmt.Printf("arr[%d]=%d\n", i, this.array[i])
	}
}

// 取出数据
func (this *Queue) getQueue() (val int, err error) {
	if this.front == this.rear {
		return -1, errors.New("队列为空")
	}

	this.front++
	val = this.array[this.front]
	return val, nil
}

func main() {
	queue := &Queue{maxSize: 5, front: -1, rear: -1}
	for i := 0; i < 5; i++ {
		err := queue.addQueue(i)
		if err != nil {
			fmt.Println(err.Error())
			break
		}
	}
	queue.showQueue()
	err := queue.addQueue(6)
	if err != nil {
		fmt.Println(err.Error())
	}

	for i := 0; i < 5; i++ {
		val, err := queue.getQueue()
		if err != nil {
			fmt.Println(err.Error())
			break
		}
		fmt.Println("取出的元素是：", val)
	}
	val, err := queue.getQueue()
	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Println("取出的元素是：", val)
	}

}
