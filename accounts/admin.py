from django.contrib import admin
from django.db.models import fields
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from django.utils.html import format_html

# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
admin.site.site_header=' '
admin.site.index_title='𓊈𒆜🆆🅴🅻🅲🅾🅼🅴 🆃🅾  🆂🆄🅿🅴🆁 🅰🅳🅼🅸🅽 🅿🅰🅽🅴🅻𒆜𓊉'
# Register your models here.
# @admin.register(Registration)
# class RegistrationAdmin(admin.ModelAdmin)
class RegistrationAdmin(BaseUserAdmin):
    add_form=customUserCreationForm
    form=customeUserChangeForms 
    model=Registration
    list_display=('id','username','mobile_no','password')

    fieldsets=(
        # (None,{'fields':('email','mobile_no')}),
        ('permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions',)}),
    )
    add_fieldsets=(
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2','email','mobile_no')
            }
        ),
    )
    search_fields = ('email','mobile_no')
    ordering=('email',)
    list_per_page=10
admin.site.register(Registration,RegistrationAdmin)


@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display=('id','registrations','full_name','gender','dob','profile_image_customer','local_address','city','state','zip_code')
    fields = ('registrations','full_name','profile_image','gender', 'dob',
    'local_address','city','state','zip_code')
    list_per_page=10
    search_fields = ('state','city')

    def profile_image_customer(self,obj):
        return format_html(f'<img src="/media/{obj.profile_image}" style=height:50px;width:50px>')

    
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display=('id','package_names','package_detail')
    search_fields = ('package_names',)
    list_per_page=10


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('id','name','department_name')
    search_fields=('department_name','name')
    list_per_page=10


@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display=('id','registration','department','booking_date','total_value','booking_amount','project_description','package')
    fields=('registration','department','booking_date','total_value','booking_amount','project_description','package')
    search_fields = ('booking_amount',)
    list_per_page=10


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('id','registration','project_details','name','position','mobile_number','profile_image')
    list_display_links = ('registration','project_details','name','position','mobile_number','profile_image')
    fields=('registration','project_details','name','position','mobile_number','profile_pic')
    list_per_page=10
    search_fields = ('name','mobile_number')

    def profile_image(self,obj):
        return format_html(f'<img src="/media/{obj.profile_pic}" style=height:50px;width:50px>')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=('id','user','subject','message')
    # list_display_links = ('registration','project_details','name','position','mobile_number','profile_image')
    # fields=('id','user','subject','message')
    list_per_page=10
    search_fields = ('user',)

    



