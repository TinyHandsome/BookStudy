package models

type User struct {
	Id       int    `json:"id"`
	Username string `json:"username"`
	Age      int    `json:"age"`
	Email    string `json:"email"`
	AddTime  int    `json:"add_time"`
}

func (user User) TableName() string {
	return "users"
}
