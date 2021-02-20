from django.urls import path, re_path

from Two import views

app_name = '[Two]'
urlpatterns = [
    # re_path(r'^students/(\d+)/', views.student),

    path('grades/', views.grades),
    re_path(r'^students/(\d)/', views.students),
    re_path(r'^gettime/(\d+)/(\d+)/(\d+)/', views.get_time, name='get_time'),
    re_path(r'^getdate/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.get_date, name='get_date'),
    re_path(r'^learn/', views.learn, name='learn'),

    path('haverequest/', views.have_request),

    path('createstudent/', views.create_student),
    path('docreatestudent/', views.do_create_student, name='do_create_student')
]
