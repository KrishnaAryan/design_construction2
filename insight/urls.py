
from django.urls import path,include
from .views import *
urlpatterns = [
    path('Insight/',InsightView.as_view() ),
    
]
