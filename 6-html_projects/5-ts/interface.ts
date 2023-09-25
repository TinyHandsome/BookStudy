// 定义接口 强约束，属性加?：实现可选特征，通过增加[]属性实现不定量属性，这里只能指定any；readonly：只读，不能再赋值
interface Instate {
    readonly name: string
    age?: number | string,
    [propName: string]: any
}

var obj1: Instate
obj1 = {
    name: "1",
    age: 1
}
var obj2: Instate
obj2 = {
    name: "2"
}

var obj3: Instate
obj3 = {
    name: "3",
    age: "12",
    sex: "male",
    isMarry: true
}


// 数组
var arr: number[] = [1, 2, 3]
var arr2: string[] = ["1", "2", "3"]
var arr3: any[] = ["1", 1, true]

var arrType: Array<number> = [1, 2, 3]
var arrType2: Array<string> = ["1", "2", "3"]
var arrType3: Array<any> = [1, "2", true]

interface IArray {
    [index: number]: number
}
var arrType4: IArray = [1, 2, 3]

interface Istate {
    name: string,
    age: number
}
interface IArr {
    [index: number]: Istate
}
var arrType5: IArr = [{ name: "1", age: 1 }, { name: "2", age: 2 }]
var arrType6: Array<Istate> = [{ name: "1", age: 1 }, { name: "2", age: 2 }]
var arrType7: Istate[] = [{ name: "1", age: 1 }, { name: "2", age: 2 }]

// 声明式类型的函数
function f(name: string, age: number): number {
    return age
}
var ageNum: number = f("zhangsan", 18)
// - 函数参数不确定
function f2(name: string, age: number, sex?: string): number {
    return age
}
// - 函数参数的默认值
function f3(name: string = "张三", age: number = 18): number {
    return age
}

// 表达式类型的函数
var f4 = function (name: string, age: number): number {
    return age
}
// - 约束方案1
var f5: (name: string, age: number) => number = function (name: string, age: number): number {
    return age
}
// - 约束方案2
interface i6 {
    (name: string, age: number): number
}
var f6: i6 = function (name: string, age: number): number {
    return age
}

// 重载的方式：联合类型的函数
function getValue(value: number): number;
function getValue(value: string): string;
function getValue(value: string | number): string | number {
    return value
}
let a: number = getValue(1)

// let test: number | string = "10"
// test = 20
// console.log(test.length);

// 类型断言，不是强制类型转换
function getAssert(name: string | number) {
    return (<string>name).length, (name as string).length
}

type strType = string | number;
var str: strType = 10
str = "10"

interface mt1 {
    name: string
}
interface mt2 {
    age: number
}
type mt = mt1 | mt2
var objj: mt = { name: "张三" }
var objj2: mt = { age: 123 }
var objj3: mt = { name: "asd", age: 11 }

// 限制字符串的选择
type sexx = "男" | "女"
function getSex(s: sexx): string {
    return s
}
getSex("男")

// 枚举类型会被编译成一个双向映射的对象
enum Days {
    // 这里默认是0，设置成其他值时会基于该值进行累加
    Sun = 0,
    Mon,
    Tue,
    Wed,
    Thu,
    Fri,
    Sat
}
console.log(Days.Fri); // 5
console.log(Days[0]); // Sun

class Person {
    private name = "张三"
    age = 18
    protected say() {
        console.log("我的名字是" + this.name + ", " + this.age);
    }
    static test() {
        console.log("test");
    }
}
var p = new Person()
// p.say()
// console.log(p.name);
class Child extends Person {
    callParent() {
        super.say()
    }
}
var c = new Child()
c.callParent()
console.log(c.age);

Child.test()

function createArray<T>(length: number, value: T): Array<T> {
    let arr = []
    for (let index = 0; index < length; index++) {
        arr[index] = value
    }
    return arr
}

var strArr: string[] = createArray<string>(3, '1')
console.log(strArr);

// 接口中使用泛型
interface Icreate {
    <T>(name: string, value: T): Array<T>
}
let func: Icreate;
func = function <T>(name: string, value: T): Array<T> {
    return []
}
var strArr: string[] = func("zhangsan", "12")