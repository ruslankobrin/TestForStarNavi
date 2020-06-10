from rest_framework import serializers

from news.models import Post, Like, Unlike


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'creation_date', 'author']
        read_only_fields = ['author']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post', 'creation_date']
        read_only_fields = ['user']


class UnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unlike
        fields = ['user', 'post', 'creation_date']
        read_only_fields = ['user']