from django.urls import path
from .views import *

urlpatterns = [
    path('', ajouter_cours, name="ajouter_cours"),
    path('modifier_cours', modifier_cours, name="modifier_cours"),
    path('supprimer_cours', supprimer_cours, name="supprimer_cours"),
]