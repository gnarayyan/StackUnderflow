from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, LoginAPI
urlpatterns = [
    path("get-details/", UserDetailAPI.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', LoginAPI.as_view())  # , name='login'),
]
