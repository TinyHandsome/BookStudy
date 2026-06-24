package main

import (
	"fmt"

	"github.com/gomodule/redigo/redis"
)

func main() {
	// conn, err := redis.Dial("tcp", "127.0.0.1:6379")
	// if err != nil {
	// 	fmt.Println("拨号失败", err)
	// 	return
	// }
	// defer conn.Close()

	var pool *redis.Pool
	pool = &redis.Pool{
		// 最大空闲链接数
		MaxIdle: 8,
		// 表示和数据的最大连接数，0表示没有限制
		MaxActive: 0,
		// 最大空闲时间
		IdleTimeout: 300,
		// 初始化连接池，链接哪个ip的redis
		Dial: func() (redis.Conn, error) {
			return redis.Dial("tcp", "127.0.0.1:6379")
		},
	}
	conn := pool.Get()
	defer pool.Close()

	_, err := conn.Do("SELECT", 1)
	if err != nil {
		fmt.Println("切换库失败：", err)
		return
	}

	_, err = conn.Do("Set", "name", "tom皮卡丘")
	if err != nil {
		fmt.Println("Set报错：", err)
		return
	}

	_, err = conn.Do("HSet", "user01", "name", "hash名字", "age", 18)
	if err != nil {
		fmt.Println("HSet报错：", err)
		return
	}

	r, err := redis.String(conn.Do("Get", "name"))
	if err != nil {
		fmt.Println("Get报错：", err)
		return
	}
	fmt.Println("name is: ", r)

	name, err := redis.String(conn.Do("HGet", "user01", "name"))
	if err != nil {
		fmt.Println("HGet报错：", err)
		return
	}
	age, err := redis.Int(conn.Do("HGet", "user01", "age"))
	if err != nil {
		fmt.Println("HGet报错：", err)
		return
	}
	fmt.Println("user01 name is: ", name, "age is: ", age)

	fmt.Println("操作成功")
}
