package main

import (
	"fmt"
	"time"
)

func adder() func() int {
	var i = 10
	return func() int {
		i++
		return i + 1
	}
}

func f1() {
	func() {
		fmt.Println("111")
	}()

	func(x, y int) {
		fmt.Println(x + y)
	}(10, 20)

	fn := func(x, y int) int {
		return x * y
	}
	fmt.Println(fn(2, 3))
}

func f2() int {
	var a int
	defer func() {
		a++
	}()
	return a
}
func f3() (a int) {
	defer func() {
		a++
	}()
	return a
}

func f4() (x int) {
	defer func(x int) {
		x++
	}(x)
	return
}

func ff1() {
	defer func() {
		err := recover()
		if err != nil {
			fmt.Println("recover err = ", err)
		}
	}()
	panic("抛出了一个异常")
}

type Person struct {
	string
	int
}

type AA struct {
	Username string
	Password string
	Address
}

type Address struct {
	Name string
	Age  int
}

func main() {
	a := 10
	fmt.Printf("a=%v atype=%T", a, a)

	const (
		n1 = 10
		n2
		n3
		n4
	)

	const (
		b = iota
		c
		d
		e
	)
	fmt.Println(n1, n2, n3, n4)
	fmt.Println(b, c, d, e)

	arr1 := [...]int{1, 2, 3}
	fmt.Println(arr1)

	s := []int{2, 3, 5, 7, 11, 13}
	bs := s[1:3]
	fmt.Println(len(bs), cap(bs))

	f1()

	ff := adder()
	fmt.Println(ff())
	fmt.Println(ff())
	fmt.Println(ff())

	fmt.Println(f2())
	fmt.Println(f3())
	fmt.Println(f4())

	ff1()

	fmt.Println(time.Now())
	fmt.Println(time.Now().Year())
	fmt.Println(time.Now().Unix())
	fmt.Println(time.Now().UnixNano())

	fmt.Println(time.Unix(1789458792, 0).Format("2006-01-02 03:04:05"))

	t, _ := time.ParseInLocation("2006-01-02 15:04:05", "2026-09-15 15:58:33", time.Local)
	fmt.Println(t.Unix())

	// ticker := time.NewTicker(time.Second)
	// for t := range ticker.C {
	// 	fmt.Println(t)
	// }

	newa := new(int(100))
	fmt.Println(*newa)

	pp1 := Person{"张三", 18}
	fmt.Println(pp1.string, pp1.int)

	var uu AA
	uu.Username = "张三"
	uu.Password = "123456"
	uu.Address.Name = "北京"
	uu.Address.Age = 18
	fmt.Println(uu)

}
