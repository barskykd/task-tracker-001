from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from . import models, serializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = get_user_model().objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Task CRUD operations.
    """
    queryset = models.Task.objects.select_related("created_by").select_related("assigned_to").only(
        "id", "title", "description", "status", "created_by", "assigned_to", "created_by__username", "assigned_to__username").all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.TaskWriteSerializer
        return serializers.TaskReadSerializer

    def create(self, request, *args, **kwargs):
        input_serializer = self.get_serializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        instance = input_serializer.save()
        output_serializer = serializers.TaskReadSerializer(instance)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class CommentaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Commentary CRUD operations.
    """
    queryset = models.Commentary.objects.all().order_by("-created_at").select_related(
        "author").only("id", "created_at", "text", "author", "author__username")
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']

    @extend_schema(parameters=[serializers.CommentaryFilterSerializer])
    def list(self, request, *args, **kwargs):
        params = serializers.CommentaryFilterSerializer(
            data=request.query_params)
        params.is_valid(raise_exception=True)
        self.request.validated_params = params.validated_data
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        input_serializer = self.get_serializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        instance = input_serializer.save()
        output_serializer = serializers.CommentaryReadSerializer(instance)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super().get_queryset()
        if hasattr(self.request, 'validated_params'):
            params = self.request.validated_params
            queryset = queryset.filter(task_id=params['task_id'])
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.CommentaryWriteSerializer
        return serializers.CommentaryReadSerializer


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
