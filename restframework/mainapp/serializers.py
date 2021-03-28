from rest_framework.relations import HyperlinkedRelatedField, StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from authapp.serializers import UserModelSerializer
from mainapp.models import Project, TodoList


class ProjectSerializer(HyperlinkedModelSerializer):
    related_users = UserModelSerializer(many=True, read_only=True)
    # users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectReadSerializer(ModelSerializer):
    # Настройка сериализатора
    # Настройка Foreign Key
    # owner = HyperlinkedIdentityField(view_name='user-detail')
    # Настройка Many to many
    # related_users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    related_users = UserModelSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoListSerializer(HyperlinkedModelSerializer):
    project = ProjectSerializer(read_only=True)
    author = UserModelSerializer(read_only=True)

    class Meta:
        model = TodoList
        fields = '__all__'


class ToDoReadSerializer(ModelSerializer):
    # project = HyperlinkedIdentityField(view_name='project-detail')
    # creator = HyperlinkedIdentityField(view_name='user-detail')
    # project = StringRelatedField()
    project = ProjectSerializer
    # author = StringRelatedField()
    author = UserModelSerializer

    class Meta:
        model = TodoList
        # exclude = ('is_active',)
        fields = '__all__'
