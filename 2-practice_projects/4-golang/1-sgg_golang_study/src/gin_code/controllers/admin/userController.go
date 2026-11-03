package admin

import "github.com/gin-gonic/gin"

type UserController struct {
}

func (con UserController) Index(ctx *gin.Context) {
	ctx.String(200, "首页a")
}

func (con UserController) News(ctx *gin.Context) {
	ctx.String(200, "新闻a--++")
}
