from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.serializer import CommentSerializer, GroupSerializer, PostSerializer
from api.permissions import IsAuthenticated, AuthorPermission
from posts.models import Comment, Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, AuthorPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        if not User.objects.get(username=self.request.user).is_superuser:
            raise PermissionDenied('Недостаточно прав для создания группы')
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, AuthorPermission,)

    def get_post_id(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post_id())

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post_id())
