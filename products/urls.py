from django.urls import path
from products import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]