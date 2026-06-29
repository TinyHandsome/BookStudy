package main

type HeroNode struct {
	no       int
	name     string
	nickname string
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
}

func main() {
	// 创建头结点
	head := &HeroNode{}
	// 创建新的HeroNode
	hero1 := &HeroNode{1, "宋江", "及时雨", nil}
}
