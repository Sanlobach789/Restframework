from django.urls import path

import authapp.views as authapp
from authapp.views_api import UserListAPIView

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('register/', authapp.register, name='register'),
    # path('profile/', authapp.profile, name='profile'),
    path('logout/', authapp.logout, name='logout'),
    path('edit/', authapp.edit, name='edit'),
    path('', UserListAPIView.as_view()),
]
