from django.urls import path

from project_tracker.views import ProjectView
# Link for project tracker
urlpatterns = [
    path('project_tracker/',ProjectView.as_view())
]
