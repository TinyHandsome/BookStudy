package main

import "fmt"

type Customer struct {
	Id     int
	Name   string
	Gender string
	Age    int
	Phone  string
	Email  string
}

func (this *Customer) GetInfo() string {
	info := fmt.Sprintf("%d\t%s\t%s\t%d\t%s\t%s",
		this.Id, this.Name, this.Gender, this.Age, this.Phone, this.Email)
	return info
}

func NewCustomer(id int, name string, gender string, age int, phone string, email string) *Customer {
	return &Customer{id, name, gender, age, phone, email}
}

type CustomerService struct {
	customers   []*Customer
	customerNum int
}

func NewCustomerService() *CustomerService {
	cs := &CustomerService{}
	cs.customerNum = 1
	customer := NewCustomer(1, "张三", "男", 20, "12345678901", "zhangsan@qq.com")
	cs.customers = append(cs.customers, customer)
	return cs
}

func (this *CustomerService) List() []*Customer {
	return this.customers
}

func (this *CustomerService) Add(customer *Customer) bool {
	this.customerNum++
	customer.Id = this.customerNum
	this.customers = append(this.customers, customer)
	return true
}

func (this *CustomerService) Delete(id int) bool {
	index := -1
	for i := 0; i < len(this.customers); i++ {
		if this.customers[i].Id == id {
			index = i
			break
		}
	}
	if index == -1 {
		return false
	}
	this.customers = append(this.customers[:index], this.customers[index+1:]...)
	return true
}

func (this *CustomerService) Update(id int, customer *Customer) bool {
	index := -1
	for i := 0; i < len(this.customers); i++ {
		if this.customers[i].Id == id {
			index = i
			break
		}
	}
	if index == -1 {
		return false
	}
	this.customers[index] = customer
	return true
}

type CustomerView struct {
	key     string // 接受用户输入
	loop    bool   // 表示是否循环的显示主菜单
	service *CustomerService
}

func (this *CustomerView) list() {
	customers := this.service.List()
	fmt.Println("-----------------客户列表----------------")
	fmt.Println("编号\t姓名\t性别\t年龄\t电话\t邮箱")
	for i := 0; i < len(customers); i++ {
		fmt.Println(customers[i].GetInfo())
	}
	fmt.Println("-----------------客户列表完成------------\n")
}

func (this *CustomerView) add() {
	fmt.Println("-----------------添加客户----------------")
	fmt.Println("姓名：")
	name := ""
	fmt.Scanln(&name)
	fmt.Println("性别：")
	gender := ""
	fmt.Scanln(&gender)
	fmt.Println("年龄：")
	age := 0
	fmt.Scanln(&age)
	fmt.Println("电话：")
	phone := ""
	fmt.Scanln(&phone)
	fmt.Println("邮箱：")
	email := ""
	fmt.Scanln(&email)

	customer := NewCustomer(-1, name, gender, age, phone, email)
	this.service.Add(customer)
}

func (this *CustomerView) delete() {
	fmt.Println("-----------------删除客户----------------")
	fmt.Println("请选择待删除客户编号(-1退出)：")
	id := -1
	fmt.Scanln(&id)
	if id == -1 {
		return
	}
	fmt.Println("是否确定删除？y/n")
	choice := ""
	fmt.Scanln(&choice)
	if choice == "y" || choice == "Y" {
		if this.service.Delete(id) {
			fmt.Println("删除成功！")
		} else {
			fmt.Println("删除失败！")
		}
	}
}

func (this *CustomerView) exit() {
	fmt.Println("确认是否退出（y/n）")
	for {
		choice := ""
		fmt.Scanln(&choice)
		if choice == "y" || choice == "Y" {
			this.loop = false
			break
		} else if choice == "n" || choice == "N" {
			break
		} else {
			fmt.Println("请输入正确的选项！")
		}
	}
}

func (this *CustomerView) update() {
	fmt.Println("-----------------修改客户----------------")
	fmt.Println("请选择待修改客户编号(-1退出)：")
}

func (this *CustomerView) mainMenu() {
	for {
		fmt.Println("----------客户信息管理软件----------")
		fmt.Println("          1. 添 加 客 户")
		fmt.Println("          2. 修 改 客 户")
		fmt.Println("          3. 删 除 客 户")
		fmt.Println("          4. 客 户 列 表")
		fmt.Println("          5. 退       出")

		fmt.Scanln(&this.key)
		switch this.key {
		case "1":
			this.add()
		case "2":
			fmt.Println("修改客户")
		case "3":
			this.delete()
		case "4":
			this.list()
		case "5":
			this.exit()
		default:
			fmt.Println("请输入正确的选项！")
		}

		if !this.loop {
			break
		}
	}

	fmt.Println("你退出了客户管理系统")
}

func main() {
	customerView := CustomerView{
		key:  "",
		loop: true,
	}
	customerView.service = NewCustomerService()
	customerView.mainMenu()
}
