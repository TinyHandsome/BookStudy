// Code scaffolded by goctl. Safe to edit.
// goctl 1.11.0

package handler

import (
	"net/http"

	"github.com/zeromicro/go-zero/rest/httpx"
	"gozero_code/internal/logic"
	"gozero_code/internal/svc"
	"gozero_code/internal/types"
)

func Gozero_codeHandler(svcCtx *svc.ServiceContext) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req types.Request
		if err := httpx.Parse(r, &req); err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
			return
		}

		l := logic.NewGozero_codeLogic(r.Context(), svcCtx)
		resp, err := l.Gozero_code(&req)
		if err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
		} else {
			httpx.OkJsonCtx(r.Context(), w, resp)
		}
	}
}
