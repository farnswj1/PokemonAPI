from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from pokemon.factories import PokemonFactory
from pokemon.serializers import PokemonSerializer
from core.factories import UserFactory


# Create your tests here.
class TestAuthMixin:
    def set_auth_credentials(self, is_staff: bool | None = False):
        user = UserFactory(is_staff=is_staff)
        access_token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')


class PokemonTestCase(APITestCase):
    def test_pokemon(self):
        for pokemon in PokemonFactory.create_batch(10):
            self.assertIsInstance(pokemon.id, int)
            self.assertIsInstance(pokemon.name, str)
            self.assertIsInstance(pokemon.type1, str)
            self.assertIsInstance(pokemon.type2, str | None)
            self.assertIsInstance(pokemon.total, int)
            self.assertIsInstance(pokemon.hp, int)
            self.assertIsInstance(pokemon.attack, int)
            self.assertIsInstance(pokemon.defense, int)
            self.assertIsInstance(pokemon.special_attack, int)
            self.assertIsInstance(pokemon.special_defense, int)
            self.assertIsInstance(pokemon.speed, int)
            self.assertIsInstance(pokemon.generation, int)
            self.assertIsInstance(pokemon.legendary, bool)


class PokemonFormTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'name': 'Bulbasaur',
            'type1': 'Grass',
            'type2': 'Poison',
            'total': 318,
            'hp': 45,
            'attack': 49,
            'defense': 49,
            'special_attack': 65,
            'special_defense': 65,
            'speed': 45,
            'generation': 1,
            'legendary': False
        }

    def test_valid(self):
        serializer = PokemonSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_invalid(self):
        self.data['name'] = '!nv@l1d'
        serializer = PokemonSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())


class PokemonListCreateAPIViewTestCase(TestAuthMixin, APITestCase):
    url = reverse_lazy('pokemon:api:list')

    def test_url(self):
        self.assertEqual(self.url, '/api/pokemon/')

    def test_list(self):
        pokemon = PokemonFactory.create_batch(10)
        data = PokemonSerializer(pokemon, many=True).data
        response = self.client.get('/api/pokemon/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], data)

    def test_create(self):
        self.set_auth_credentials(is_staff=True)
        data = {
            'name': 'Charmander',
            'type1': 'Fire',
            'total': 309,
            'hp': 39,
            'attack': 52,
            'defense': 43,
            'special_attack': 60,
            'special_defense': 50,
            'speed': 65,
            'generation': 1,
            'legendary': False
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data.items() <= response.data.items())

    def test_login_required_to_create(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 401)

    def test_permission_required_to_create(self):
        user = UserFactory()
        access_token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, 403)


class PokemonDetailAPIViewTestCase(TestAuthMixin, APITestCase):
    url = reverse_lazy('pokemon:api:detail', kwargs={'pk': 1})

    def setUp(self):
        self.pokemon = PokemonFactory(id=1, name='Charmander')

    def test_url(self):
        self.assertEqual(self.url, '/api/pokemon/1/')

    def test_detail(self):
        data = PokemonSerializer(self.pokemon).data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)

    def test_update(self):
        self.set_auth_credentials(is_staff=True)
        data = PokemonSerializer(self.pokemon).data
        response = self.client.put(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data == data)

    def test_delete(self):
        self.set_auth_credentials(is_staff=True)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

    def test_login_required_to_update(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, 401)

    def test_permission_required_to_update(self):
        self.set_auth_credentials()
        response = self.client.patch(self.url, data={})
        self.assertEqual(response.status_code, 403)

    def test_login_required_to_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 401)

    def test_permission_required_to_delete(self):
        self.set_auth_credentials()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 403)
