from factory.django import DjangoModelFactory, Password
from factory import Faker, LazyAttribute
from core.models import User


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    password = Password('password')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = LazyAttribute(lambda obj: f'{obj.username}@example.com')

    class Meta:
        model = User
