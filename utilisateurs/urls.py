from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('collapse', collapse, name="collapse"),
    path('bienvenue', bienvenue, name="bienvenue"),
    path('liste_repetiteurs', liste_repetiteurs, name="liste_repetiteurs"),
    path('enregistrement_prof', enregistrement_prof, name="enregistrement_prof"),
    path('enregistrement', enregistrement, name="enregistrement"),
    path('connexion', connexion, name="connexion"),
    path('consulter_profil', consulter_profil, name="consulter_profil"),
    path('modifier_profil', modifier_profil, name="modifier_profil"),
    path('voir_profil', voir_profil, name="voir_profil"),
    path('profs_disponibles', profs_disponibles, name="profs_disponibles"),
    path('recherche_repetiteur', recherche_repetiteur, name="recherche_repetiteur"),
    path('user_logout', user_logout, name="user_logout"),
]