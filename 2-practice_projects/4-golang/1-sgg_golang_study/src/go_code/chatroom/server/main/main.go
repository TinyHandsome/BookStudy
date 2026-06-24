package main

import (
	"demo/chatroom/server/model"
	"fmt"
	"net"
	"time"
)

func doProcess(conn net.Conn) {
	defer conn.Close()

	// 创还能总控
	processor := &Processor{Conn: conn}
	err := processor.Process2()
	if err != nil {
		fmt.Println("客户端和服务器通讯协程出错，err=", err)
		return
	}
}

func initUserDao() {
	// 这里的pool本身就是一个全局变量，在redis中
	model.MyUserDao = model.NewUserDao(pool)
}

func main() {
	initPool("localhost:6379", 16, 0, 300*time.Second)
	initUserDao()

	fmt.Println("服务器在8889端口监听。。。")
	listen, err := net.Listen("tcp", "0.0.0.0:8889")
	if err != nil {
		fmt.Println("net.Listen err=", err)
		return
	}
	defer listen.Close()

	for {
		fmt.Println("等待客户端连接。。。")
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println("listen.Accept err=", err)
			continue
		} else {
			fmt.Println("客户端连接成功。。。", conn, "客户端IP：", conn.RemoteAddr().String())
			go doProcess(conn)
		}
	}
}
