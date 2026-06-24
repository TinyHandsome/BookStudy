package main

import (
	"demo/chatroom/client/process"
	"fmt"
	"os"
)

var userId int
var userPwd string
var userName string

func main() {
	var key int
	var loop = true

	for loop {
		fmt.Println("----------欢迎来到多人聊天室----------")
		fmt.Println("\t\t1. 登录聊天室")
		fmt.Println("\t\t2. 注册用户")
		fmt.Println("\t\t3. 退出系统")
		fmt.Println("请选择(1-3):")

		fmt.Scanf("%d\n", &key)
		switch key {
		case 1:
			fmt.Println("登录聊天室")
			fmt.Println("请输入用户ID：")
			fmt.Scanf("%d\n", &userId)
			fmt.Println("请输入用户密码：")
			fmt.Scanf("%s\n", &userPwd)
			// 完成登录
			up := &process.UserProcess{}
			up.Login(userId, userPwd)
		case 2:
			fmt.Println("注册用户")
			fmt.Println("请输入用户ID：")
			fmt.Scanf("%d\n", &userId)
			fmt.Println("请输入用户密码：")
			fmt.Scanf("%s\n", &userPwd)
			fmt.Println("请输入用户名称：")
			fmt.Scanf("%s\n", &userName)

			up := &process.UserProcess{}
			up.Register(userId, userName, userPwd)
		case 3:
			fmt.Println("退出系统")
			os.Exit(0)
		default:
			fmt.Println("请输入正确的选项！")
		}
	}

	// switch key {
	// case 1:
	// 	fmt.Println("请输入用户ID：")
	// 	fmt.Scanf("%d\n", &userId)
	// 	fmt.Println("请输入用户密码：")
	// 	fmt.Scanf("%s\n", &userPwd)

	// 	// login(userId, userPwd)
	// 	// if err != nil {
	// 	// 	fmt.Println("登录失败！")
	// 	// } else {
	// 	// 	fmt.Println("登录成功！")
	// 	// }
	// case 2:
	// 	fmt.Println("进行用户注册")
	// }
}
