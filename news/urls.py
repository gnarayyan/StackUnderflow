from django.urls import path
from . import views

urlpatterns = [
    path('hint/', views.NewsHomeView.as_view()),
    path('info/<str:model>', views.CategoryView.as_view()),
    path('all/', views.NewsAllView.as_view()),
    path('post/', views.PostNewsView.as_view()),


]
