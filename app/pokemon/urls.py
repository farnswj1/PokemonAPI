from django.urls import path, include
from pokemon import views


app_name = 'pokemon'

api_urls = [
    path('', views.PokemonListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', views.PokemonDetailAPIView.as_view(), name='detail'),
]

urlpatterns = [
    path('api/pokemon/', include((api_urls, 'api'), namespace='api')),
]
