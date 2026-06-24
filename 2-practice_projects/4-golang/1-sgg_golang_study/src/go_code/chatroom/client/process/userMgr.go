package process

import (
	"demo/chatroom/client/model"
	"demo/chatroom/common/message"
	"fmt"
)

// 客户端要维护的map
var onlineUsers map[int]*message.User = make(map[int]*message.User, 10)

// 在用户登录成功后完成初始化
var CurUser model.CurUser

// 在客户端显示当前在线的用户
func outputOnlineUser() {

	fmt.Println("有用户状态更新 - 当前在线用户列表:")
	for id, _ := range onlineUsers {
		fmt.Println("用户id:\t", id)
	}
	fmt.Print("\n\n")
}

func updateUserStatus(notifyUserStatusMes *message.NotifyUserStatusMes) {

	user, ok := onlineUsers[notifyUserStatusMes.UserId]
	if !ok {
		// 没有才创建
		user = &message.User{
			UserId: notifyUserStatusMes.UserId,
		}
	}

	// 更新状态
	user.UserStatus = notifyUserStatusMes.Status
	onlineUsers[notifyUserStatusMes.UserId] = user
	outputOnlineUser()
}
