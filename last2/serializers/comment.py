from rest_framework import serializers
from last2.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'news', 'author']
        read_only_fields = ['author', 'created_at']
