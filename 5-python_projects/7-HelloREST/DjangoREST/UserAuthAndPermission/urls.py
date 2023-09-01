from django.conf.urls import url

from UserAuthAndPermission import views

urlpatterns = [
    url(r'^users/$', views.UsersAPIView.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserAPIView.as_view(), name='usermodel-detail'),
]