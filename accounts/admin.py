from django.contrib import admin
from django.db.models import fields
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
admin.site.site_header=' '
admin.site.index_title='Welcome to our site'
# Register your models here.
# @admin.register(Registration)
# class RegistrationAdmin(admin.ModelAdmin):
class RegistrationAdmin(BaseUserAdmin):
    add_form=customUserCreationForm
    form=customeUserChangeForms 
    model=Registration
    list_display=('username','first_name','last_name','mobile_no','password')

    fieldsets=(
        # (None,{'fields':('email','mobile_no')}),
        ('permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions',)}),
    )
    add_fieldsets=(
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name','email','mobile_no')
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name','mobile_no')
    ordering=('email',)
    list_per_page=10
admin.site.register(Registration,RegistrationAdmin)


@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display=['registrations','gender','dob','profile_image','local_address','city','state','zip_code','created_at','updated_at']
    fields = ('registrations', 'profile_image','gender', 'dob',
    'local_address','city','state','zip_code')
    list_per_page=10
    search_fields = ('state_startswith','city_startswith')


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display=['package_names','created_at','updated_at']
    search_fields = ('package_names',)
    list_per_page=10


@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display=['registration','booking_date','total_value','booking_amount','project_description','package','created_at','updated_at']
    fields=('registration','booking_date','total_value','booking_amount','project_description','package')
    search_fields = ('booking_amount_startswith',)
    list_per_page=10


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['team_name','project_details','project_head','project_manager','architect','structural_engineer','procurement_manager','project_coordinator','project_engineer','site_engineer','created_at','updated_at']
    fields=('team_name','project_details','project_head','project_manager','architect','structural_engineer','procurement_manager','project_coordinator','project_engineer','site_engineer')
    list_per_page=10
    search_fields = ('team_name_startswith','project_head_startswith')

