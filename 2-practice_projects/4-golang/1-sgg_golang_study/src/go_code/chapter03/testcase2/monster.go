package monster

import (
	"encoding/json"
	"fmt"
	"os"
)

type Monster struct {
	Name  string
	Age   int
	Skill string
}

func (this *Monster) Store() bool {
	data, err := json.Marshal(this)
	if err != nil {
		fmt.Println("json序列化失败：", err)
		return false
	}
	filePath := "monster.json"
	err = os.WriteFile(filePath, data, 0666)
	if err != nil {
		fmt.Println("文件写入失败：", err)
		return false
	}
	return true
}

func (this *Monster) ReStore() bool {
	filePath := "monster.json"
	data, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Println("文件读取失败：", err)
		return false
	}
	err = json.Unmarshal(data, this)
	if err != nil {
		fmt.Println("反序列化失败：", err)
		return false
	}
	return true
}
