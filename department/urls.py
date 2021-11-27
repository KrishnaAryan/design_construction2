
from django.urls import path,include
from .views import *
urlpatterns = [
    path('Finance/',FinanceView.as_view() ),
    path('ProjectCoordination/',ProjectCoordinationView.as_view() ),
    path('DesignTeam/',DesignTeamView.as_view() ),
    path('ExecutionTeam/',ExecutionTeamView.as_view() ),
    
]
