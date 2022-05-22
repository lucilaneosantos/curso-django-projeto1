from django.urls import path

from receitas.views import contato, home

# dominio/receitas/
urlpatterns = [
    path('', home),
    path('contato/', contato)
]
