from django.urls import path

from App import views

app_name = '[App]'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('uploadfile/', views.upload_file, name='upload_file'),
    path('imagefield/', views.image_field, name='image_field'),
    path('mine/', views.mine, name='mine'),
]