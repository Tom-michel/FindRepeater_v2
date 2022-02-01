from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.



# page d'accueil

def accueil(request):
    return render(request, 'utilisateurs/index.html')


# crer son compte (profil) parent/eleve

def enregistrement(request):
    return render(request, 'utilisateurs/enregistrement.html')


# se connecter à son compte

def connexion(request):
    return render(request, 'utilisateurs/conexion.html')



# consulter son profil

@login_required(login_url='connexion')
def consulter_profil(request):
    return render(request, 'utilisateurs/consulter_profil.html')




# modifier son profil

@login_required(login_url='connexion')
def modifier_profil(request):
    return render(request, 'utilisateurs/modifier_profil.html')



# voir un profil (par le client)

@login_required(login_url='connexion')
def voir_profil(request):
    return render(request, 'utilisateurs/voir_profil.html')



# afficher la liste des répétiteurs disponibles (après une recherche)

@login_required(login_url='connexion')
def profs_disponibles(request):
    return render(request, 'utilisateurs/profs_disponibles.html')



# rechercher un repetiteurs

@login_required(login_url='connexion')
def recherche_repetiteur(request):
    return render(request, 'utilisateurs/recherche_repetiteur.html')



# fonction permettant de se déconnecter

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')