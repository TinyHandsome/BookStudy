from alipay import AliPay
from flask_restful import Resource

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_required
from App.settings import ALIPAY_APPID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY


class MovieOrderPayResource(Resource):

    @login_required
    def get(self, order_id):
        # 构建支付的客户端 AlipayClient
        alipay_client = AliPay(
            appid=ALIPAY_APPID,
            # 默认回调url
            app_notify_url=None,
            app_private_key_string=APP_PRIVATE_KEY,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
            alipay_public_key_string=ALIPAY_PUBLIC_KEY,
            # RSA or RSA2
            sign_type="RSA2",
            debug=False
        )
        # 使用Alipay进行支付的请求发起
        # 电脑网站支付
        subject = "苹果 iwatch7"
        order_string = alipay_client.api_alipay_trade_page_pay(
            out_trade_no='110000',
            total_amount=1000,
            subject=subject,
            return_url='',
            notify_url=''
        )

        # 手机网站支付
        # order_string = alipay_client.api_alipay_trade_wap_pay(
        #     out_trade_no='1100001',
        #     total_amount=1000,
        #     subject=subject,
        #     return_url='',
        #     notify_url=''
        # )

        # 客户端操作
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": {
                "pay_url": pay_url,
                "order_id": order_id
            }
        }

        return data
