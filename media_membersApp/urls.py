from django.urls import path
from . import views


urlpatterns = [
    path('members/', views.members, name='members'),
    path('member/<int:pk>/', views.member, name='member'),
]
