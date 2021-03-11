from rest_framework.viewsets import ModelViewSet

from mainapp.models import Project, TodoList
from mainapp.serializers import ProjectSerializer, TodoListSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


