package main

import "fmt"

type HeroNode struct {
	no       int
	name     string
	nickname string
	pre      *HeroNode
	next     *HeroNode
}

// 给链表插入节点，尾插法
func InsertHeroNode(head *HeroNode, newHeroNode *HeroNode) {
	temp := head

	for {
		if temp.next == nil {
			// 找到最后啦
			break
		}
		temp = temp.next
	}
	// 将新node加入到链表的最后
	temp.next = newHeroNode
	newHeroNode.pre = temp
}

// 根据no的编号从小到大插入
func InsertHeroNode2(head *HeroNode, newHeroNode *HeroNode) {
	temp := head
	for {
		if temp.next == nil {
			// 找到最后啦
			break
		} else if temp.next.no >= newHeroNode.no {
			// 找到位置了
			break
		}
		temp = temp.next
	}
	newHeroNode.next = temp.next
	newHeroNode.pre = temp
	// 如果插入的节点是最后一个，则可以指向temp.next即nil，但是没有指向自己的
	if temp.next != nil {
		temp.next.pre = newHeroNode
	}
	temp.next = newHeroNode
}

// 删除一个节点
func DeleteHeroNode(head *HeroNode, no int) {
	temp := head

	flag := false
	for {
		if temp.next == nil {
			// 找到最后啦
			break
		} else if temp.next.no == no {
			// 找到位置了
			flag = true
			break
		}
		temp = temp.next
	}

	if flag {
		temp.next = temp.next.next
		// 记住，这里的temp.next已经换成了之前的temp.next.next
		if temp.next != nil {
			temp.next.pre = temp
		}
	} else {
		fmt.Println("没有找到该节点")
	}
}

// 显示链表所有的节点信息
func ListHeroNode(head *HeroNode) {
	if head.next == nil {
		fmt.Println("链表为空")
		return
	}
	// 创建一个辅助变量
	temp := head.next
	for {
		fmt.Printf("HeroNode[%d, %s, %s]\n", temp.no, temp.name, temp.nickname)
		temp = temp.next
		if temp == nil {
			break
		}
	}
}
func ListHeroNode2(head *HeroNode) {
	if head.next == nil {
		fmt.Println("链表为空")
		return
	}
	// 创建一个辅助变量
	temp := head.next
	// 找到最后一个节点
	for {
		// 如果当前为最后一个节点，则退出
		if temp.next == nil {
			break
		}
		temp = temp.next
	}

	for {
		fmt.Printf("HeroNode[%d, %s, %s]\n", temp.no, temp.name, temp.nickname)
		temp = temp.pre
		// 判断是否是列表头，找到head就退出
		if temp.pre == nil {
			break
		}
	}
}

func main() {
	// 创建头结点
	head := &HeroNode{}
	// 创建新的HeroNode
	hero1 := &HeroNode{1, "宋江", "及时雨", nil, nil}
	hero2 := &HeroNode{2, "卢俊义", "玉麒麟", nil, nil}
	hero3 := &HeroNode{3, "林冲", "豹子头", nil, nil}
	InsertHeroNode(head, hero1)
	InsertHeroNode(head, hero3)
	InsertHeroNode(head, hero2)
	ListHeroNode(head)
	ListHeroNode2(head)
}
