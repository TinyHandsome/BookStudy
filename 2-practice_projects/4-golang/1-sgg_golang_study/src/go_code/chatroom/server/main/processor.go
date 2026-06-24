package main

import (
	"demo/chatroom/common/message"
	"demo/chatroom/server/process"
	"demo/chatroom/server/utils"
	"fmt"
	"io"
	"net"
)

type Processor struct {
	Conn net.Conn
}

// 功能：根据客户端发送消息种类不同，决定调用哪个函数来处理
func (this *Processor) serverProcessMes(mes *message.Message) (err error) {
	// 处理解析好的数据，根据不同的类型做不同的处理
	fmt.Println("mes= ", mes)

	switch mes.Type {
	case message.LoginMesType:
		// 处理登录
		// 创建一个处理登录的processor
		fmt.Println("处理登录...")
		up := &process.UserProcess{Conn: this.Conn}
		err = up.ServerProcessLogin(mes)
	case message.RegisterMesType:
		fmt.Println("处理注册...")
		// 处理注册
		up := &process.UserProcess{Conn: this.Conn}
		err = up.ServerProcessRegister(mes)

	default:
		fmt.Println("消息类型不存在，无法处理。。。")
	}
	return
}

func (this *Processor) Process2() (err error) {
	// 读取数据并解析，处理服务器的数据 -> serverProcessMes

	for {
		tf := utils.Transfer{Conn: this.Conn}
		mes, err := tf.ReadPkg()
		if err != nil {
			if err == io.EOF {
				fmt.Println("客户端退出了。。。")
			} else {
				fmt.Println("readPkg err=", err)
			}
			return err
		}

		// fmt.Println("mes=", mes)
		err = this.serverProcessMes(&mes)
		if err != nil {
			fmt.Println("serverProcessMes err=", err)
			return err
		}

	}
}
