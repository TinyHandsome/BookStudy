from django.contrib import admin

from App.models import UserModel, Address


class UserAdmin(admin.ModelAdmin):
    list_display = 'u_name', 'u_password'
    search_fields = 'u_name',
    list_filter = 'u_name',
    list_per_page = 3


admin.site.register(UserModel, UserAdmin)
admin.site.register(Address)
