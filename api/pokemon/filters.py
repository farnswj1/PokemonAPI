from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    RangeFilter,
    BooleanFilter
)
from pokemon.models import Pokemon

class PokemonFilterSet(FilterSet):
    name = CharFilter('name', label='Name', lookup_expr='icontains')
    type1 = CharFilter('type1', label='Type 1', lookup_expr='icontains')
    type2 = CharFilter('type2', label='Type 2', lookup_expr='icontains')
    total = RangeFilter('total', label='Total')
    hp = RangeFilter('hp', label='HP')
    attack = RangeFilter('attack', label='Attack')
    defense = RangeFilter('defense', label='Defense')
    special_attack = RangeFilter('special_attack', label='Special Attack')
    special_defense = RangeFilter('special_defense', label='Special Defense')
    speed = RangeFilter('speed', label='Speed')
    generation = RangeFilter('generation', label='Generation')
    legendary = BooleanFilter('legendary', label='Legendary')

    class Meta:
        model = Pokemon
        fields = '__all__'
