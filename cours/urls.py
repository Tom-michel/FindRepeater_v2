from django.urls import path
from .views import *

urlpatterns = [
    path('', liste_cours, name="liste_cours"),
    path('ajouter_cours', ajouter_cours, name="ajouter_cours"),
    path('modifier_cours/<str:id_c>', modifier_cours, name="modifier_cours"),
    path('supprimer_cours/<str:id_c>', supprimer_cours, name="supprimer_cours"),
    path('ajouter_matiere', ajouter_matiere, name="ajouter_matiere"),
    path('ajouter_classe', ajouter_classe, name="ajouter_classe"),
    path('ajouter_classe_cli', ajouter_classe_cli, name="ajouter_classe_cli"),
    path('ajouter_classe_cli_Modif', ajouter_classe_cli_Modif, name="ajouter_classe_cli_Modif"),
    path('ajouter_classe_rep_modif/<str:id_c>', ajouter_classe_rep_modif, name="ajouter_classe_rep_modif"),
    path('ajouter_matiere_rep_modif/<str:id_c>', ajouter_matiere_rep_modif, name="ajouter_matiere_rep_modif"),
]