package main

import (
	"fmt"
	"os"
	"reflect"
	"strings"
	"sync"
	"time"
)

var a1, a2, a3 = 1, 2, 3
var (
	b1 = 10
	b2 = 20
	b3 = 39
)

func main() {
	/*
		var i int
		// i = 10
		fmt.Println("i=", i)

		var a = 10
		fmt.Println("a=", a)

		b := 3.3
		fmt.Println("b=", b)

		var n1, n2, n3 int
		// n1, n2, n3 = 1, 2, 3
		fmt.Println(n1, n2, n3)
		var n4, n5, n6 = 100, "tom", true
		fmt.Println(n4, n5, n6)

		n7, n8, n9 := 100, "tom", true
		fmt.Println(n7, n8, n9)

		fmt.Println(a1, a2, a3)

		var nn1 = 100
		fmt.Printf("n1 type is: %T\n", nn1)

		var num1 int64 = 10
		fmt.Printf("num1 type is: %T, num1 bytes is %d\n", num1, unsafe.Sizeof(num1))

		num2 := 5.1234e2
		fmt.Printf("num2 type is: %T, num2 bytes is %d\n", num2, unsafe.Sizeof(num2))

		var c1 byte = 'a'
		var c2 byte = '0'
		fmt.Println(c1, c2)

		fmt.Printf("c4=%c \n", 22269)

		var address string = "北京长城 110 helloworld"
		fmt.Println(address)

		str1 := `asdfasdfasdf\nasdfasdf`
		fmt.Println(str1)

		var numm int64 = 999999
		var numm2 int8 = int8(numm)
		fmt.Println(numm2)
	*/

	/*
		var num1 int = 99
		var num2 float64 = 23.456
		var b bool = true
		var myCar byte = 'h'
		var str string

		// method 1
		str = fmt.Sprintf("%d", num1)
		fmt.Printf("str type %T str=%q \n", str, str)
		str = fmt.Sprintf("%f", num2)
		fmt.Printf("str type %T str=%q \n", str, str)
		str = fmt.Sprintf("%t", b)
		fmt.Printf("str type %T str=%q \n", str, str)
		str = fmt.Sprintf("%c", myCar)
		fmt.Printf("str type %T str=%q \n", str, str)

		// method 2
		str = strconv.FormatInt(int64(num1), 10)
		fmt.Printf("str type %T str=%q \n", str, str)
		str = strconv.Itoa(num1)
		fmt.Printf("str type %T str=%q \n", str, str)

		str = strconv.FormatFloat(num2, 'f', 10, 64)
		fmt.Printf("str type %T str=%q \n", str, str)
		str = strconv.FormatBool(b)
		fmt.Printf("str type %T str=%q \n", str, str)

		var str2 string = "true"
		var bb bool
		bb, _ = strconv.ParseBool(str2)
		fmt.Printf("b type %T b=%v \n", bb, bb)
	*/

	/*
		i := 10
		fmt.Println("i 的地址是 ", &i)

		var ptr *int = &i
		fmt.Println("ptr 是 ", ptr)
		fmt.Println("ptr 的地址是 ", &ptr)
		fmt.Println("ptr 指向的值是 ", *ptr)

		fmt.Println(10 / 4)
		fmt.Println(10.0 / 4)

		a := 1
		b := 3
		a, b = b, a
		fmt.Println(a, b)
	*/

	/*
		var name string
		var age int
		var sal float32
		// fmt.Println("请输入姓名：")
		// fmt.Scanln(&name)
		// fmt.Println("名字是：", name)

		fmt.Println("请输入你的几个名字，用空格隔开")
		fmt.Scanf("%s %f %d", &name, &sal, &age)
		fmt.Printf("名字是：%v 薪水是：%v 年龄是：%v", name, sal, age)
	*/

	// fmt.Printf("%d\n", 011)
	// fmt.Printf("%d\n", 0x11)

	// var a int = 1 >> 2
	// var b int = -1 >> 2
	// var c int = 1 << 2
	// var d int = -1 << 2
	// fmt.Println(a, b, c, d)

	// if a := 1; a == 1 {
	// 	fmt.Println("a==1")
	// } else {
	// 	fmt.Println("a!=1")
	// }

	// var a int32 = 30
	// var b int32 = 33
	// if a+b > 50 {
	// 	fmt.Println("hello world!")
	// }

	// var a float64 = 3.0
	// var b float64 = 100.0
	// var c float64 = 6.0

	// m := b*b - 4*a*c
	// if m > 0 {
	// 	x1 := (-b + math.Sqrt(m)) / (2 * a)
	// 	x2 := (-b - math.Sqrt(m)) / (2 * a)
	// 	fmt.Printf("x1 = %v, x2 = %v", x1, x2)
	// } else if m == 0 {
	// 	x1 := (-b + math.Sqrt(m)) / 2 * a
	// 	fmt.Printf("x1 = %v", x1)
	// } else {
	// 	fmt.Println("无解")
	// }

	// var key byte
	// var x byte = 'b'
	// fmt.Println("请输入一个字符：")
	// fmt.Scanf("%c", &key)
	// switch key {
	// case 'a', 'd':
	// 	fmt.Println("你输入的是a或者d")
	// case x:
	// 	fmt.Println("你输入的是c")
	// case 'b':
	// 	fmt.Println("你输入的是b")
	// default:
	// 	fmt.Println("你输入的是其他字符")
	// }

	// var age int = 10
	// switch {
	// case age == 10:
	// 	fmt.Println("age = 10")
	// 	fallthrough
	// case age == 20:
	// 	fmt.Println("age = 20")
	// default:
	// 	fmt.Println("age != 10, age != 20")
	// }

	// var x interface{}
	// var y = 10.0
	// x = y
	// switch i := x.(type) {
	// case nil:
	// 	fmt.Println("x is nil")
	// case int:
	// 	fmt.Println("x is int")
	// case float64:
	// 	fmt.Println("x is float64")
	// case func(int) float64:
	// 	fmt.Println("x is func(int) float64")
	// case bool, string:
	// 	fmt.Println("x is bool or string")
	// default:
	// 	fmt.Printf("未知类型 %T\n", i)
	// }

	// var char byte
	// fmt.Println("请输入一个字符：")
	// fmt.Scanf("%c", &char)
	// switch char {
	// case 'a', 'e', 'i', 'o', 'u':
	// 	// 把字符大写输出
	// 	fmt.Printf("%c", unicode.ToUpper(rune(char)))
	// default:
	// 	fmt.Println("other")
	// }

	// i := 1
	// for i <= 10 {
	// 	fmt.Println(i)
	// 	i++
	// }

	// str := "烟台欢迎你"
	// for i, v := range str {
	// 	fmt.Printf("index=%d, val=%c\n", i, v)
	// }

	// sum := 0
	// for i := 0; i < 100; i++ {
	// 	if i%9 == 0 {
	// 		sum += i
	// 	}
	// }
	// fmt.Println(sum)

	// rand.Seed(time.Now().Unix())
	// fmt.Println(rand.Intn(100) + 1)

	// label2:
	// 	for i := 0; i < 10; i++ {
	// 		for j := 0; j < 10; j++ {
	// 			if j == 2 {
	// 				break label2
	// 				fmt.Println(j)
	// 			}
	// 		}
	// 	}

	// 	fmt.Println("ok1")
	// 	goto label2
	// 	fmt.Println("ok2")
	// 	fmt.Println("ok3")
	// 	fmt.Println("ok4")
	// label2:
	// 	fmt.Println("ok5")
	// 	fmt.Println("ok6")

	// test2(4)

	// // 斐波那契数
	// fmt.Println(fib(5))
	// // 函数作为形参调用
	// test_fib(fib, 1, 2)
	// // ...
	// fmt.Println(calc(4, 2))

	// res1 := func(n1 int, n2 int) int {
	// 	return n1 + n2
	// }(10, 20)
	// fmt.Println(res1)

	// a := func(n1 int, n2 int) int {
	// 	return n1 + n2
	// }
	// fmt.Println(a(1, 2))

	// fmt.Println(Func1(33, 34))

	// f := AddUpper()
	// fmt.Println(f(1))
	// fmt.Println(f(2))

	// f := makeSuffix(".jpg")
	// fmt.Println("文件名处理后=", f("winter.jpg"))

	// sum(3, 4)
	// str1 := "123123呗"
	// str2 := []rune(str1)
	// fmt.Println(len(str2))

	// fmt.Println(strconv.Atoi("12"))
	// fmt.Println(strconv.Itoa(12))

	// var bytes = []byte("hello go")
	// fmt.Println(bytes)

	// fmt.Println(string([]byte{97, 98, 99}))
	// fmt.Println(strings.EqualFold("abc", "aBc"))
	// fmt.Println(strings.Index("你好啊朋友", "朋1"))

	// fmt.Println(strings.Trim("aa123a123aa", "aa"))

	// fmt.Println(time.Now())
	// fmt.Println(time.Now().Month())
	// fmt.Println(time.Now().Format("2006-01-02 15:04:05"))
	// fmt.Println(time.Now().Format("yyyy-MM-dd"))

	// fmt.Println(1)
	// time.Sleep(1 * time.Second)
	// fmt.Println(2)

	// num2 := new(int)
	// fmt.Printf("num2的类型：%T，num2的值：%v，num2的地址：%v", num2, num2, &num2)

	// testException()

	// var hens [6]float64
	// hens[0] = 10.0
	// fmt.Println(hens)
	// for i := 0; i < len(hens); i++ {
	// 	fmt.Println(hens[i])
	// }

	// list := [3]string{1: "tom", 0: "jack", 2: "marry"}
	// fmt.Println(list)

	// for i, v := range list {
	// 	fmt.Println(i, v)
	// }

	// var intArr [5]int = [5]int{1, -1, 9, 90, 11}
	// maxVal := intArr[0]
	// maxValIndex := 0

	// for i := 1; i < len(intArr); i++ {
	// 	if intArr[i] > maxVal {
	// 		maxVal = intArr[i]
	// 		maxValIndex = i
	// 	}
	// }

	// fmt.Println("最大值是：", maxVal, "最大值索引是：", maxValIndex)

	// s1 := intArr[:]
	// fmt.Println(append(s1, s1...))

	// s := "asdf@qqqq"
	// qp := s[4:]
	// fmt.Printf("qp type = %T\n\n", qp)

	// arr := []byte(s)
	// arr[0] = 'A'
	// strnew := string(arr)
	// fmt.Println(strnew)

	// list := [5]int{24, 69, 80, 57, 13}
	// BubbleSort(&list)

	// list := [6]int{1, 24, 69, 80, 157, 193}
	// BinaryFind(&list, 24, 0, len(list)-1)
	// var arr = [2][3]int{{1, 2, 3}, {4, 5, 6}}
	// fmt.Println(arr)
	// for i := 0; i < len(arr); i++ {
	// 	for j := 0; j < len(arr[i]); j++ {
	// 		fmt.Printf("arr[%v][%v] = %v\n", i, j, arr[i][j])
	// 	}
	// }

	// var m map[string]int
	// m = make(map[string]int, 1)
	// m["name"] = 1
	// m["name2"] = 1
	// fmt.Println(m)

	// var t A
	// t.test()

	// computer := Computer{}
	// phone := Phone{}
	// camera := Camera{}

	// computer.BindingUsb(phone)
	// computer.BindingUsb(camera)

	// file, err := os.Open("test.txt")
	// if err != nil {
	// 	fmt.Println("打开文件失败：", err)
	// }
	// defer file.Close()

	// reader := bufio.NewReader(file)
	// for {
	// 	str, err := reader.ReadString('\n')
	// 	// 读到文件末尾了
	// 	if err == io.EOF {
	// 		break
	// 	}
	// 	fmt.Print(str)

	// }

	// content, err := os.ReadFile("test.txt")
	// if err != nil {
	// 	fmt.Println("文件读取失败：", err)
	// }
	// fmt.Printf("%v", string(content))

	// file, err := os.OpenFile("aa.txt", os.O_APPEND|os.O_WRONLY, 0666)
	// if err != nil {
	// 	fmt.Println("文件打开失败：", err)
	// }
	// defer file.Close()
	// str := "hello world2"
	// writer := bufio.NewWriter(file)
	// for i := 0; i < 5; i++ {
	// 	writer.WriteString(str + "\n")
	// }
	// // 写入缓存后还要落盘才行
	// writer.Flush()

	// content, err := ioutil.ReadFile("test.txt")
	// if err != nil {
	// 	fmt.Println("文件读取失败：", err)
	// 	return
	// }

	// err = ioutil.WriteFile("aa.txt", content, 0666)
	// if err != nil {
	// 	fmt.Println("文件写入失败：", err)
	// 	return
	// }

	// srcFile, err := os.Open("test.txt")
	// defer srcFile.Close()
	// if err != nil {
	// 	fmt.Println("文件打开失败：", err)
	// 	return
	// }

	// reader := bufio.NewReader(srcFile)

	// destFile, err := os.OpenFile("test-copy.txt", os.O_CREATE|os.O_WRONLY, 0666)
	// writer := bufio.NewWriter(destFile)
	// defer destFile.Close()

	// written, err := io.Copy(writer, reader)
	// if err != nil {
	// 	fmt.Println("文件写入失败：", err)
	// 	return
	// }
	// fmt.Println("文件复制成功，已复制：", written, "字节")

	// file, err := os.Open("test.txt")
	// defer file.Close()
	// if err != nil {
	// 	fmt.Println("文件打开失败：", err)
	// 	return
	// }
	// var count CharCount
	// reader := bufio.NewReader(file)
	// for {
	// 	str, err := reader.ReadString('\n')
	// 	if err == io.EOF {
	// 		break
	// 	}
	// 	// count.ChCount += utf8.RuneCountInString(str)
	// 	for _, v := range str {
	// 		switch {
	// 		case v == ' ' || v == '\t':
	// 			count.SpaceCount++
	// 		case v >= '0' && v <= '9':
	// 			count.NumCount++
	// 		case v >= 'a' && v <= 'z' || v >= 'A' && v <= 'Z':
	// 			count.ChCount++
	// 		default:
	// 			// 其中 /r/n 三行是6个
	// 			fmt.Printf("%c", v)
	// 			count.OtherCount++
	// 		}
	// 	}
	// }

	// fmt.Println(count)

	// monster := Monster{
	// 	Name:     "牛魔王",
	// 	Age:      500,
	// 	Birthday: "2020-01-01",
	// 	Sal:      5000.0,
	// 	Skill:    "芭蕾",
	// }
	// data, err := json.Marshal(&monster)
	// if err != nil {
	// 	fmt.Println("json序列化失败：", err)
	// 	return
	// }
	// fmt.Println(string(data))

	// var a map[string]interface{}
	// a = make(map[string]interface{})
	// a["name"] = "牛魔王"
	// a["age"] = 500
	// a["birthday"] = "2020-01-01"
	// a["sal"] = 5000.0
	// a["skill"] = "芭蕾"
	// data2, err := json.Marshal(a)
	// if err != nil {
	// 	fmt.Println("json序列化失败：", err)
	// 	return
	// }
	// fmt.Println(string(data2))

	// var slice []map[string]interface{}
	// var m1 = make(map[string]interface{})
	// m1["name"] = "牛魔王"
	// m1["age"] = 500
	// m1["birthday"] = "2020-01-01"
	// m1["sal"] = 5000.0
	// m1["skill"] = "芭蕾"
	// slice = append(slice, m1)
	// var m2 = make(map[string]interface{})
	// m2["name"] = "牛魔王2"
	// m2["age"] = 500
	// m2["birthday"] = "2020-01-01"
	// m2["sal"] = 5000.0
	// m2["skill"] = "芭蕾"
	// slice = append(slice, m2)
	// data3, err := json.Marshal(slice)
	// if err != nil {
	// 	fmt.Println("json序列化失败：", err)
	// 	return
	// }
	// fmt.Println(string(data3))

	// var num1 float64 = 3.14
	// data4, err := json.Marshal(num1)
	// if err != nil {
	// 	fmt.Println("json序列化失败：", err)
	// 	return
	// }
	// fmt.Println(string(data4))

	// str := `{"age":500,"birthday":"2020-01-01","name":"牛魔王","sal":5000,"skill":"芭蕾"}`
	// var monster Monster
	// err := json.Unmarshal([]byte(str), &monster)
	// if err != nil {
	// 	fmt.Println("json反序列化失败：", err)
	// 	return
	// }
	// fmt.Println(monster)

	// go test11()
	// for i := 0; i < 10; i++ {
	// 	fmt.Println("hello, golang, i = ", i)
	// 	time.Sleep(time.Second)
	// }

	// 查看cpu核数
	// cpuNmum := runtime.NumCPU()
	// fmt.Println("cpuNmum = ", cpuNmum)

	// 设置使用多少个cpu
	// runtime.GOMAXPROCS(cpuNmum)

	// var i int64 = 1
	// for ; i <= 50; i++ {
	// 	go calcal(i)
	// }

	// time.Sleep(time.Second * 5)
	// lock.Lock()
	// for i, v := range myMap {
	// 	fmt.Printf("map[%d]=%d\n", i, v)
	// }
	// lock.Unlock()

	// var intChan chan int
	// intChan = make(chan int, 3)
	// fmt.Println(intChan)

	// // 向管道写入数据
	// intChan <- 10
	// num := 211
	// intChan <- num

	// fmt.Println(len(intChan), cap(intChan))

	// // 从管道中读取数据
	// var num2 int
	// num2 = <-intChan
	// fmt.Println(len(intChan), cap(intChan), num2)

	// allChan := make(chan interface{}, 10)
	// allChan <- 10
	// allChan <- "hello golang"
	// allChan <- Cat{"tom", 10}

	// <-allChan
	// <-allChan
	// newCat := <-allChan
	// fmt.Printf("type is %T, value is %v\n", newCat, newCat)
	// fmt.Println(newCat.(Cat).Name)

	// myChan := make(chan Person, 10)
	// for i := 0; i < 10; i++ {
	// 	num := rand.Intn(100)
	// 	myChan <- Person{Name: "tom" + strconv.FormatInt(int64(i+1), 10), Age: num, Address: "beijing"}
	// }
	// close(myChan)
	// for v := range myChan {
	// 	person := v
	// 	fmt.Println(person.Name, person.Age, person.Address)
	// }

	// intChan := make(chan int, 10)
	// exitChan := make(chan bool, 1)

	// go writeData(intChan)
	// go readData(intChan, exitChan)
	// <-exitChan

	// intChan := make(chan int, 1000)
	// primeChan := make(chan int, 2000)
	// exitChan := make(chan bool, 20)

	// start := time.Now().Unix()
	// go putNum(intChan)
	// for i := 0; i < 20; i++ {
	// 	go prime(intChan, primeChan, exitChan)
	// }

	// go func() {
	// 	for i := 0; i < 20; i++ {
	// 		<-exitChan
	// 	}
	// 	end := time.Now().Unix()
	// 	fmt.Println("使用协程耗时=", end-start)

	// 	close(primeChan)
	// }()

	// for {
	// 	_, ok := <-primeChan
	// 	if !ok {
	// 		break
	// 	}
	// 	// fmt.Println("素数=", res)
	// }
	// fmt.Println("main goroutine over")

	// intChan := make(chan int, 10)
	// for i := 0; i < 10; i++ {
	// 	intChan <- i
	// }
	// stringChan := make(chan string, 5)
	// for i := 0; i < 5; i++ {
	// 	stringChan <- "hello golang" + strconv.FormatInt(int64(i+1), 10)
	// }

	// for {
	// 	select {
	// 	case v := <-intChan:
	// 		fmt.Println("读取的数据为：", v)
	// 	case v := <-stringChan:
	// 		fmt.Println("从stringChan读取数据为：", v)
	// 	default:
	// 		fmt.Println("都取不到，拜拜，加入自己的逻辑处理")
	// 		return
	// 	}
	// }

	// go sayHello()
	// go testS()
	// time.Sleep(time.Second * 10)

	// var num int = 100
	// reflectTest01(num)

	// stu := Student{Name: "tom", Age: 18}
	// reflectTest02(stu)

	// const (
	// 	a    = iota
	// 	b    = iota
	// 	c, d = iota, iota
	// )
	// fmt.Println(a, b, c, d)

	// var num int = 11
	// reflectTest03(&num)
	// fmt.Println("num=", num)

	var a MM = MM{
		Name:  "牛魔王",
		Age:   500,
		Score: 100.0,
	}
	TestStruct(a)

}

