from django.contrib import admin
from django.db.models import fields
from .models import *
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
admin.site.site_header=' '
admin.site.index_title='Welcome to our site'
# Register your models here.
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    # form = UserChangeForm
    # fieldsets = (
    #   (None, {'fields': ('username', 'password', )}),
    #   (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    #   (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                  'groups', 'user_permissions')}),
    #   (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    #     (_('user_info'), {'fields': ('native_name', 'phone_no')}),
    #  )
    # add_fieldsets = (
    #   (None, {
    #       'classes': ('wide', ),
    #       'fields': ('username', 'password1', 'password2'),
    #   }),
    # )


    list_display=['first_name','last_name','email','username','password','mobile_no','created_at','updated_at']
    fields = ('username','password','first_name','last_name','email','mobile_no','user_permissions','is_staff','is_active','is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    # admin.site.register(Registration, UserAdmin)
    
@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display=['registrations','gender','dob','profile_image','local_address','city','state','zip_code','created_at','updated_at']
    fields = ('registrations', 'profile_image','gender', 'dob',
    'local_address','city','state','zip_code')
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display=['package_names','created_at','updated_at']

@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display=['registration','booking_date','total_value','booking_amount','project_description','package','created_at','updated_at']
    fields=('registration','booking_date','total_value','booking_amount','project_description','package')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['team_name','project_details','project_head','project_manager','architect','structural_engineer','procurement_manager','project_coordinator','project_engineer','site_engineer','created_at','updated_at']
    fields=('team_name','project_details','project_head','project_manager','architect','structural_engineer','procurement_manager','project_coordinator','project_engineer','site_engineer')