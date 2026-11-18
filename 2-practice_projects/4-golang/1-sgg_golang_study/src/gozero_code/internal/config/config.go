// Code scaffolded by goctl. Safe to edit.
// goctl 1.11.0

package config

import "github.com/zeromicro/go-zero/rest"

type Config struct {
	rest.RestConf
	Mysql struct {
		DataSource string
	}
}
