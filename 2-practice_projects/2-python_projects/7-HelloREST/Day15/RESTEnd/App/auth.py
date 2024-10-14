from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from App.models import UserModel


class LoginAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.query_params.get('token')
            user_id = cache.get(token)
            user = UserModel.objects.get(pk=user_id)
            return user, token
        except Exception as e:
            return


