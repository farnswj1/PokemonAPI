from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
    ProhibitNullCharactersValidator
)
from django.urls import reverse
from django_choices_field import TextChoicesField


# Create your models here.
class TypeCategory(models.TextChoices):
    BUG = ('Bug', 'Bug')
    DARK = ('Dark', 'Dark')
    DRAGON = ('Dragon', 'Dragon')
    ELECTRIC = ('Electric', 'Electric')
    FAIRY = ('Fairy', 'Fairy')
    FIGHTING = ('Fighting', 'Fighting')
    FIRE = ('Fire', 'Fire')
    FLYING = ('Flying', 'Flying')
    GHOST = ('Ghost', 'Ghost')
    GRASS = ('Grass', 'Grass')
    GROUND = ('Ground', 'Ground')
    ICE = ('Ice', 'Ice')
    NORMAL = ('Normal', 'Normal')
    POISON = ('Poison', 'Poison')
    PSYCHIC = ('Psychic', 'Psychic')
    ROCK = ('Rock', 'Rock')
    STEEL = ('Steel', 'Steel')
    WATER = ('Water', 'Water')


class Pokemon(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(30),
            RegexValidator(r"^[A-Z][A-Za-z0-9% \-'\.\(\)]+$"),
            ProhibitNullCharactersValidator()
        ]
    )
    type1 = TextChoicesField(
        max_length=10,
        null=False,
        choices_enum=TypeCategory,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(10),
            RegexValidator(r"^[A-Z][a-z]{2,9}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    type2 = TextChoicesField(
        max_length=10,
        null=True,
        choices_enum=TypeCategory,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(10),
            RegexValidator(r"^[A-Z][a-z]{2,9}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    total = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )
    hp = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    attack = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    defense = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    special_attack = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    special_defense = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    speed = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    generation = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9)
        ]
    )
    legendary = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pokemon:api:detail', args=(self.pk,))

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Pokemon'
