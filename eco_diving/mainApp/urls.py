from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView),
    path('project/', views.projectView),
    path('news/', views.newsView),
]
