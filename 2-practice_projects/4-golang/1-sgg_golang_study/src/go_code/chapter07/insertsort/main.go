package main

import "fmt"

func InsertSort(arr []int) {
	// 插入排序
	for i := 1; i < len(arr); i++ {
		// 待插入的元素
		insertVal := arr[i]
		// 下标总是待插入元素的前一个
		insertIndex := i - 1
		// 找到插入位置
		for insertIndex >= 0 && insertVal > arr[insertIndex] {
			// 比较值后移
			arr[insertIndex+1] = arr[insertIndex]
			// 指针前移
			insertIndex--
		}
		// 指针+1的位置 写入待插入的元素
		if insertIndex+1 != i {
			arr[insertIndex+1] = insertVal
		}
		fmt.Printf("第%d次插入后的数组为：%v\n", i, arr)
	}
}

func main() {
	arr := []int{23, 0, 12, 56, 34}
	fmt.Printf("初始数组为：%v\n", arr)
	InsertSort(arr)
}