type MM struct {
	Name  string `json:"name"`
	Age   int    `json:"monster_age"`
	Score float32
	Sex   string
}

func (s MM) Print() {
	fmt.Println("--- start ---")
	fmt.Println(s)
	fmt.Println("--- end ---")
}

func (s MM) GetSum(n1, n2 int) int {
	return n1 + n2
}

func (s MM) Set(name string, age int, score float32, sex string) {
	s.Name = name
	s.Age = age
	s.Score = score
	s.Sex = sex
}

func TestStruct(a interface{}) {
	// 获取 reflect.Type 类型
	typ := reflect.TypeOf(a)
	// 获取 reflect.Value 类型
	val := reflect.ValueOf(a)
	// 获取变量的类别
	kd := val.Kind()
	// 如果传入的不是结构体，我就不玩了
	if kd != reflect.Struct {
		fmt.Println("传入的参数必须是结构体")
		return
	}
	// 获取到该结构体有几个字段
	num := val.NumField()
	fmt.Println("结构体的字段数量：", num)
	// 遍历结构体的字段
	for i := 0; i < num; i++ {
		fmt.Printf("第%d个字段，值是%v\n", i, val.Field(i))
		tagVal := typ.Field(i).Tag.Get("json")
		// 如果该字段有tag标签就显示
		if tagVal != "" {
			fmt.Printf("tag是%s\n", tagVal)
		}
	}
	// 获取到该结构体有多少个方法
	numOfMethod := val.NumMethod()
	fmt.Println("结构体的方法数量：", numOfMethod)
	// 方法的顺序跟编写的顺序无关，跟方法名的排序有关（ASCII码）
	val.Method(1).Call(nil)

	// 调用结构体的第1个方法 Method(0)
	var params []reflect.Value
	params = append(params, reflect.ValueOf(10))
	params = append(params, reflect.ValueOf(40))
	// 传入的是 []reflect.Value 切片，返回的结果也是
	res := val.Method(0).Call(params)
	fmt.Println("res=", res[0].Int())
}

