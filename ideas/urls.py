from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ideas'),
    path('<int:pk>/', views.detail, name='idea-detail'),
]
