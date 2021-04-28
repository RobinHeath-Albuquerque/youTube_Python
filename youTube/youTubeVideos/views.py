from django.http import Http404
from django.shortcuts import render
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class VideoList(APIView):
    def get(self, request):
        video = Video.objects.get(pk=1)
        serializer = VideoSerializer(video, many=False,
                                     context={'request': request})
        return Response(serializer.data)



# Create your views here.
class VideoDetail(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)
