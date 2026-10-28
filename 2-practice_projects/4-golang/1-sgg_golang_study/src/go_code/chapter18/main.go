package main

import "fmt"

type Number interface {
	int | int32 | int64 | float64
}

func getDataInterface[T Number](value T) T {
	return value
}
func main() {
	// str1 := getDataInterface("hello")
	// str2 := getDataInterface(123)
	// str3 := getDataInterface(true)
	// fmt.Println(str1, str2, str3)
	fmt.Println(getDataInterface(123))
}
