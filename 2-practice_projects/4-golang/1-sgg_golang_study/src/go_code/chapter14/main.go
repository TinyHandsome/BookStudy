package main

import (
	"fmt"
	"reflect"
)

func reflectFn(x any) {
	v := reflect.TypeOf(x)
	fmt.Println(v)
}

func main() {
	a := 10
	b := 23.4
	c := true
	d := "hello world"
	reflectFn(a)
	reflectFn(b)
	reflectFn(c)
	reflectFn(d)

}
