from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.groups_view, name='groups'),
    path('leaderboards/', views.leaderboard_view, name='leaderboards'),
]

