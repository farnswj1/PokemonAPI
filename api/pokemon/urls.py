from django.urls import path
from pokemon import views

app_name = "pokemon"

urlpatterns = [
    path('', views.PokemonListAPIView.as_view(), name='list'),
    path('create', views.PokemonCreateAPIView.as_view(), name='create'),
    path('<int:pk>', views.PokemonDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/update', views.PokemonUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete', views.PokemonDeleteAPIView.as_view(), name='delete'),
]
