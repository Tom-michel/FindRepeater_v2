from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('bienvenue', bienvenue, name="bienvenue"),
    path('liste_repetiteurs', liste_repetiteurs, name="liste_repetiteurs"),
    path('enregistrement_prof', enregistrement_prof, name="enregistrement_prof"),
    path('enregistrement', enregistrement, name="enregistrement"),
    path('connexion', connexion, name="connexion"),
    path('consulter_profil', consulter_profil, name="consulter_profil"),
    path('modifier_profil/<str:id_r>/<str:id_u>', modifier_profil, name="modifier_profil"),
    path('modifier_profil_cli/<str:id_c>/<str:id_u>', modifier_profil_cli, name="modifier_profil_cli"),
    path('voir_profil/<str:id_r>/<str:id_u>', voir_profil, name="voir_profil"),
    path('profs_compatibles/<str:id_cli>', profs_compatibles, name="profs_compatibles"),
    path('recherche_repetiteur', recherche_repetiteur, name="recherche_repetiteur"),
    path('user_logout', user_logout, name="user_logout"),
]