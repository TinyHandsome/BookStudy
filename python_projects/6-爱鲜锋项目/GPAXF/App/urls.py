from django.conf.urls import url

from App import views

app_name = 'App'
urlpatterns = [
    url(r'home/', views.home, name='home'),
    url(r'market/', views.market, name='market'),
    url(r'marketwithparams/(?P<typeid>\d+)/', views.market_with_params, name='market_with_params'),
    url(r'cart/', views.cart, name='cart'),
    url(r'mine/', views.mine, name='mine'),

    url(r'learn', views.learn),
]