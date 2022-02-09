from django.conf import settings
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views import static

from app.views import func1_views, index_views, func2_views, func3_views, func4_views, func5_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('func1/', func1_views.func1, name='func1'),
    path('func2/', func2_views.func2, name='func2'),
    path('func3/', func3_views.func3, name='func3'),
    path('func4/', func4_views.func4, name='func4'),
    path('func5/', func5_views.func5, name='func5'),

    # ico logo研究
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
    # debug关闭后，静态文件处理
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
