package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func putNum(intChan chan int) {
	for i := 2; i < 120000; i++ {
		intChan <- i
	}
	close(intChan)
	wg.Done()
}

func primeNum(intChan chan int, primeChan chan int, exitChan chan bool) {
	for num := range intChan {
		var flag = true
		for i := 2; i < num; i++ {
			if num%i == 0 {
				flag = false
				break
			}
		}
		if flag {
			primeChan <- num
		}
	}
	exitChan <- true
	wg.Done()
}

func printPrime(primeChan chan int) {
	for num := range primeChan {
		fmt.Println(num)
	}
	wg.Done()
}

func main() {
	// 从 intChan 取出数据，并判断是否为素数，如果是，就放到 primeChan
	intChan := make(chan int, 1000)
	primeChan := make(chan int, 1000)
	// 标识primeChan退出
	exitChan := make(chan bool, 16)

	// 存放数字的协程
	wg.Add(1)
	go putNum(intChan)
	// 统计素数的协程
	for i := 0; i < 16; i++ {
		wg.Add(1)
		go primeNum(intChan, primeChan, exitChan)
	}
	// 打印素数的协程
	wg.Add(1)
	go printPrime(primeChan)
	// 判断exitChan是否存满值
	wg.Add(1)
	go func() {
		for i := 0; i < 16; i++ {
			<-exitChan
		}
		// 关闭primeChan
		close(primeChan)
		wg.Done()
	}()

	wg.Wait()
	fmt.Println("main goroutine done")
}
