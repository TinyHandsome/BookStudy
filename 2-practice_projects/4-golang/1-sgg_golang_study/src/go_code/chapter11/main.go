package main

import "fmt"

func main() {
	ch := make(chan int, 3)
	ch <- 10
	ch <- 20
	ch <- 30
	a := <-ch
	fmt.Println(a)
	<-ch
	c := <-ch
	fmt.Println(c)
}
