from rest_framework import serializers
from last2.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title', 'content', 'views', 'category', 'auth', 'created_at']
        read_only_fields = ['auth', 'created_at']
 