from django.urls import path
from .views import RegisterUserAPIView, LoginAPI, UserProfile
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', LoginAPI.as_view()),

    path('profile/', UserProfile.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')

]
