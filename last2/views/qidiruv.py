from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from last2.models import News
from last2.serializers.news import NewsSerializer

class NewsSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if query:
            search_filter = Q(title__icontains=query) | Q(content__icontains=query)
            results = News.objects.filter(search_filter)
            serializer = NewsSerializer(results, many=True)
            return Response(serializer.data)
        return Response({"detail": "No query parameter provided."}, status=status.HTTP_400_BAD_REQUEST)
