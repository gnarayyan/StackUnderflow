from django.urls import path
from . import views

urlpatterns = [
    path('', views.RootHomeView.as_view()),
    path('api/', views.APIHomeView.as_view()),

]
