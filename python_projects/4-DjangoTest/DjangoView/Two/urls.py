from django.urls import path

from Two import views

app_name = '[Two]'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('mine/', views.mine, name='mine'),
    path('loggout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('studentlogin/', views.student_login, name='student_login'),
]