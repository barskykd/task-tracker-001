from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]
        read_only_fields = ["id", "username"]


class TaskReadSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(allow_null=True, required=False)

    class Meta:
        model = models.Task
        fields = ["id", "title", "description", "created_by", "created_at",
                  "updated_at", "assigned_to", "status", "status_display"]

    def get_status_display(self, obj) -> str:
        return obj.get_status_display()


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ["id", "title", "description", "assigned_to", "status"]

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['created_by'] = request.user
        return super().create(validated_data)


class CommentaryFilterSerializer(serializers.Serializer):
    task_id = serializers.IntegerField(
        required=True, help_text="Id of task for which to get comments.")


class CommentaryReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = models.Commentary
        fields = ["id", "author", "text", "created_at"]


class CommentaryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commentary
        fields = ["task", "text"]

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['author'] = request.user
        return super().create(validated_data)
