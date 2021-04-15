from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

from mainapp.models import Project
from mainapp.views_api import ProjectViewSet


class TestProjectList(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        project = mixer.blend(Project)
        client = APIClient()
        response = client.put(f'/api/projects/{project.id}/', {
            'name': 'Грин'}
                              )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestBookViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
