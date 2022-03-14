from django.urls import path
from .views import *

urlpatterns = [
    path('', liste_cours, name="liste_cours"),
    path('ajouter_cours', ajouter_cours, name="ajouter_cours"),
    path('modifier_cours/<str:id_c>', modifier_cours, name="modifier_cours"),
    path('supprimer_cours/<str:id_c>', supprimer_cours, name="supprimer_cours"),
    path('ajouter_matiere', ajouter_matiere, name="ajouter_matiere"),
    path('ajouter_classe', ajouter_classe, name="ajouter_classe"),
]