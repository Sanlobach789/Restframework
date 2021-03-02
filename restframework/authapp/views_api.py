from rest_framework.viewsets import ModelViewSet

from authapp.models import User
from authapp.serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
