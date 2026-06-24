package process

import (
	"demo/chatroom/client/utils"
	"demo/chatroom/common/message"
	"encoding/json"
	"fmt"
)

type SmsProcess struct {
}

// 发送群聊的消息
func (this *SmsProcess) SendGroupMes(content string) (err error) {
	var mes message.Message
	mes.Type = message.SmsMesType

	var smsMes message.SmsMes
	smsMes.Content = content
	smsMes.UserId = CurUser.UserId
	smsMes.UserStatus = CurUser.UserStatus

	data, err := json.Marshal(smsMes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}

	mes.Data = string(data)
	data, err = json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}

	tf := &utils.Transfer{Conn: CurUser.Conn}
	fmt.Println("正在发送群消息，内容是：", string(data))
	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("发送群聊消息失败")
		return
	}

	return
}
