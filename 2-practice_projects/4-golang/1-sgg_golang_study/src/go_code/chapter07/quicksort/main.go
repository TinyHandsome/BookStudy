package main

import "fmt"

func QuickSort(left int, right int, array []int) {
	// 快速排序
	// left：数组左边的下标
	// right：数组的右边下标
	// array：待排序的数组
	l := left
	r := right
	if l > r {
		return
	}
	// 中轴：待排序数组中间的元素
	pivot := array[(l+r)/2]
	temp := 0

	// for循环的目标是将比 pivot小的数放到左边，大的数放在右边
	for l <= r {
		// 找到比中轴小的数，放到左边
		for array[l] < pivot {
			l++
		}
		// 找到比中轴大的数，放到右边
		for array[r] > pivot {
			r--
		}
		// 如果l >= r，说明中轴的数，左边的数都比它小，右边的数都比它大，跳出循环
		if l >= r {
			break
		}
		// 如果l < r，则交换l和r
		temp = array[l]
		array[l] = array[r]
		array[r] = temp
		// 如果交换的数是中轴，则r继续向左移动l，避免重复交换
		if array[l] == pivot {
			r--
		}
		// 如果交换的数是中轴，则l继续向右移动r，避免重复交换
		if array[r] == pivot {
			l++
		}
	}
	// 如果l == r，说明l和r已经相遇，则分别继续移动一位
	if l == r {
		l++
		r--
	}
	// 向左递归
	if left < r {
		QuickSort(left, r, array)
	}
	// 向右递归
	if right > l {
		QuickSort(l, right, array)
	}
}

func main() {
	arr := []int{-9, 78, 0, 23, -567, 70, 1, 43, 421, 56, 89}
	QuickSort(0, len(arr)-1, arr)
	fmt.Println(arr)
}
