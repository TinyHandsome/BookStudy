package main

import (
	"fmt"

	"github.com/gomodule/redigo/redis"
)

var pool *redis.Pool

func init() {
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
}

func main() {
	conn := pool.Get()
	defer conn.Close()

	_, err := conn.Do("SET", "name", "张三")
	if err != nil {
		fmt.Println("set failed, err:", err)
		return
	}

	r, err := redis.String(conn.Do("GET", "name"))
	if err != nil {
		fmt.Println("get failed, err:", err)
	}
	fmt.Println("name:", r)
}
