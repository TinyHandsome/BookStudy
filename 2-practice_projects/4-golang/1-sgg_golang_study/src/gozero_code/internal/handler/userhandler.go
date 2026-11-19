// Code scaffolded by goctl. Safe to edit.
// goctl 1.11.0

package handler

import (
	"net/http"

	"github.com/zeromicro/go-zero/rest/httpx"
	"gozero_code/internal/logic"
	"gozero_code/internal/svc"
)

func UserHandler(svcCtx *svc.ServiceContext) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		l := logic.NewUserLogic(r.Context(), svcCtx)
		resp, err := l.User()
		if err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
		} else {
			httpx.OkJsonCtx(r.Context(), w, resp)
		}
	}
}
