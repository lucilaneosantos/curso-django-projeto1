from django.urls import path

from receitas.views import home

# dominio/receitas/
urlpatterns = [
    path('', home),  # home
]
