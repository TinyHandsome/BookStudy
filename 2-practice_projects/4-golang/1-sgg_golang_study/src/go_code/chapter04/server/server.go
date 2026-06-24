package main

import (
	"fmt"
	"io"

	// 做socket网络开发时，net包含以后我们需要所有的方法和函数
	"net"
)

func process(conn net.Conn) {
	// 这里我们循环的接收客户端发送的数据
	defer conn.Close()
	for {
		// 创建一个新的切片
		buf := make([]byte, 1024)
		// 等待客户端通过conn发送信息流，如果客户端没有Write，那么会一直阻塞
		// fmt.Println("服务器等待客户端发送数据。。。", conn.RemoteAddr().String())
		n, err := conn.Read(buf)
		if err == io.EOF {
			fmt.Println("客户端退出了。。。")
			return
		}
		// 显示客户端发送的内容到服务器的终端
		fmt.Println("服务器收到客户端发来的数据：", string(buf[:n]))
	}
}

func main() {
	fmt.Println("服务器开始监听了。。。")
	listen, err := net.Listen("tcp", "0.0.0.0:8888")

	if err != nil {
		fmt.Println("net.Listen err=", err)
		return
	}
	defer listen.Close() // 延时关闭

	for {
		fmt.Println("等待客户端连接。。。")
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println("listen.Accept err=", err)
			continue
		} else {
			fmt.Println("客户端连接成功。。。", conn, "客户端IP：", conn.RemoteAddr().String())
		}
		go process(conn)
	}
}
