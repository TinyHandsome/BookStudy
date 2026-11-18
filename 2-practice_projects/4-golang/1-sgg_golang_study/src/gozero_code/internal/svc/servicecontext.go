// Code scaffolded by goctl. Safe to edit.
// goctl 1.11.0

package svc

import (
	"gozero_code/internal/config"
)

type ServiceContext struct {
	Config     config.Config
	DataSource string
}

func NewServiceContext(c config.Config) *ServiceContext {
	return &ServiceContext{
		Config:     c,
		DataSource: c.Mysql.DataSource,
	}
}
