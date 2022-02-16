from django.conf import settings
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views import static

from app.views import func1_views, index_views, func2_views, func3_views, func4_views, func5_views, func6_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('mysql2hive/', func1_views.func1, name='func1'),
    path('hana2hive/', func2_views.func2, name='func2'),
    path('oracle2hive/', func6_views.func6, name='func6'),
    path('generate_new_hive_schedule/', func6_views.func6_generate_new_hive_schedule, name='func6_generate_new_hive_schedule'),

    path('leaphddosave/', func3_views.func3, name='func3'),
    path('quotewords/', func4_views.func4, name='func4'),
    path('spiderpics/', func5_views.func5, name='func5'),

    # ico logo研究
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
    # debug关闭后，静态文件处理
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
