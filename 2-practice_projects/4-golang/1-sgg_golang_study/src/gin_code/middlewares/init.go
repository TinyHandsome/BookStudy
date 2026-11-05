package middlewares

import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
)

func InitMiddleware(ctx *gin.Context) {
	// 判断用户是否登录
	fmt.Println(time.Now())
	fmt.Println(ctx.Request.URL)

	ctx.Set("username", "张三")
}
