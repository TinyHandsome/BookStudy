package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	file, err := os.Open("./main.go")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	// 操作文件
	var strSlice []byte
	var tempSlice = make([]byte, 128)

	for {
		n, err := file.Read(tempSlice)
		if err == io.EOF { // 文件读取完毕
			break
		}
		if err != nil {
			fmt.Println(err)
			return
		}

		fmt.Println("读取了：", n, "字节")
		// 注意这里的 :n 写法
		strSlice = append(strSlice, tempSlice[:n]...)
	}
	fmt.Println(string(strSlice))
}
