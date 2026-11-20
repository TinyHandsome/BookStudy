// Code scaffolded by goctl. Safe to edit.
// goctl 1.11.0

package logic

import (
	"context"

	"gozero_code/internal/svc"
	"gozero_code/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type UserLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewUserLogic(ctx context.Context, svcCtx *svc.ServiceContext) *UserLogic {
	return &UserLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *UserLogic) User() (resp *types.Response, err error) {
	resp = &types.Response{
		Message: "你好 用户 222",
	}

	return
}
