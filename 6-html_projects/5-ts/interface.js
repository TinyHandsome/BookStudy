var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var obj1;
obj1 = {
    name: "1",
    age: 1
};
var obj2;
obj2 = {
    name: "2"
};
var obj3;
obj3 = {
    name: "3",
    age: "12",
    sex: "male",
    isMarry: true
};
// 数组
var arr = [1, 2, 3];
var arr2 = ["1", "2", "3"];
var arr3 = ["1", 1, true];
var arrType = [1, 2, 3];
var arrType2 = ["1", "2", "3"];
var arrType3 = [1, "2", true];
var arrType4 = [1, 2, 3];
var arrType5 = [{ name: "1", age: 1 }, { name: "2", age: 2 }];
var arrType6 = [{ name: "1", age: 1 }, { name: "2", age: 2 }];
var arrType7 = [{ name: "1", age: 1 }, { name: "2", age: 2 }];
// 声明式类型的函数
function f(name, age) {
    return age;
}
var ageNum = f("zhangsan", 18);
// - 函数参数不确定
function f2(name, age, sex) {
    return age;
}
// - 函数参数的默认值
function f3(name, age) {
    if (name === void 0) { name = "张三"; }
    if (age === void 0) { age = 18; }
    return age;
}
// 表达式类型的函数
var f4 = function (name, age) {
    return age;
};
// - 约束方案1
var f5 = function (name, age) {
    return age;
};
var f6 = function (name, age) {
    return age;
};
function getValue(value) {
    return value;
}
var a = getValue(1);
// let test: number | string = "10"
// test = 20
// console.log(test.length);
// 类型断言，不是强制类型转换
function getAssert(name) {
    return name.length, name.length;
}
var str = 10;
str = "10";
var objj = { name: "张三" };
var objj2 = { age: 123 };
var objj3 = { name: "asd", age: 11 };
function getSex(s) {
    return s;
}
getSex("男");
// 枚举类型会被编译成一个双向映射的对象
var Days;
(function (Days) {
    // 这里默认是0，设置成其他值时会基于该值进行累加
    Days[Days["Sun"] = 0] = "Sun";
    Days[Days["Mon"] = 1] = "Mon";
    Days[Days["Tue"] = 2] = "Tue";
    Days[Days["Wed"] = 3] = "Wed";
    Days[Days["Thu"] = 4] = "Thu";
    Days[Days["Fri"] = 5] = "Fri";
    Days[Days["Sat"] = 6] = "Sat";
})(Days || (Days = {}));
console.log(Days.Fri); // 5
console.log(Days[0]); // Sun
var Person = /** @class */ (function () {
    function Person() {
        this.name = "张三";
        this.age = 18;
    }
    Person.prototype.say = function () {
        console.log("我的名字是" + this.name + ", " + this.age);
    };
    Person.test = function () {
        console.log("test");
    };
    return Person;
}());
var p = new Person();
// p.say()
// console.log(p.name);
var Child = /** @class */ (function (_super) {
    __extends(Child, _super);
    function Child() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Child.prototype.callParent = function () {
        _super.prototype.say.call(this);
    };
    return Child;
}(Person));
var c = new Child();
c.callParent();
console.log(c.age);
Child.test();
function createArray(length, value) {
    var arr = [];
    for (var index = 0; index < length; index++) {
        arr[index] = value;
    }
    return arr;
}
var strArr = createArray(3, '1');
console.log(strArr);
