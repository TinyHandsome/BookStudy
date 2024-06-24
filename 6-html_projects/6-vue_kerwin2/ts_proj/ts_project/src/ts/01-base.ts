var myname: string = "kerwin"
myname = "100"

var aa: boolean = true

var mylist: number[] = [1, 2, 3]
mylist.push(4)

var a: string | number = 12
a = "12"

var b: (string | number)[] = [1, "2"]
b.push("12")

var c: any = [12]
c = 1

// 第二种风格
var d: Array<string> = ["aaa", "bbb"]
var e: Array<string | number> = ["aaa", 12]
var f: Array<any> = ["aaa", "bbb", 123, true]

// 对象
var obj: InterObj = {
    name: "kewin",
    age: 100,
    d: {}
}
// 定义接口
interface InterObj {
    name: string,
    age: number,
    // 可选属性
    location?: string,
    // 未知属性
    [propName: string]: any
}

function test(a: number, b: number):number {
    return a + b
}

export default {}