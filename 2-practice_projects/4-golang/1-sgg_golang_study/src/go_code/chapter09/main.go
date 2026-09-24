package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup

func test() {
	for i := 0; i < 10; i++ {
		fmt.Println("i = ", i)
	}
	wg.Done()
}

func test2() {
	for i := 0; i < 10; i++ {
		fmt.Println("q = ", i)
	}
	wg.Done()
}

func main() {
	wg.Add(1)
	go test()
	wg.Add(1)
	go test2()
	for i := 0; i < 10; i++ {
		// fmt.Println("main goroutine i = ", i)
	}

	wg.Wait()
	fmt.Println("main goroutine end")

	cpuNum := runtime.NumCPU()
	fmt.Println("cpuNum =", cpuNum)
}
