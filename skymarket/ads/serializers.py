from rest_framework import serializers
from ads.models import Ad, Comment
from phonenumber_field.modelfields import PhoneNumberField


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ["id"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        exclude = ["created_at"]


