from strawberry import auto
from pokemon.models import Pokemon as PokemonModel
import strawberry_django


@strawberry_django.type(PokemonModel)
class Pokemon:
    name: auto
    type1: auto
    type2: auto
    total: auto
    hp: auto
    attack: auto
    defense: auto
    special_attack: auto
    special_defense: auto
    speed: auto
    generation: auto
    legendary: auto
