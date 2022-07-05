from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
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

    @method_decorator(cache_page(7200))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PokemonDetailAPIView(RetrieveAPIView):
    """
    Returns the stats of the Pokemon with the corresponding ID.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @method_decorator(cache_page(7200))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PokemonCreateAPIView(CreateAPIView):
    """
    Creates a new Pokemon and saves its data to the database.
    Only administrators have access to this endpoint.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonUpdateAPIView(UpdateAPIView):
    """
    Modifies the data of an existing Pokemon.
    Only administrators have access to this endpoint.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDeleteAPIView(DestroyAPIView):
    """
    Removes an existing Pokemon from the database.
    Only administrators have access to this endpoint. 
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
