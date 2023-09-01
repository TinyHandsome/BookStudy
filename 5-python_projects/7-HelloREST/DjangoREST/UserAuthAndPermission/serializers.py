from rest_framework import serializers

from UserAuthAndPermission.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('url', 'id', 'u_name', 'u_password', 'is_super')