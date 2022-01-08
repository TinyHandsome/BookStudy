from rest_framework import serializers

from App.models import UserModel, Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('url', 'id', 'a_address')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    address_list = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('url', 'id', 'u_name', 'u_password', 'address_list')
