from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
    ProhibitNullCharactersValidator
)

# Create your models here.
class Pokemon(models.Model):
    TYPES = (
        ('Bug', 'Bug'),
        ('Dark', 'Dark'),
        ('Dragon', 'Dragon'),
        ('Electric', 'Electric'),
        ('Fairy', 'Fairy'),
        ('Fighting', 'Fighting'),
        ('Fire', 'Fire'),
        ('Flying', 'Flying'),
        ('Ghost', 'Ghost'),
        ('Grass', 'Grass'),
        ('Ground', 'Ground'),
        ('Ice', 'Ice'),
        ('Normal', 'Normal'),
        ('Poison', 'Poison'),
        ('Psychic', 'Psychic'),
        ('Rock', 'Rock'),
        ('Steel', 'Steel'),
        ('Water', 'Water'),
    )

    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
            RegexValidator(r"^[A-Z][A-Za-z0-9% \-'\.\(\)]+$"),
            ProhibitNullCharactersValidator()
        ]
    )
    type1 = models.CharField(
        max_length=10,
        choices=TYPES,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(10),
            RegexValidator(r"^[A-Z][a-z]{2,9}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    type2 = models.CharField(
        max_length=10,
        null=True,
        choices=TYPES,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(10),
            RegexValidator(r"^[A-Z][a-z]{2,9}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    total = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )
    hp = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    attack = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    defense = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    special_attack = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    special_defense = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    speed = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(300)
        ]
    )
    generation = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )
    legendary = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Pokemon'
