from datetime import timezone
from rest_framework import pagination, viewsets
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdCreateSerializer, AdDetailSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from ads.permissions import IsUser, IsOwnerPermission


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = AdCreateSerializer
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        permissions = []
        if self.action == "list":
            permissions = [AllowAny]
        elif self.action in ["retrieve", "create", "me"]:
            permissions = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permissions = [IsAuthenticated, (IsOwnerPermission and IsUser) | IsAdminUser]
        return [permission() for permission in permissions]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = Comment.objects.all().filter(ad=kwargs["ad_pk"])
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        permissions = []
        if self.action in ["list", "retrieve", "create", "me"]:
            permissions = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permissions = [IsAuthenticated, (IsOwnerPermission and IsUser) | IsAdminUser]
        return [permission() for permission in permissions]


