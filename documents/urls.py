
from django.urls import path,include
from .views import *
urlpatterns = [
    path('agreements/',AgreementsView.as_view() ),
    path('documents/',DocumentsView.as_view() ),
    path('concept_plans/',ConceptPlansView.as_view() ),
    path('working_drawings/',WorkingDrawingsView.as_view() ),
    path('structural_rawings/',StructuralDrawingsView.as_view() ),
    path('threeD_serializer/',ThreeDSerializerView.as_view() ),
    
]
