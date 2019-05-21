from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from rest_framework import viewsets
from .permission import IsAuthorOrReadonly
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [
        IsAuthorOrReadonly,
    ]
    filter_backends = [SearchFilter]
    search_fields = ['message']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 로그인 한 유저의 리소스만 필터해서 보이기
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs