// Code scaffolded by goctl. Safe to edit.
// goctl 1.11.0

package logic

import (
	"context"

	"gozero_code/internal/svc"
	"gozero_code/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type Gozero_codeLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewGozero_codeLogic(ctx context.Context, svcCtx *svc.ServiceContext) *Gozero_codeLogic {
	return &Gozero_codeLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *Gozero_codeLogic) Gozero_code(req *types.Request) (resp *types.Response, err error) {
	// todo: add your logic here and delete this line
	resp = &types.Response{
		Message: "你好 " + req.Name + l.svcCtx.DataSource,
	}
	return
}
