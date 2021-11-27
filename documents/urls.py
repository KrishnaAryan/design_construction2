
from django.urls import path,include
from .views import *
urlpatterns = [
    path('Agreements/',AgreementsView.as_view() ),
    path('Documents/',DocumentsView.as_view() ),
    path('ConceptPlans/',ConceptPlansView.as_view() ),
    path('WorkingDrawings/',WorkingDrawingsView.as_view() ),
    path('StructuralDrawings/',StructuralDrawingsView.as_view() ),
    path('ThreeDSerializer/',ThreeDSerializerView.as_view() ),
    
]
