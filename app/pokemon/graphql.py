from graphene import ObjectType
from graphene.relay import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from pokemon.models import Pokemon


class PokemonNode(DjangoObjectType):
    class Meta:
        model = Pokemon
        fields = '__all__'
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'type1': ['exact', 'icontains', 'istartswith'],
            'type2': ['exact', 'icontains', 'istartswith'],
            'total': ['exact', 'gt', 'lt'],
            'hp': ['exact', 'gt', 'lt'],
            'attack': ['exact', 'gt', 'lt'],
            'defense': ['exact', 'gt', 'lt'],
            'special_attack': ['exact', 'gt', 'lt'],
            'special_defense': ['exact', 'gt', 'lt'],
            'speed': ['exact', 'gt', 'lt'],
            'generation': ['exact', 'gt', 'lt'],
            'legendary': ['exact']
        }
        interfaces = (Node,)


class PokemonQuery(ObjectType):
    pokemon = Node.Field(PokemonNode)
    all_pokemon = DjangoFilterConnectionField(PokemonNode)
