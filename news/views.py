from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from news.filters import LikeFilter
from news.models import Post, Like, Unlike
from news.serializers import PostSerializer, LikeSerializer, UnlikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user)
        except Exception as e:
            raise ValidationError(e)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeFilter

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise ValidationError(e)


class UnlikeViewSet(viewsets.ModelViewSet):
    queryset = Unlike.objects.all()
    serializer_class = UnlikeSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise ValidationError(e)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '../'
    template_name = 'signup.html'