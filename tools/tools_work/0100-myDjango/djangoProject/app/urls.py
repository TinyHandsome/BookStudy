from django.urls import path, re_path

from app.views import func1_views, index_views, func2_views, func3_views, func4_views, func5_views, func6_views, \
    func7_get_columns_view, func8_idcard_code_country_view, func0_test

urlpatterns = [
    path('', index_views.index, name='index'),
    path('test/', func0_test.test, name='test'),

    path('mysql2hive/', func1_views.func1, name='func1'),
    path('hana2hive/', func2_views.func2, name='func2'),
    path('oracle2hive/', func6_views.func6, name='func6'),
    path('generate_new_hive_schedule/', func6_views.func6_generate_new_hive_schedule, name='func6_generate_new_hive_schedule'),

    path('leaphddosave/', func3_views.func3, name='func3'),
    path('quotewords/', func4_views.func4, name='func4'),
    path('getcolumns/', func7_get_columns_view.func7_get_columns, name='func7'),
    path('spiderpics/', func5_views.func5, name='func5'),
    path('get_idcard_code_country/', func8_idcard_code_country_view.func8_idcard_code_country, name='func8'),
]
