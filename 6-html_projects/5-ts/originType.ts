var str: string = "hello";
var num: number = 1;
var flag: boolean = true;
var un: undefined = undefined;
var nul: null = null;

str = null;

var callBack = function (): void {
    // return 10;
};

// var num2: void = 3;

var num: any = 1;
num = true;


// 给变量赋值初始值的时候，如果没有指定类型，就会根据初始值倒推类型
var b = 1;
b = '2'

// 没有给b赋初始值，就是any，var b: any
var bb;
bb = 1
bb = '2'

// 联合类型
var muchtype: string | number = "hello"
muchtype = 10
console.log(muchtype.toString());