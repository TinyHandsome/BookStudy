package models

type User struct {
	Id       int
	Username string
	Age      int
	Email    string
	AddTime  int
}

func (user User) TableName() string {
	return "users"
}
