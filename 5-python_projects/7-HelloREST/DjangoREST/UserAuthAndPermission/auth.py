from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from UserAuthAndPermission.models import UserModel


class UserAuth(BaseAuthentication):
    def authenticate(self, request):
        if request.method == 'GET':
            token = request.query_params.get('token')

            try:
                u_id = cache.get(token)
                user = UserModel.objects.get(pk=u_id)
                return user, token
            except:
                return
