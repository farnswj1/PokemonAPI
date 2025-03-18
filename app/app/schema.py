from graphene import ObjectType, Schema
from pokemon.graphql import PokemonQuery


class Query(PokemonQuery, ObjectType):
    pass


schema = Schema(query=Query, auto_camelcase=False)
