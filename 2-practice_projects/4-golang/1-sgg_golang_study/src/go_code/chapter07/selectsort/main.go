package main

import "fmt"

func SelectSort(arr *[5]int) {
	for i := 0; i < len(arr)-1; i++ {
		max := i
		for j := i + 1; j < len(arr); j++ {
			if arr[max] < arr[j] {
				max = j
			}
		}
		if i != max {
			arr[i], arr[max] = arr[max], arr[i]
		}
	}
}
func main() {
	arr := [5]int{10, 34, 19, 100, 80}
	SelectSort(&arr)
	fmt.Println(arr)
}
