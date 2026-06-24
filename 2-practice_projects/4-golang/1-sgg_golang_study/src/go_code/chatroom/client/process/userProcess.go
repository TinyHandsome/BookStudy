package process

import (
	"demo/chatroom/client/utils"
	"demo/chatroom/common/message"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"net"
	"os"
)

type UserProcess struct {
}

func (this *UserProcess) Register(userId int, userName string, userPwd string) (err error) {
	// fmt.Println("用户", userId, "注册成功")
	// return nil
	// 1. 链接到服务器
	conn, err := net.Dial("tcp", "localhost:8889")
	if err != nil {
		fmt.Println("net.Dial err:", err)
		return err
	}
	defer conn.Close()

	var mes message.Message
	mes.Type = message.RegisterMesType
	var registerMes message.RegisterMes
	registerMes.User.UserId = userId
	registerMes.User.UserName = userName
	registerMes.User.UserPwd = userPwd

	data, err := json.Marshal(registerMes)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	mes.Data = string(data)
	data, err = json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	tf := &utils.Transfer{Conn: conn}
	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("注册发送信息错误：", err)
	}

	mes, err = tf.ReadPkg()
	if err != nil {
		fmt.Println("readPkg err:", err)
		return
	}

	var registerResMes message.RegisterResMes
	err = json.Unmarshal([]byte(mes.Data), &registerResMes)
	switch registerResMes.Code {
	case 200:
		fmt.Println("注册成功，请重新登录")
		os.Exit(0)
	default:
		fmt.Println(registerResMes.Error)
		os.Exit(0)

	}
	return
}

func (this *UserProcess) Login(userId int, userPwd string) (err error) {
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
	tf := &utils.Transfer{Conn: conn}
	mes, err = tf.ReadPkg()
	if err != nil {
		fmt.Println("readPkg err:", err)
		return
	}

	var loginResMes message.LoginResMes
	err = json.Unmarshal([]byte(mes.Data), &loginResMes)
	switch loginResMes.Code {
	case 200:
		// 初始化curUser
		CurUser.Conn = conn
		CurUser.UserId = userId
		CurUser.UserStatus = message.UserOnline

		// fmt.Println("登录成功")
		// 显示在线用户列表
		fmt.Println("登录成功！当前在线用户列表:")
		for _, v := range loginResMes.UsersId {
			// 不显示自己在线
			if userId == v {
				continue
			}
			fmt.Println("用户id:\t", v)
			// 完成客户端的onlineUsers 的初始化
			user := &message.User{
				UserId:     v,
				UserStatus: message.UserOnline,
			}
			onlineUsers[v] = user
		}
		fmt.Print("\n\n")

		// 启动协程，保持跟服务器端的通信，如果服务器有数据推送，就接受
		go serverProcessMes(conn)

		// 显示我们登录成功的菜单
		for {
			ShowMenu()
		}
	default:
		fmt.Println(loginResMes.Error)
	}

	return
}
