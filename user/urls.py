from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
]
