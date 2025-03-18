from django.contrib.admin import ModelAdmin, register
from django.utils.translation import gettext_lazy as _
from pokemon.models import Pokemon


# Register your models here.
@register(Pokemon)
class PostAdmin(ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name', 'total', 'hp', 'attack', 'defense', 'legendary')
    list_filter = ('type1', 'type2', 'legendary')
    search_fields = ('name',)
    ordering = ('id',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'id',
                )
            }
        ),
        (
            _('Information'),
            {
                'fields': (
                    'name',
                    'type1',
                    'type2',
                    'total',
                    'hp',
                    'attack',
                    'defense',
                    'special_attack',
                    'special_defense',
                    'speed',
                    'generation',
                    'legendary',
                )
            }
        )
    )
