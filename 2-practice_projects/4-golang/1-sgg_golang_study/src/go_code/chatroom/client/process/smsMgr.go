package process

import (
	"demo/chatroom/common/message"
	"encoding/json"
	"fmt"
)

func outputGroupMes(mes *message.Message) {
	// 反序列化 mes.Data
	var smsMes message.SmsMes
	err := json.Unmarshal([]byte(mes.Data), &smsMes)
	if err != nil {
		fmt.Println("json.Unmarshal err=", err)
		return
	}
	// 显示内容
	info := fmt.Sprintf("用户id:\t%d 对大家说:\t%s",
		smsMes.UserId, smsMes.Content)
	fmt.Println(info)
	fmt.Println()
}
