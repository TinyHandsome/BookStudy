package main

import "fmt"

type CatNode struct {
	no   int
	name string
	next *CatNode
}

func InsertCatNode(head *CatNode, newCatNode *CatNode) {
	// 判断是不是添加第一只猫
	if head.next == nil {
		head.no = newCatNode.no
		head.name = newCatNode.name
		head.next = head
		fmt.Println(newCatNode, "加入到环形的链表中。。。")
		return
	}

	// 定义一个临时的变量，帮忙找到环形的最后节点
	temp := head
	for {
		if temp.next == head {
			break
		}
		temp = temp.next
	}
	temp.next = newCatNode
	newCatNode.next = head
}

// 输出环形链表
func ListCatNode(head *CatNode) {
	if head.next == nil {
		fmt.Println("链表为空。。。")
		return
	}
	temp := head
	for {
		fmt.Printf("猫的编号：%d, 猫的名字：%s\n", temp.no, temp.name)
		if temp.next == head {
			break
		}
		temp = temp.next
	}
}

// 删除
func DeleteCatNode(head *CatNode, no int) *CatNode {
	temp := head
	helper := head
	if temp.next == nil {
		fmt.Println("链表为空。。。")
		return head
	}
	// 如果只有一个节点
	if temp.next == temp {
		if temp.no == no {
			temp.next = nil
			fmt.Println(temp, "被删除了。。。")
		} else {
			fmt.Println("没有找到该节点。。。")
		}
		return head
	}

	// 将helper定位到链表最后
	for {
		if helper.next == head {
			break
		}
		helper = helper.next
	}

	flag := true
	// 如果不只有一个节点
	for {
		// 已经到最后一个了，都还没找到，说明没有这个节点
		if temp.next == head {
			break
		}
		// 找到了
		if temp.no == no {
			// 如果删除的是头结点
			if temp == head {
				head = head.next
			}

			// 前一个指针的next指向，要删除的节点的next
			helper.next = temp.next
			fmt.Println(temp, "被删除了。。。")
			flag = false
			break
		}
		temp = temp.next
		helper = helper.next
	}
	// 最后还要比较一次
	if flag {
		if temp.no == no {
			helper.next = temp.next
			fmt.Println(temp, "被删除了。。。")
		} else {
			fmt.Println("没有找到该节点。。。")
		}
	}
	return head
}

func main() {
	// 初始化头结点
	head := &CatNode{}
	// 创建一只猫
	cat1 := &CatNode{1, "小花", nil}
	cat2 := &CatNode{2, "小黑", nil}
	cat3 := &CatNode{3, "小黄", nil}
	InsertCatNode(head, cat1)
	InsertCatNode(head, cat2)
	InsertCatNode(head, cat3)
	ListCatNode(head)
}
