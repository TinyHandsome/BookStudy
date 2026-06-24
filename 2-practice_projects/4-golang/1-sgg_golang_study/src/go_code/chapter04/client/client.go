package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

func main() {
	conn, err := net.Dial("tcp", "127.0.0.1:8888")
	if err != nil {
		fmt.Println("net.Dial err=", err)
		return
	}
	defer conn.Close()

	// 1. 客户端可以发送单行数据，然后退出
	reader := bufio.NewReader(os.Stdin)

	for {
		// 从终端读取一行用户的输入，并准备发送给服务器
		line, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("reader.ReadString err=", err)
			return
		}
		// 如果用户输入的是exit，就退出
		line = strings.TrimSpace(line)
		if line == "exit" {
			fmt.Println("用户退出。。。")
			return
		}
		// 再将line发送给服务器
		_, err = conn.Write([]byte(line))
		if err != nil {
			fmt.Println("conn.Write err=", err)
		}
	}
}
