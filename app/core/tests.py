from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from graphene_django.utils.testing import GraphQLTestCase
from pokemon.factories import PokemonFactory
from core.factories import UserFactory
import pytest


# Create your tests here.
class UserTestCase(TestCase):
    def test_users(self):
        for user in UserFactory.create_batch(5):
            self.assertIsInstance(user.id, int)
            self.assertIsInstance(user.email, str)
            self.assertIsInstance(user.username, str)
            self.assertIsInstance(user.password, str)
            self.assertIsInstance(user.first_name, str)
            self.assertIsInstance(user.last_name, str)


class HomeViewTestCase(TestCase):
    url = reverse_lazy('core:index')

    def test_url(self):
        self.assertEqual(self.url, '/')

    def test_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')


class APIDocumentationViewTestCase(TestCase):
    url = reverse_lazy('core:api:docs')

    def test_url(self):
        self.assertEqual(self.url, '/api/docs/')

    def test_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/docs.html')


class MyTokenObtainPairViewTestCase(APITestCase):
    url = reverse_lazy('core:api:login')

    def setUp(self):
        self.user = UserFactory(username='test')

    def test_url(self):
        self.assertEqual(self.url, '/api/login/')

    def test_valid(self):
        data = {'username': 'test', 'password': 'password'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_invalid(self):
        data = {
            'username': 'test',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 401)


class MyTokenRefreshViewTestCase(APITestCase):
    url = reverse_lazy('core:api:refresh')

    def setUp(self):
        self.user = UserFactory(username='test')
        self.refresh = RefreshToken.for_user(self.user)

    def test_url(self):
        self.assertEqual(self.url, '/api/refresh/')

    def test_valid(self):
        data = {'refresh': str(self.refresh)}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.data)

    def test_invalid(self):
        data = {'refresh': 'invalid'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 401)


class GraphQLViewTestCase(TestCase):
    url = reverse_lazy('core:graphql')

    def test_url(self):
        self.assertEqual(self.url, '/graphql/')

    @pytest.mark.skip(reason='Not working at this time.')
    def test_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


@pytest.mark.skip(reason='Not working at this time.')
class GraphQLAPITestCase(GraphQLTestCase):
    def setUp(self):
        PokemonFactory.create_batch(10)

    def test_query(self):
        response = self.query(
            '''
            query {
                pokemon {
                    id
                    name
                }
            }
            '''
        )
        self.assertResponseNoErrors(response)
