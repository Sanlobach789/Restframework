from rest_framework import mixins, viewsets, generics
from rest_framework.viewsets import ModelViewSet

from authapp.models import User
from authapp.serializers import UserModelSerializer, UserModelBaseSerializer


class UserListAPIView(
    # mixins.UpdateModelMixin, mixins.ListModelMixin,
    #                       mixins.RetrieveModelMixin, viewsets.GenericViewSet,
    generics.ListAPIView
):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelBaseSerializer
        return UserModelSerializer
