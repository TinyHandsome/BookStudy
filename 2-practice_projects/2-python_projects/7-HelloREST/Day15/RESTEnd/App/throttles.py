from rest_framework.throttling import SimpleRateThrottle

from App.models import UserModel


class UserThrottle(SimpleRateThrottle):

    scope = 'user'

    def get_cache_key(self, request, view):
        if isinstance(request.user, UserModel):
            ident = request.auth
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }


class AddressThrottle(SimpleRateThrottle):

    scope = 'address'

    def get_cache_key(self, request, view):
        if isinstance(request.user, UserModel):
            ident = request.auth
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
