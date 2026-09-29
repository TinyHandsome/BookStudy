package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func test(n int) {
	for num := (n - 1) * 300000; num < n*300000; num++ {
		if num <= 1 {
			// 1不是素数就不用判断了
			continue
		}
		var flag = true
		for i := 2; i < num; i++ {
			if num%i == 0 {
				flag = false
				break
			}
		}
		if flag {
			// fmt.Println(num, "是素数")
		}
	}
	wg.Done()
}

func main() {
	start := time.Now().Unix()
	for i := 1; i < 11; i++ {
		wg.Add(1)
		go test(i)
	}
	wg.Wait()
	fmt.Println("结束")
	end := time.Now().Unix()
	fmt.Println("程序运行时间：", end-start, "秒")
}
