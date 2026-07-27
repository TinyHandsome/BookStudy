package main

func SetWay(myMap *[8][7]int, i int, j int) bool {
	// 分析出什么情况下，就找到出路了
	if myMap[6][5] == 2 {
		return true
	} else {
		// 说明继续要找
		if myMap[i][j] == 0 {
			myMap[i][j] = 2
			// 右下左上
			if SetWay(myMap, i+1, j) {
				return true
			} else if SetWay(myMap, i, j+1) {
				return true
			} else if SetWay(myMap, i-1, j) {
				return true
			} else if SetWay(myMap, i, j-1) {
			} else {
				// 死路，不可能吧
				myMap[i][j] = 3
				return false
			}
		} else {
			// 是墙啦
			return false
		}
	}
	return false
}

func main() {
	// 1. 如果元素的值为1，就是墙
	// 2. 如果元素的值为0，是还没走过的点
	// 3. 如果元素的值为2，是已经走过的点
	// 4. 如果元素的值为3，是走过的点，但是走不通
	var myMap [8][7]int
	for i := 0; i < 7; i++ {
		myMap[0][i] = 1
		myMap[7][i] = 1
	}
	for i := 0; i < 8; i++ {
		myMap[i][0] = 1
		myMap[i][6] = 1
	}
	myMap[3][1] = 1
	myMap[3][2] = 1

	// 输出
	for i := 0; i < 8; i++ {
		for j := 0; j < 7; j++ {
			print(myMap[i][j], " ")
		}
		println()
	}
	println()

	SetWay(&myMap, 1, 1)
	// 探测完毕
	for i := 0; i < 8; i++ {
		for j := 0; j < 7; j++ {
			print(myMap[i][j], " ")
		}
		println()
	}
}
