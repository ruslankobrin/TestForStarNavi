from rest_framework import serializers

from news.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'creation_date', 'author']
        read_only_fields = ['author']