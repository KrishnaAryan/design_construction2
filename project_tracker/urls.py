from django.urls import path

from project_tracker.views import ProjectView

urlpatterns = [
    path('project_tracker/',ProjectView.as_view())
]
