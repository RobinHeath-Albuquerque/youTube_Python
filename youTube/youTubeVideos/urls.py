from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('youTubeVideos/', views.VideoList.as_view()),
    path('youTubeVideos/<int:pk>/', views.VideoDetail.as_view()),
]
