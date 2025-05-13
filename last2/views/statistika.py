from rest_framework import generics
from last2.models import News
from last2.serializers.news import NewsSerializer

class MostViewedNewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-views')
    serializer_class = NewsSerializer


class LatestNewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer


class LastFiveNewsAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-created_at')[:5]
