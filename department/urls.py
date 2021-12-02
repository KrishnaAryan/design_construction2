
from django.urls import path,include
from .views import *
urlpatterns = [
    path('finance/',FinanceView.as_view() ),
    path('project_coordination/',ProjectCoordinationView.as_view() ),
    path('design_team/',DesignTeamView.as_view() ),
    path('execution_team/',ExecutionTeamView.as_view() ),
    
]
