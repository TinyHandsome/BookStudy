from rest_framework.permissions import BasePermission

from App.models import UserModel


class RequireLoginPermission(BasePermission):

    def has_permission(self, request, view):
        return isinstance(request.user, UserModel)
