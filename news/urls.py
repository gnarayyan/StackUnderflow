from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHomeView.as_view()),
    path('info/', views.InfoView.as_view()),
    path('info/<str:model>', views.CategoryView.as_view()),




]
