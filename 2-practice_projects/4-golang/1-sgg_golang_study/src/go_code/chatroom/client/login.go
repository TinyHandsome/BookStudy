package main

import (
	"demo/chatroom/common/message"
	"demo/chatroom/server/utils"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"net"
)

func login(userId int, userPwd string) (err error) {
	// fmt.Println("用户", userId, "登录成功")
	// return nil
	// 1. 链接到服务器
	conn, err := net.Dial("tcp", "localhost:8889")
	if err != nil {
		fmt.Println("net.Dial err:", err)
		return err
	}
	defer conn.Close()

	// 2. 准备通过conn发送消息给服务
	var mes message.Message
	mes.Type = message.LoginMesType

	// 3. 创建一个LoginMes结构体
	var loginMes message.LoginMes
	loginMes.UserId = userId
	loginMes.UserPwd = userPwd

	// 4. 将loginMes进行序列化
	data, err := json.Marshal(loginMes)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	// 5. 将data赋予 mes.Data 字段
	mes.Data = string(data)

	// 6. 将mes进行序列化
	data, err = json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	// 7. 发送data给服务器
	// 7.1 先把data的长度发送给服务器
	var pkgLen uint32
	pkgLen = uint32(len(data))
	var buf [4]byte
	binary.BigEndian.PutUint32(buf[:4], pkgLen)
	// 发送长度
	n, err := conn.Write(buf[:4])
	if n != 4 || err != nil {
		fmt.Println("conn.Write err:", err)
		return
	}

	fmt.Println("客户端，发送消息长度成功...", len(data), string(data))

	// 发送消息本身
	_, err = conn.Write(data)
	if err != nil {
		fmt.Println("conn.Write err:", err)
		return
	}

	// time.Sleep(20 * time.Second)
	tf := utils.Transfer{Conn: conn}
	mes, err = tf.ReadPkg()
	if err != nil {
		fmt.Println("readPkg err:", err)
		return
	}

	var loginResMes message.LoginResMes
	err = json.Unmarshal([]byte(mes.Data), &loginResMes)
	switch loginResMes.Code {
	case 200:
		fmt.Println("登录成功")
	case 500:
		fmt.Println(loginResMes.Error)
	}

	return
}