/* ---------------------------------------- */

func reflectTest03(b interface{}) {
	rVal := reflect.ValueOf(b)
	// 类别是 ptr，指针
	fmt.Println("rVal kind=", rVal.Kind())
	// 需要先拿到指针指向的元素，再赋值
	rVal.Elem().SetInt(100)
}

type Student struct {
	Name string
	Age  int
}

func reflectTest02(b any) {
	rType := reflect.TypeOf(b)
	fmt.Println(rType, rType.Name())
	rVal := reflect.ValueOf(b)

	kind1 := rType.Kind()
	kind2 := rVal.Kind()
	fmt.Println("kind1=", kind1, "kind2=", kind2)

	iV := rVal.Interface()
	fmt.Printf("iV=%v, iV Type=%T \n", iV, iV)
	stu, ok := iV.(Student)
	if ok {
		fmt.Println("stu.Name=", stu.Name)
	}
}

func reflectTest01(b interface{}) {
	rType := reflect.TypeOf(b)
	fmt.Println(rType, rType.Name())
	rVal := reflect.ValueOf(b)
	fmt.Println(rVal, rVal.Int())

	iV := rVal.Interface()
	num2 := iV.(int)
	fmt.Println("num2=", num2)
}

func sayHello() {
	for i := 0; i < 10; i++ {
		fmt.Println("hello, golang, i = ", i)
		time.Sleep(time.Second)
	}
}

