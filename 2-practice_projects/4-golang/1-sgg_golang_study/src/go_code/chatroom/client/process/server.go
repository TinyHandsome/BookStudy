package process

import (
	"demo/chatroom/client/utils"
	"demo/chatroom/common/message"
	"encoding/json"
	"fmt"
	"net"
	"os"
)

// 显示登录成功后的界面
func ShowMenu() {
	fmt.Println("----------恭喜xxx登录成功----------")
	fmt.Println("----------1. 显示在线用户列表----------")
	fmt.Println("----------2. 发送消息----------")
	fmt.Println("----------3. 信息列表----------")
	fmt.Println("----------4. 退出系统----------")
	fmt.Println("请选择（1-4）：")
	var key int
	var content string

	smsProcess := &SmsProcess{}
	fmt.Scanf("%d\n", &key)
	switch key {
	case 1:
		// fmt.Println("显示在线用户列表")
		outputOnlineUser()
	case 2:
		fmt.Println("请输入你想对大家说的话：")
		fmt.Scanf("%s\n", &content)
		smsProcess.SendGroupMes(content)
	case 3:
		fmt.Println("信息列表")
	case 4:
		fmt.Println("你选择退出了系统。。。")
		os.Exit(0)
	default:
		fmt.Println("你输入的选项不对。。。")
	}
}

// 和服务器保持通讯
func serverProcessMes(conn net.Conn) {
	// 创建一个transfer实例，不停的读取服务器发送的消息
	tf := &utils.Transfer{
		Conn: conn,
	}
	for {
		fmt.Println("客户端正在等待读取服务器发送的消息。。。")
		mes, err := tf.ReadPkg()
		if err != nil {
			fmt.Println("tf.ReadPkg err=", err)
			return
		}
		// 如果读取到消息，又是下一步处理逻辑
		switch mes.Type {
		case message.NotifyUserStatusMesType:
			// 1. 取出NotifyUserStatusMes
			var notifyUserStatusMes message.NotifyUserStatusMes
			err := json.Unmarshal([]byte(mes.Data), &notifyUserStatusMes)
			if err != nil {
				fmt.Println("json.Unmarshal err=", err)
				return
			}
			updateUserStatus(&notifyUserStatusMes)
		default:
			fmt.Println("服务器发送了未知的消息。。。")
		}
		// fmt.Println("mes=", mes)
	}
}
