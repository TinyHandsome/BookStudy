package main

import (
	"fmt"
	"os"
)

func main() {
	byteStr, err := os.ReadFile("./main.go")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(byteStr))
}
