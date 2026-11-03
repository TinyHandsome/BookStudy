package routers

import (
	"gin_code/controllers/admin"

	"github.com/gin-gonic/gin"
)

func AdminRoutersInit(r *gin.Engine) {

	adminController := admin.UserController{}
	adminRouters := r.Group("/admin")
	{
		adminRouters.GET("/", adminController.Index)
		adminRouters.GET("/news", adminController.News)
	}
}
