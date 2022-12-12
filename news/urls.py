from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHomeView.as_view()),
    path('info/', views.InfoView.as_view()),




]
