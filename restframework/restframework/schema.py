import graphene
from graphene_django import DjangoObjectType

from authapp.models import User
from mainapp.models import TodoList, Project


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = TodoList
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class UserMutation(graphene.Mutation):
    class Arguments:
        last_name = graphene.String(required=True)
        id = graphene.UUID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, last_name, id):
        user = User.objects.get(id=id)
        user.last_name = last_name
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(ToDoType)
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.UUID(required=True))
    project_by_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_project_by_name(self, info, name=None):
        projects = Project.objects.all()
        if name:
            projects = Project.objects.filter(name__contains=name)
        return projects

    def resolve_user_by_name(self, info, id=None):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return TodoList.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)