from rest_framework import generics
from last2.models import Save
from last2.serializers.save import SaveSerializer

class SaveAPIView(generics.ListCreateAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class SaveDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    lookup_field = 'pk'
