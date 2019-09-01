from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from stuapp import views

urlpatterns = [
    # path('actors/', views.ActorView.as_view()),
    # re_path(r'^actors/(\d+)$', views.ActorDetailView.as_view()),
]

