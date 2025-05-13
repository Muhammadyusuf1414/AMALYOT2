from rest_framework import serializers
from last2.models import Save

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'
