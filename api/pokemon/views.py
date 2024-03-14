from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from pokemon.filters import PokemonFilterSet


# Create your views here.
class PokemonListAPIView(ListAPIView):
    """
    Returns a paginated list of Pokemon.
    The results can be filtered via query parameters.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filterset_class = PokemonFilterSet


class PokemonCreateAPIView(CreateAPIView):
    """
    Creates a new Pokemon and saves its data to the database.
    Only administrators have access to this endpoint.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete the data of the Pokemon
    with the corresponding ID.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
