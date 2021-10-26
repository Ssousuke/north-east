from django.urls import path
from . import views

app_name = 'publication'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<str:slug>/', views.detail, name='detail'),
]
