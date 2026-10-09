package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func writeData(ch chan int) {
	for i := 0; i < 10; i++ {
		ch <- i
		fmt.Printf("写入数据：%d\n", i)
		time.Sleep(time.Millisecond * 5)
	}
	close(ch)
	wg.Done()
}
func readData(ch chan int) {
	for v := range ch {
		fmt.Println("从管道中读到的数据是：", v)
		time.Sleep(time.Millisecond * 1000)

	}
	wg.Done()
}

func main() {
	var ch = make(chan int, 10)
	wg.Add(2)
	go writeData(ch)
	go readData(ch)
	wg.Wait()
	fmt.Println("main goroutine end...")
}
