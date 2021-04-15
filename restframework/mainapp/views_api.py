from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Project, TodoList
from .serializers import ProjectSerializer, TodoListSerializer, ProjectReadSerializer


class ProjectPagination(PageNumberPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectReadSerializer
        return ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    pagination_class = ProjectPagination
