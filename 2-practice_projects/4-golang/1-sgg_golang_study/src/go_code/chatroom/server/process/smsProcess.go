package process

import (
	"demo/chatroom/common/message"
	"demo/chatroom/server/utils"
	"encoding/json"
	"fmt"
	"net"
)

type SmsProcess struct {
}

func (this *SmsProcess) SendGroupMes(mes *message.Message) (err error) {
	// 遍历服务器端的map，将消息转发出去

	// 解压json中的data数据，后面用于获取发起用户的id
	var smsMes message.SmsMes
	err = json.Unmarshal([]byte(mes.Data), &smsMes)
	if err != nil {
		fmt.Println("json.Unmarshal err=", err)
		return
	}

	// 原封不动把数据转为json
	data, err := json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}

	for id, up := range userMgr.onlineUsers {
		if id == smsMes.UserId {
			continue
		}
		fmt.Println("转发群聊消息给：", id, "内容是：", string(data))
		this.sendMesToEachOnlineUser(data, up.Conn)
	}
	return
}

func (this *SmsProcess) sendMesToEachOnlineUser(data []byte, conn net.Conn) (err error) {
	tf := &utils.Transfer{Conn: conn}
	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("发送群聊消息失败", err)
		return
	}
	return
}
