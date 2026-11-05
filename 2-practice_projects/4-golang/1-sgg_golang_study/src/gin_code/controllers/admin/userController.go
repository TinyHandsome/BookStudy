package admin

import (
	"fmt"
	"net/http"
	"path"

	"github.com/gin-gonic/gin"
)

type UserController struct {
}

func (con UserController) Index(ctx *gin.Context) {
	ctx.SetCookie("username", "zhangsan", 3600, "/", "localhost", false, true)

	fmt.Println("loading index")
	username, _ := ctx.Get("username")
	v, _ := username.(string)
	fmt.Println("finish loading")
	ctx.String(200, "首页a--%v", v)
}

func (con UserController) News(ctx *gin.Context) {
	username, _ := ctx.Cookie("username")
	ctx.String(200, "新闻a--++ "+username)
}

func (con UserController) Upload(ctx *gin.Context) {
	// username := ctx.PostForm("username")
	// file, err := ctx.FormFile("file")

	// dst := path.Join("./static/upload", file.Filename)
	// if err == nil {
	// 	ctx.SaveUploadedFile(file, dst)
	// }

	form, _ := ctx.MultipartForm()
	files := form.File["files"]
	for _, file := range files {
		fmt.Println(file.Filename)
		dst2 := path.Join("./static/upload", file.Filename)
		ctx.SaveUploadedFile(file, dst2)
	}

	ctx.JSON(http.StatusOK, gin.H{
		"success": true,
	})
}
