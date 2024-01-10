from django.urls import path
from .views import PersonListCreateView, PersonDetailView, TeamListCreateView, TeamDetailView

urlpatterns = [
    path('person/', PersonListCreateView.as_view(), name='person-list-create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('team/', TeamListCreateView.as_view(), name='team-list-create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]
