from factory.django import DjangoModelFactory
from factory import Faker
from pokemon.models import Pokemon, TypeCategory


type_choices = [choice[0] for choice in TypeCategory.choices]


class PokemonFactory(DjangoModelFactory):
    name = Faker('pystr', min_chars=2, max_chars=30)
    type1 = Faker('random_element', elements=type_choices)
    type2 = Faker('random_element', elements=type_choices)
    total = Faker('random_int', min=0, max=1000)
    hp = Faker('random_int', min=0, max=300)
    attack = Faker('random_int', min=0, max=300)
    defense = Faker('random_int', min=0, max=300)
    special_attack = Faker('random_int', min=0, max=300)
    special_defense = Faker('random_int', min=0, max=300)
    speed = Faker('random_int', min=0, max=300)
    generation = Faker('random_int', min=1, max=9)
    legendary = Faker('boolean')

    class Meta:
        model = Pokemon
