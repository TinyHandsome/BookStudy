from django.conf.urls import url

from App import views

app_name = 'App'
urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^market/', views.market, name='market'),
    url(r'^marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/', views.market_with_params,
        name='market_with_params'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^mine/', views.mine, name='mine'),

    url(r'^register/', views.regster, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^checkuser/', views.check_user, name='check_user'),

    url(r'^logout/', views.logout, name='logout'),
    url(r'^activate/', views.activate, name='activate'),

    url(r'^addtocart/', views.add_to_cart, name='add_to_cart'),

]
