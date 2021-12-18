
from django.urls import path
from .views import *
urlpatterns = [
    path('register/',RegistrationView.as_view()),
    path('personal_details/',PersonalDetailsView.as_view() ),
    path('package/',PackageView.as_view()),
    path('team/',TeamView.as_view()),
    path('login/',LoginView.as_view()),
    path('change_password/',ChangePasswordView.as_view()),
    path('project_detail/',ProjectDetailsView.as_view()),
    path('logout/',LogOutView.as_view()),
    path('forget_password/',ForgetPassword.as_view()),
    path('otp_verify/',VerifyOtp.as_view()),
    # path('resend_otp/',resend_otp)
    path('sub_admin_login/',SubAdminLoginView.as_view()),
    path('notification/',NotificationView.as_view())
]
