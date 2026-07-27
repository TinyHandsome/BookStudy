package main

import "fmt"

type Hero struct {
	No    int
	Name  string
	Left  *Hero
	Right *Hero
}

// 前序遍历 根左右
func PreOrder(node *Hero) {
	if node != nil {
		fmt.Printf("no=%d name=%s\n", node.No, node.Name)
		PreOrder(node.Left)
		PreOrder(node.Right)
	}
}

// 中序遍历 左根右
func InfixOrder(node *Hero) {
	if node != nil {
		InfixOrder(node.Left)
		fmt.Printf("no=%d name=%s\n", node.No, node.Name)
		InfixOrder(node.Right)
	}
}

// 后序遍历 左右根
func PostOrder(node *Hero) {
	if node != nil {
		PostOrder(node.Left)
		PostOrder(node.Right)
		fmt.Printf("no=%d name=%s\n", node.No, node.Name)
	}
}

func main() {
	root := &Hero{No: 1, Name: "张三"}
	left1 := &Hero{No: 2, Name: "李四"}
	right1 := &Hero{No: 3, Name: "王五"}

	node10 := &Hero{No: 10, Name: "小张"}
	node12 := &Hero{No: 12, Name: "小王"}
	left1.Left = node10
	left1.Right = node12

	root.Left = left1
	root.Right = right1

	right2 := &Hero{No: 4, Name: "赵六"}
	right1.Right = right2
	// PreOrder(root)
	// InfixOrder(root)
	PostOrder(root)
}
