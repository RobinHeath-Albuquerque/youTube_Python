from django.shortcuts import render
from youTube.youTubeVideos.models import Video
from serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class VideoList(APIView):

    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


# Create your views here.
