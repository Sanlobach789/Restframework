from rest_framework.serializers import HyperlinkedModelSerializer

from authapp.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'first_name', 'last_name', 'email', 'age', 'avatar')
