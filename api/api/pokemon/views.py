from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(7200))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PokemonDetailAPIView(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @method_decorator(cache_page(7200))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PokemonCreateAPIView(CreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonUpdateAPIView(UpdateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDeleteAPIView(DestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