func testS() {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("test发生错误，recover err = ", err)
		}
	}()

	var myMap map[int]string
	myMap[0] = "tom"
}

func prime(intChan chan int, primeChan chan int, exitChan chan bool) {
	for {
		// time.Sleep(time.Millisecond * 10)
		num, ok := <-intChan
		if !ok {
			break
		}
		flag := true
		for i := 2; i < num; i++ {
			if num%i == 0 {
				flag = false
				break
			}
		}
		if flag {
			primeChan <- num
		}
	}
	fmt.Println("有一个primeNum 协程因为取不到数据退出啦")
	exitChan <- true
}

func putNum(intChan chan int) {
	for i := 0; i < 200000; i++ {
		intChan <- i
	}
	close(intChan)
}

func writeData(intChan chan int) {
	for i := 0; i < 50; i++ {
		intChan <- i
		fmt.Println("写入数据：", i)
	}
	close(intChan)
}

func readData(intChan chan int, exitChan chan bool) {
	for {
		v, ok := <-intChan
		if !ok {
			fmt.Println("管道已关闭")
			break
		}
		fmt.Println("从管道中读到的数据是：", v)
	}
	exitChan <- true
	close(exitChan)
}

type Person struct {
	Name    string
	Age     int
	Address string
}

type Cat struct {
	Name string
	Age  int
}

