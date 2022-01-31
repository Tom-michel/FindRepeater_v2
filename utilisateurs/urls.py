from django.urls import path
from utilisateurs.views import accueil

urlpatterns = [
    path('', accueil, name="accueil")
]