from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('training_options/',views.training_options,name="room")
]