var (
	myMap = make(map[int64]int64)
	lock  sync.Mutex
)

func calcal(n int64) {
	fmt.Println("正在执行", n, "阶乘的计算")
	var res int64 = 1
	var i int64 = 1
	for ; i <= n; i++ {
		res *= i
	}

	lock.Lock()
	myMap[n] = res
	lock.Unlock()
}

func test11() {
	for i := 0; i < 10; i++ {
		fmt.Println("hello, world, i = ", i)
		time.Sleep(time.Second)
	}
}

type Monster struct {
	Name     string  `json:"name"`
	Age      int     `json:"age"`
	Birthday string  `json:"birthday"`
	Sal      float64 `json:"sal"`
	Skill    string  `json:"skill"`
}

type CharCount struct {
	ChCount    int
	NumCount   int
	SpaceCount int
	OtherCount int
}

func PathExists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return false, err
}

type Usb interface {
	Start()
	Stop()
}

type Phone struct {
}

func (phone Phone) Start() {
	fmt.Println("手机开始工作")
}

func (phone Phone) Stop() {
	fmt.Println("手机停止工作")
}

type Camera struct {
}

func (camera Camera) Start() {
	fmt.Println("相机开始工作")
}

func (camera Camera) Stop() {
	fmt.Println("相机停止工作")
}

