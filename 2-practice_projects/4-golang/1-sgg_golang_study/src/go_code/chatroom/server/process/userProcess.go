package process

import (
	"demo/chatroom/common/message"
	"demo/chatroom/server/model"
	"demo/chatroom/server/utils"
	"encoding/json"
	"fmt"
	"net"
)

type UserProcess struct {
	Conn net.Conn
	// 增加一个字段，表示该Conn是哪个用户的
	UserId int
}

// 通知所有在线的用户 userId 上线了
func (this *UserProcess) NotifyOthersOnlineUser(userId int) {
	// 获取所有在线用户
	onlineUsers := userMgr.GetAllOnlineUser()

	// 遍历
	for id, up := range onlineUsers {
		if id == userId {
			continue
		}
		// 开始通知
		up.NotifyMeOnline(userId)
	}
}

func (this *UserProcess) NotifyMeOnline(userId int) {
	var mes message.Message
	mes.Type = message.NotifyUserStatusMesType
	var notifyUserStatusMes message.NotifyUserStatusMes
	notifyUserStatusMes.UserId = userId
	notifyUserStatusMes.Status = message.UserOnline

	data, err := json.Marshal(notifyUserStatusMes)
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

	// 发送，这里不能提出去，因为一个this代表的是一个用户
	tf := &utils.Transfer{Conn: this.Conn}
	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("tf.WritePkg err:", err)
		return
	}
}

func (this *UserProcess) ServerProcessRegister(mes *message.Message) (err error) {
	var registerMes message.RegisterMes
	err = json.Unmarshal([]byte(mes.Data), &registerMes)
	if err != nil {
		fmt.Println("json.Unmarshal err:", err)
		return
	}

	var resMes message.Message
	resMes.Type = message.RegisterResMesType
	var registerResMes message.RegisterResMes
	err = model.MyUserDao.Register(&registerMes.User)

	if err != nil {
		if err == model.ERROR_USER_EXISTS {
			registerResMes.Code = 505
			registerResMes.Error = model.ERROR_USER_EXISTS.Error()
		} else {
			registerResMes.Code = 506
			registerResMes.Error = "注册发生未知错误。。。"
		}
	} else {
		registerResMes.Code = 200
	}

	// 返回结果序列化
	data, err := json.Marshal(registerResMes)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	resMes.Data = string(data)
	data, err = json.Marshal(resMes)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	tf := &utils.Transfer{Conn: this.Conn}
	err = tf.WritePkg(data)
	return
}

func (this *UserProcess) ServerProcessLogin(mes *message.Message) (err error) {
	// 处理登录请求，并返回结果

	// 1. 先从mes中取出 mes.Data，并直接反序列化成LoginMes
	var loginMes message.LoginMes
	err = json.Unmarshal([]byte(mes.Data), &loginMes)
	if err != nil {
		fmt.Println("json.Unmarshal err=", err)
		return
	}

	// 先声明一个 resMes
	var resMes message.Message
	resMes.Type = message.LoginResMesType
	// 再声明一个 LoginResMes
	var loginResMes message.LoginResMes

	// 我们需要到redis数据库去完成验证
	user, err := model.MyUserDao.Login(loginMes.UserId, loginMes.UserPwd)

	if err != nil {
		switch err {
		case model.ERROR_USER_NOTEXISTS:
			loginResMes.Code = 500
			loginResMes.Error = err.Error()
		case model.ERROR_USER_PWD:
			loginResMes.Code = 403
			loginResMes.Error = err.Error()
		default:
			loginResMes.Code = 500
			loginResMes.Error = "服务器内部错误，请稍后再试。。。"
		}
	} else {
		loginResMes.Code = 200
		// 用户登录成功之后，把用户放入到userMgr中
		// 将登录成功的用户id赋给this
		this.UserId = loginMes.UserId
		userMgr.AddOnlineUser(this)
		// 将当前在线用户的id放入返回内容中 loginResMes.UsersId
		// 遍历 userMgr.onlineUsers
		for id, _ := range userMgr.onlineUsers {
			loginResMes.UsersId = append(loginResMes.UsersId, id)
		}
		// 通知其他的在线用户，我上线了
		this.NotifyOthersOnlineUser(loginMes.UserId)
		fmt.Println("用户：", user, "登录成功")
	}

	// 检验用户 id  和 密码合法
	// if loginMes.UserId == 100 && loginMes.UserPwd == "123456" {
	// 	loginResMes.Code = 200
	// } else {
	// 	loginResMes.Code = 500
	// 	loginResMes.Error = "该用户不存在，请注册后再使用。。。"
	// }

	// 将loginResMes 序列化成 json
	data, err := json.Marshal(loginResMes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}

	// 将data赋值给resMes
	resMes.Data = string(data)
	// 对resMes进行序列化，准备发送
	data, err = json.Marshal(resMes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}

	// 发送
	tf := &utils.Transfer{Conn: this.Conn}
	err = tf.WritePkg(data)
	return
}
