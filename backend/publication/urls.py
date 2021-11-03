from django.urls import path
from . import views

app_name = 'publication'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('noticias/<str:slug>/', views.detail, name='detail'),
    path('categorias/', views.category, name='category'),
    path('categorias/<str:category>/', views.post_category, name='list_post'),
    path('resultado/postagens/', views.search, name='search')
]
