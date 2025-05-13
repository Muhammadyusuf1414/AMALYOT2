from rest_framework.generics import ListCreateAPIView
from last2.models import CustomUser
from last2.serializers.user import CustomUserSerializer

class CustomUserAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
