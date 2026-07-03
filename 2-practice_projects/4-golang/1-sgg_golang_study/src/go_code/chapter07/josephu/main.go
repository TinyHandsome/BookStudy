package main

import "fmt"

// 小孩的结构体
type Boy struct {
	No   int
	Next *Boy
}

// 小孩的个数，返回环形链表小孩的第一个指针
func AddBoy(num int) *Boy {
	first := &Boy{}
	curBoy := &Boy{}
	if num < 1 {
		fmt.Println("num的值不正确。。。")
		return first
	}
	// 循环的构建这个环形链表
	for i := 1; i <= num; i++ {
		boy := &Boy{No: i}
		// 因为第一个小孩比较特殊
		if i == 1 {
			first = boy
			curBoy = boy
			curBoy.Next = first
		} else {
			curBoy.Next = boy
			curBoy = boy
			curBoy.Next = first
		}
	}
	return first
}

// 显示单向的环形链表
func ShowBoy(first *Boy) {
	if first.Next == nil {
		fmt.Println("链表为空。。。")
		return
	}
	curBoy := first
	for {
		fmt.Printf("小孩的编号%d\n", curBoy.No)
		if curBoy.Next == first {
			break
		}
		curBoy = curBoy.Next
	}
}

func PlayGame(first *Boy, startNo int, countNum int) *Boy {
	if first.Next == nil {
		fmt.Println("链表为空。。。")
		return first
	}
	tail := first
	for {
		if tail.Next == first {
			break
		}
		tail = tail.Next
	}
	// 移动到startNo去，即移动startNo -1 次
	for i := 0; i < startNo-1; i++ {
		first = first.Next
		tail = tail.Next
	}
	// 继续移动countNum下，然后删除first指向的小孩
	for {
		// 判断 如果tail == first，则说明只剩一个小孩啦
		if tail == first {
			break
		}
		// 开始数 countNum - 1次
		for i := 0; i < countNum-1; i++ {
			first = first.Next
			tail = tail.Next
		}
		fmt.Printf("小孩%d出列。。。\n", first.No)
		first = first.Next
		tail.Next = first
	}
	fmt.Printf("最后出圈的小孩为：%d \n", first.No)
	return first
}

func main() {
	first := AddBoy(50)
	ShowBoy(first)
	PlayGame(first, 20, 31)
}
