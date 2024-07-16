from rest_framework.schemas import get_schema_view
from strawberry_django.optimizer import DjangoOptimizerExtension
from pokemon.types import Pokemon
import strawberry
import strawberry_django


api_schema = get_schema_view(
    title='Pokemon API',
    description='This is an API that provides data on Pokemon.',
    version='1.0.0'
)


@strawberry.type
class Query:
    pokemon: list[Pokemon] = strawberry_django.field()


graphql_schema = strawberry.Schema(
    query=Query,
    extensions=[DjangoOptimizerExtension]
)
