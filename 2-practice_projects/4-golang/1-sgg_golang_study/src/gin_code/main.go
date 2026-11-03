package main

import (
	"encoding/xml"
	"fmt"
	"gin_code/routers"
	"net/http"
	"text/template"
	"time"

	"github.com/gin-gonic/gin"
)

type Article struct {
	Title   string `json:"title"`
	Desc    string `json:"desc"`
	Content string `json:"content"`
}

type UserInfo struct {
	Username string `json:"username" form:"username"`
	Password string `json:"password" form:"password"`
}
type Info struct {
	Title   string `json:"title" xml:"title"`
	Content string `json:"content" xml:"content"`
}

func UnixToTime(timestamp int) string {
	t := time.Unix(int64(timestamp), 0)
	return t.Format("2006-01-02 15:04:05")
}

func main() {
	// 创建一个默认的路由引擎
	r := gin.Default()
	// 注册模板函数
	r.SetFuncMap(template.FuncMap{
		"UnixToTime": UnixToTime,
	})
	// 加载模板
	r.LoadHTMLGlob("templates/**/*")
	// 配置静态文件服务
	r.Static("/static", "./static/")

	// 路由分组

	defaultRouters := r.Group("/v1")
	{
		defaultRouters.GET("/", func(ctx *gin.Context) {
			ctx.String(200, "首页")
		})
		defaultRouters.GET("/news", func(ctx *gin.Context) {
			ctx.String(200, "新闻")
		})
	}
	routers.AdminRoutersInit(r)

	// 配置路由
	r.GET("/", func(c *gin.Context) {
		uname := c.Query("username")
		age := c.DefaultQuery("age", "0")

		c.HTML(http.StatusOK, "default/index.html", gin.H{
			"title": "首页",
			"score": 89,
			"hobby": []string{"eat", "sleep", "coding"},
			"news": &Article{
				Title:   "皮卡丘",
				Content: "皮皮虾",
			},
			"date":     1629423555,
			"username": uname,
			"age":      age,
		})
	})
	r.POST("/user", func(ctx *gin.Context) {
		uname := ctx.DefaultPostForm("username", "test")
		pword := ctx.PostForm("password")
		ctx.JSON(http.StatusOK, gin.H{
			"username": uname,
			"password": pword,
		})
	})
	r.GET("/news", func(c *gin.Context) {
		// c.String(200, "我是新闻页面111")
		news := &Article{
			Title:   "新闻标题",
			Desc:    "我是描述",
			Content: "测试",
		}
		c.HTML(http.StatusOK, "default/news.html", gin.H{
			"title": "新闻页面",
			"news":  news,
		})
	})
	r.GET("/getuser", func(ctx *gin.Context) {
		user := &UserInfo{}
		if err := ctx.ShouldBind(&user); err == nil {
			fmt.Printf("%#v\n", user)
			ctx.JSON(http.StatusOK, user)
		} else {
			ctx.JSON(http.StatusOK, gin.H{
				"err": err.Error(),
			})
		}
	})
	r.POST("/getuser2", func(ctx *gin.Context) {
		user := &UserInfo{}
		if err := ctx.ShouldBind(&user); err == nil {
			fmt.Printf("%#v\n", user)
			ctx.JSON(http.StatusOK, user)
		} else {
			ctx.JSON(http.StatusOK, gin.H{
				"err": err.Error(),
			})
		}
	})
	r.POST("/xml2", func(ctx *gin.Context) {
		// ctx.ShouldBindBodyWithXML(obj any)
		info := &Info{}
		xmlSliceData, _ := ctx.GetRawData()
		fmt.Println(xmlSliceData)
		if err := xml.Unmarshal(xmlSliceData, &info); err == nil {
			ctx.JSON(http.StatusOK, info)
		} else {
			ctx.JSON(http.StatusBadRequest, gin.H{
				"err": err.Error(),
			})
		}
	})

	r.GET("/json", func(c *gin.Context) {
		c.JSON(http.StatusOK, map[string]any{
			"success": true,
			"msg":     "hi",
		})
	})
	r.GET("/json2", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"msg":     "hi2",
		})
	})
	r.GET("/json3", func(c *gin.Context) {
		a := &Article{
			Title:   "你好",
			Desc:    "我是描述",
			Content: "测试",
		}
		c.JSON(http.StatusOK, a)
	})
	// 跨域处理的请求，现在应该很少用这种方案了
	r.GET("/jsonp", func(c *gin.Context) {
		a := &Article{
			Title:   "你好",
			Desc:    "我是描述",
			Content: "测试",
		}
		c.JSONP(http.StatusOK, a)
	})
	r.GET("/xml", func(c *gin.Context) {
		c.XML(http.StatusOK, gin.H{
			"success": true,
			"msg":     "hi gin, xml",
		})
	})
	r.POST("/add", func(c *gin.Context) {
		c.String(200, "我是post请求，主要用于增加数据")
	})
	r.PUT("/edit", func(c *gin.Context) {
		c.String(200, "这是一个put请求，主要用于编辑数据")
	})
	r.DELETE("/delete", func(c *gin.Context) {
		c.String(http.StatusOK, "delete请求，主要用于删除数据")
	})

	// 动态路由传值
	r.GET("/list/:cid", func(ctx *gin.Context) {
		cid := ctx.Param("cid")
		ctx.String(200, "%v", cid)
	})

	r.Run()
}
