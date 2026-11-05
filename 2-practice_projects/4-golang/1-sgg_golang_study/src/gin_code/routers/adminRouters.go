package routers

import (
	"fmt"
	"gin_code/controllers/admin"
	"gin_code/middlewares"
	"time"

	"github.com/gin-gonic/gin"
)

func AdminRoutersInit(r *gin.Engine) {

	adminController := admin.UserController{}
	adminRouters := r.Group("/admin", middlewares.InitMiddleware)
	{
		adminRouters.GET("/", func(ctx *gin.Context) {
			start := time.Now().UnixNano()
			fmt.Println("我是中间件开始")
			ctx.Next()
			fmt.Println("我是中间件结束")
			end := time.Now().UnixNano()
			fmt.Println("last time: ", end-start)

			username, _ := ctx.Get("username")
			fmt.Println(username)

		}, adminController.Index)
		adminRouters.GET("/news", adminController.News)
		adminRouters.POST("/upload", adminController.Upload)
	}
}
