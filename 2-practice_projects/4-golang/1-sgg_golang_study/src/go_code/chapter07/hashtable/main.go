package main

import "fmt"

type Emp struct {
	Id   int
	Name string
	Next *Emp
}

func (this *Emp) showMe() {
	fmt.Printf("链表%d 找到该雇员 %d-%s\n", this.Id%7, this.Id, this.Name)
}

// 不带表头，即第一个节点就存放雇员
type EmpLink struct {
	Head *Emp
}

// 添加员工的方法，保证添加时，编号从小到大
func (this *EmpLink) Insert(emp *Emp) {
	// 创建一个辅助指针
	cur := this.Head
	// pre 始终在cur前面
	var pre *Emp = nil
	// 如果当前就是空链表
	if cur == nil {
		this.Head = emp
		return
	}
	// 如果不是空链表，给emp找到对应的位置，并插入
	for {
		if cur != nil && cur.Id < emp.Id {
			pre = cur
			cur = cur.Next
		} else {
			// 找到位置了
			break
		}
	}
	// 把emp加在pre的后面
	emp.Next = cur
	pre.Next = emp
}

// 显示
func (this *EmpLink) ShowLink(no int) {
	if this.Head == nil {
		fmt.Printf("链表%d 为空\n", no)
		return
	}
	cur := this.Head
	fmt.Printf("链表%d ", no)
	for {
		fmt.Printf("雇员%d 名字为：%s => ", cur.Id, cur.Name)
		cur = cur.Next
		if cur == nil {
			break
		}
	}
	fmt.Println("")
}

// 根据id查找对应的员工
func (this *EmpLink) FindById(id int) *Emp {
	cur := this.Head
	for {
		if cur != nil && cur.Id == id {
			return cur
		} else if cur == nil {
			break
		}
		cur = cur.Next
	}
	return nil
}

// 定义hashtable，含有一个链表数组
type HashTable struct {
	LinkArr [7]EmpLink
}

// 编写Insert方法
func (this *HashTable) Insert(emp *Emp) {
	// 1.根据员工的id，得到员工应该被存放的链表在LinkArr中的位置
	index := this.GetIndex(emp.Id)
	this.LinkArr[index].Insert(emp)
}

// 显示hashtable所有的链表
func (this *HashTable) ShowAll() {
	for i := 0; i < len(this.LinkArr); i++ {
		this.LinkArr[i].ShowLink(i)
	}
}

// 编写用于散列的函数
func (this *HashTable) GetIndex(id int) int {
	return id % 7
}

// 完成查找的方法
func (this *HashTable) FindEmpById(id int) *Emp {
	// 1.根据员工id，得到员工应该被存放的链表在LinkArr中的位置
	index := this.GetIndex(id)
	// 2.根据index在LinkArr中，得到对应的链表
	return this.LinkArr[index].FindById(id)
}

func main() {
	var hashTable HashTable
	emp1 := Emp{1, "张三", nil}
	emp2 := Emp{8, "李四", nil}
	emp3 := Emp{1230, "王五", nil}
	emp4 := Emp{22, "赵六", nil}
	emp5 := Emp{15, "田七", nil}
	hashTable.Insert(&emp1)
	hashTable.Insert(&emp2)
	hashTable.Insert(&emp3)
	hashTable.Insert(&emp4)
	hashTable.Insert(&emp5)
	hashTable.ShowAll()

	emp := hashTable.FindEmpById(22)
	if emp != nil {
		emp.showMe()
	} else {
		fmt.Println("没有找到该员工")
	}
}
