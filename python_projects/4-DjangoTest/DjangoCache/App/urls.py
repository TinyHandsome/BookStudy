from django.urls import path

from App import views

app_name = '[App]'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('jokes/', views.jokes, name='jokes'),
    path('home/', views.home, name='home'),
    path('getphone/', views.get_phone, name='get_phone'),
    path('getticket/', views.get_ticket, name='get_ticket'),
    path('search/', views.search, name='search'),
    path('calc/', views.calc, name='calc'),
    path('login/', views.login, name='login'),

    path('addstudents/', views.add_students, name='add_students'),
    path('getstudents/', views.get_students, name='get_students'),
    path('getstudentswithpage/', views.get_students_with_page, name='get_students_with_page'),
]
