from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name']


class FollowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'image', 'video', 'description', 'hashtag', 'created_at']


class PostLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['user', 'post', 'created_at']


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'parent', 'created_at', ]


class CommentLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['user', 'comment', 'created_at']


class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['user', 'image', 'video', 'created_at']


class SaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ['user']


class SaveItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = ['post', 'save', 'created_date']


class ChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['person', 'created_date']


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['chat', 'author', 'text', 'image', 'video', 'created_date']




