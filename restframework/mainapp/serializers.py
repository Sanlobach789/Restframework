from rest_framework.serializers import HyperlinkedModelSerializer

from mainapp.models import Project, TodoList


class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
