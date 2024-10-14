import uuid

from django.core.cache import cache
from rest_framework import status, exceptions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from DjangoREST.settings import SUPER_USERS
from UserAuthAndPermission.auth import UserAuth
from UserAuthAndPermission.constants import HTTP_ACTION_REGISTER, HTTP_ACTION_LOGIN
from UserAuthAndPermission.models import UserModel
from UserAuthAndPermission.permissions import IsSuperUser
from UserAuthAndPermission.serializers import UserSerializer


class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (UserAuth,)
    permission_classes = (IsSuperUser,)

    def get(self, request, *args, **kwargs):
        if isinstance(request.user, UserModel):
            return self.list(request, *args, **kwargs)
        else:
            print('获取失败')
            raise exceptions.NotAuthenticated

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')

        if action == HTTP_ACTION_REGISTER:
            return self.create(request, *args, **kwargs)
        elif action == HTTP_ACTION_LOGIN:
            u_name = request.data.get('u_name')
            u_password = request.data.get('u_password')
            try:
                user = UserModel.objects.get(u_name=u_name)
                if user.u_password == u_password:
                    token = uuid.uuid4().hex
                    # 设置token对应的是user的id
                    cache.set(token, user.id)
                    data = {
                        'msg': 'login success',
                        'status': 200,
                        'token': token
                    }
                    return Response(data)
                else:
                    raise exceptions.AuthenticationFailed
            except UserModel.DoesNotExist:
                raise exceptions.NotFound
        else:
            raise exceptions.ValidationError

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = serializer.data
        u_name = data.get('u_name')

        if u_name in SUPER_USERS:
            print('创建超级用户')
            u_id = data.get('id')
            user = UserModel.objects.get(pk=u_id)
            user.is_super = True
            user.save()
            data.update({'is_super': True})

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
