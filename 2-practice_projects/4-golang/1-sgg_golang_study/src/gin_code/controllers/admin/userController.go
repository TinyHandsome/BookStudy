package admin

import (
	"fmt"
	"net/http"
	"path"

	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
)

type UserController struct {
}

func (con UserController) Index(ctx *gin.Context) {
	ctx.SetCookie("username", "zhangsan", 3600, "/", "localhost", false, true)
	session := sessions.Default(ctx)
	session.Options(sessions.Options{MaxAge: 3600 * 6})
	session.Set("key2", "kkkkkg")
	session.Save()

	fmt.Println("loading index")
	username, _ := ctx.Get("username")
	v, _ := username.(string)
	fmt.Println("finish loading")
	ctx.String(200, "首页a--%v", v)
}

func (con UserController) News(ctx *gin.Context) {
	username, _ := ctx.Cookie("username")
	session := sessions.Default(ctx)
	key1 := session.Get("key2")

	ctx.String(200, "新闻a--++ "+username+"--------------"+key1.(string))
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
