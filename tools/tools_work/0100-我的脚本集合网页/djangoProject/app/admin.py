from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.site_header = '李英俊小朋友'
admin.site.site_title = '李英俊小朋友'
admin.site.index_title = '后台管理'

admin.site.register([User, UrlManage, FuncType, MyRole])