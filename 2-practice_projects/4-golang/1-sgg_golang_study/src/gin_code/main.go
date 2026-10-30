package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Article struct {
	Title   string `json:"title"`
	Desc    string `json:"desc"`
	Content string `json:"content"`
}

func main() {
	// 创建一个默认的路由引擎
	r := gin.Default()
	// 加载模板
	r.LoadHTMLGlob("templates/*")
	// 配置路由
	r.GET("/", func(c *gin.Context) {
		c.String(200, "值：%v", "你好gin")
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
	r.GET("/news", func(c *gin.Context) {
		// c.String(200, "我是新闻页面111")
		c.HTML(http.StatusOK, "new.html", gin.H{
			"title": "我是后台数据",
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
	r.Run()
}