type Computer struct {
}

func (computer Computer) BindingUsb(usb Usb) {
	usb.Start()
	usb.Stop()
}

type Account struct {
	AccountNo string
	Pwd       string
	Balance   float64
}

func (account *Account) Deposite(money float64, pwd string) {
	if account.Pwd == pwd {
		account.Balance += money
		fmt.Println("存款成功，余额为：", account.Balance)
	} else {
		fmt.Println("密码错误")
	}
}

type A struct {
	Num int
}

func (a A) test() {
	fmt.Println("test")
}

func BubbleSort(arr *[5]int) {
	fmt.Println("排序前：", *arr)
	for i := 0; i < len(*arr)-1; i++ {
		for j := 0; j < len(*arr)-1-i; j++ {
			if (*arr)[j] > (*arr)[j+1] {
				(*arr)[j], (*arr)[j+1] = (*arr)[j+1], (*arr)[j]
			}
		}
		fmt.Printf("第 %v 轮排序：%v\n", i+1, *arr)
	}
}

func BinaryFind(arr *[6]int, findVal int, leftIndex int, rightIndex int) {
	if leftIndex > rightIndex {
		fmt.Println("没有找到")
		return
	}

	middle := (leftIndex + rightIndex) / 2
	if (*arr)[middle] > findVal {
		fmt.Printf("左边界：%v，右边界：%v\n", leftIndex, middle-1)
		BinaryFind(arr, findVal, leftIndex, middle-1)
	} else if (*arr)[middle] < findVal {
		fmt.Printf("左边界：%v，右边界：%v\n", leftIndex, middle-1)
		BinaryFind(arr, findVal, middle+1, rightIndex)
	} else {
		fmt.Println("找到，索引是：", middle)
	}
}

