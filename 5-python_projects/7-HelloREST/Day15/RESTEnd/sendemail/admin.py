from django.contrib import admin

from sendemail.models import Grade, Student


class MyAdminSite(admin.AdminSite):
    site_title = 'RockLearn'
    site_header = 'Rock'
    site_url = '/send/home/'


site = MyAdminSite()


class StudentInfo(admin.TabularInline):
    extra = 3
    model = Student


class GradeAdmin(admin.ModelAdmin):
    list_display = 'g_name', 'g_position'
    inlines = [StudentInfo]


class StudentAdmin(admin.ModelAdmin):

    def sex(self):
        if self.s_sex:
            return '女'
        else:
            return '男'

    sex.short_description = '性别'
    list_display = 's_name', 's_age', sex
    fieldsets = (
        ('基本信息', {'fields': ('s_name', 's_age', 's_sex')}),
        ('可选信息', {'fields': ('s_height', 's_weight')}),
    )


site.register(Grade, GradeAdmin)
site.register(Student, StudentAdmin)
