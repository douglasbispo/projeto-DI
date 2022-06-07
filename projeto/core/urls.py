from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("dashboard/", views.DashboardView, name="dashboard"),
]