func testException() {
	defer func() {
		err := recover()
		if err != nil {
			// 说明捕获到了异常
			fmt.Println("err =", err)
		}
	}()
	x1 := 10
	x2 := 0
	fmt.Println(x1 / x2)
}

func sum(n1 int, n2 int) int {
	defer fmt.Println("ok n1=", n1)
	defer fmt.Println("ok n2=", n2)

	// 增加一句话，但是defer上的输出不变
	n1++
	n2++

	res := n1 + n2
	fmt.Println("ok3 res=", res)
	return res
}

func makeSuffix(suffix string) func(string) string {
	return func(name string) string {
		if !strings.HasSuffix(name, suffix) {
			return name + suffix
		}
		return name
	}
}

func AddUpper() func(int) int {
	var n int = 10
	return func(x int) int {
		n = n + x
		return n
	}
}

var Func1 = func(n1 int, n2 int) int {
	return n1 + n2
}

func calc(a int, b int) (sum int, sub int) {
	sum = a + b
	sub = a - b
	return
}

func fib(n int) int {
	if n <= 2 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}

type myfib func(int) int

func test_fib(funcvar myfib, num1 int, num2 int) {
	fmt.Println(funcvar(num1) + funcvar(num2))
}

func test(n int) {
	if n > 2 {
		n--
		test(n)
	}
	fmt.Println("n =", n)
}

func test2(n int) {
	if n > 2 {
		n--
		test2(n)
	} else {
		fmt.Println("n =", n)
	}
}
