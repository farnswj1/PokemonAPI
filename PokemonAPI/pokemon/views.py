from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Pokemon
from .serializers import PokemonSerializer
from .filters import PokemonFilterSet

# Create your views here.
class PokemonListAPIView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filterset_class = PokemonFilterSet


class PokemonDetailAPIView(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonCreateAPIView(CreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonUpdateAPIView(UpdateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDeleteAPIView(DestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
