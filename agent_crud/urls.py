from django.urls import path
from agent_crud import views

urlpatterns = [
    path("", views.home, name="home"),
]