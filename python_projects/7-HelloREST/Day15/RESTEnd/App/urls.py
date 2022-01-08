from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^users/$', views.UsersAPIView.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserAPIView.as_view(), name='usermodel-detail'),
    url(r'^address/$', views.AddressAPIView.as_view(
        {
            'post': 'create',
            'get': 'list',
        }
    )),
    url(r'^address/(?P<pk>\d+)/$', views.AddressAPIView.as_view(
        {
            'get': 'retrieve',
        }
    ), name='address-detail'),
]
