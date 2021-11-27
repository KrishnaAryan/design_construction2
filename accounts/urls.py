
from django.urls import path
from .views import *
urlpatterns = [
    path('Registration/',RegistrationView.as_view() ),
    path('PersonalDetails/',PersonalDetailsView.as_view() ),
    path('Package/',PackageView.as_view() ),
    path('TeamSerializer/',TeamSerializerView.as_view() ),
    path('login/',LoginView.as_view()),
    path('change_password/',ChangePasswordView.as_view() )
    
]
