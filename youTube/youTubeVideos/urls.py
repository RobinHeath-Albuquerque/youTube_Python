from django.urls import path
from . import views

urlpatterns = [
    path('video', views.VideoList.as_view()),
]