from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from authapp.models import User
from authapp.serializers import UserModelSerializer


class UserViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
