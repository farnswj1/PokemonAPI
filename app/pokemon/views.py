from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from pokemon.filters import PokemonFilterSet


# Create your views here.
class PokemonListCreateAPIView(ListCreateAPIView):
    """
    Returns a paginated list of Pokemon.
    The results can be filtered via query parameters.
    Also creates a new Pokemon and saves its data to the database.
    Only administrators have access to creating one.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filterset_class = PokemonFilterSet


class PokemonDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete the data of the Pokemon
    with the corresponding ID.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
