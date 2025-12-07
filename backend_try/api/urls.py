from django.urls import path
from .views import DataApi

urlpatterns= [
    path('data/', DataApi.as_view()),
    path('data/<int:pk>/', DataApi.as_view()),
]