package model

import (
	"demo/chatroom/common/message"
	"encoding/json"
	"fmt"

	"github.com/gomodule/redigo/redis"
)

var (
	MyUserDao *UserDao
)

// 定义一个UserDao结构体
// 完成对USer结构体的各种操作
type UserDao struct {
	pool *redis.Pool
}

// 使用工厂模式，创建一个UserDao的实例
func NewUserDao(pool *redis.Pool) (userDao *UserDao) {
	userDao = &UserDao{
		pool: pool,
	}
	return
}

// 根据用户id返回一个User实例+err
func (this *UserDao) getUserById(id int) (user *User, err error) {
	// 通过给定的id去redis里查询用户
	conn := this.pool.Get()
	defer conn.Close()

	res, err := redis.String(conn.Do("HGet", "users", id))
	if err != nil {
		if err == redis.ErrNil {
			//表示在redis中没有找到对应的id
			err = ERROR_USER_NOTEXISTS
		}
		return
	}

	user = &User{}
	// 需要把res反序列化成User实例
	err = json.Unmarshal([]byte(res), user)
	if err != nil {
		fmt.Println("json.Unmarshal err=", err)
		return
	}
	return
}

// 完成登录的校验
func (this *UserDao) Login(userId int, userPwd string) (user *User, err error) {
	// 通过给定的id去redis里查询用户
	user, err = this.getUserById(userId)
	if err != nil {
		return
	}

	if user.UserPwd != userPwd {
		err = ERROR_USER_PWD
		return
	}

	return
}

func (this *UserDao) Register(user *message.User) (err error) {
	// 1.使用给定的id去redis中查询这个用户是否存在
	conn := this.pool.Get()
	defer conn.Close()

	_, err = this.getUserById(user.UserId)
	if err == nil {
		// 2.如果返回err为nil，说明在redis中已经存在这个用户
		err = ERROR_USER_EXISTS
		fmt.Println("用户已存在")
		return
	}

	// 3.准备一个user.json
	data, err := json.Marshal(user)
	if err != nil {
		fmt.Println("json.Marshal err:", err)
		return
	}

	_, err = conn.Do("HSet", "users", user.UserId, string(data))
	if err != nil {
		fmt.Println("保存注册用户错误：", err)
		return
	}
	return
}
