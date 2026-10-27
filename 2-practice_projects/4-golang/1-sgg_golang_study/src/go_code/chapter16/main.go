package main

import (
	"bufio"
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

	var fileString string
	reader := bufio.NewReader(file)
	for {
		// 一次读取一行数据
		str, err := reader.ReadString('\n')
		if err == io.EOF {
			fileString += str
			break
		}
		if err != nil {
			fmt.Println(err)
			return
		}
		fileString += str
	}
	fmt.Println(fileString)
}
