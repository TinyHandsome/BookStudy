package main

import "fmt"

type ValNode struct {
	row int
	col int
	val int
}

func main() {
	var chessMap [11][11]int
	chessMap[1][2] = 1
	chessMap[2][3] = 2

	for _, v := range chessMap {
		for _, v2 := range v {
			// fmt.Printf("第%d行, 第%d列, 值为%d\n", i, j, v2)
			fmt.Printf("%d\t", v2)
		}
		fmt.Println()
	}

	// 转成稀疏数组
	var sparseArr []ValNode
	sparseArr = append(sparseArr, ValNode{11, 11, 0})
	for i, v := range chessMap {
		for j, v2 := range v {
			if v2 != 0 {
				sparseArr = append(sparseArr, ValNode{i, j, v2})
			}
		}
		fmt.Println()
	}

	// 输出稀疏数组
	fmt.Println("稀疏数组为:")
	for i, valNode := range sparseArr {
		fmt.Printf("第%d行, row:%d, col:%d, val:%d\n", i, valNode.row, valNode.col, valNode.val)
	}

	// 恢复数组
	var chessMap2 [11][11]int
	for _, valNode := range sparseArr[1:] {
		chessMap2[valNode.row][valNode.col] = valNode.val
	}
	fmt.Println("恢复后的数组为:")
	for _, v := range chessMap2 {
		for _, v2 := range v {
			fmt.Printf("%d\t", v2)
		}
		fmt.Println()
	}
}
