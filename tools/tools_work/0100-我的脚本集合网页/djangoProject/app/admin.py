from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.site_header = '李英俊小朋友'
admin.site.site_title = '李英俊小朋友'
admin.site.index_title = '后台管理'


class UrlManageAdmin(admin.ModelAdmin):
    list_display = ('func_name', 'func_url', 'func_url_name', 'func_type', 'update_time', 'create_time')


admin.site.register(UrlManage, UrlManageAdmin)
admin.site.register([User, FuncType, MyRole])
