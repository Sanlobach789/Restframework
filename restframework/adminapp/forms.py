from restframework.authapp.models import User


class UserAdminEditForm(UserEditForm):
    class Meta:
        model = User
        fields = '__all__'
