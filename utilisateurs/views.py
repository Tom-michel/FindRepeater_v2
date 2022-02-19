from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, ClientForm, RepetiteurForm
from django.contrib.auth.models import User
from .models import Repetiteur, Client

# Create your views here.



# page d'accueil

def accueil(request):
    listR = Repetiteur.objects.all()
    listRep = []
    for rep in listR:
        listRep.append(rep.user.username)
    content = {'listRep':listRep}
    return render(request, 'utilisateurs/index.html', content)



# page affiché après inscription du client

@login_required(login_url='connexion')
def bienvenue(request):
    return render(request, 'utilisateurs/bienvenue.html') 


def collapse(request):
    user_form = UserForm()
    repetiteur_form = RepetiteurForm()
    content = {
        'form1':user_form,
        'form2':repetiteur_form,
    }
    return render(request, 'utilisateurs/collapse.html', content) 



# crer son compte (profil) parent/eleve

def enregistrement(request):
    registered = False
    err1 = " "
    err2 = " "
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if user_form.is_valid() and client_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            registered = True
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page Mon Profil
            return HttpResponseRedirect('bienvenue')
        else:
            err1 = user_form.errors
            err2 = client_form.errors
    else:
        user_form = UserForm()
        client_form = ClientForm()
    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':client_form,
    }
    return render(request, 'utilisateurs/enregistrement.html', content)

def enregistrement_prof(request):
    registered = False
    err1 = " "
    err2 = " "
    errUser = ""
    if request.method == "POST":
        repetiteur_form = RepetiteurForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if user_form.is_valid() and repetiteur_form.is_valid():
            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            repetiteur = repetiteur_form.save(commit=False)
            tel1 = repetiteur.telephone1
            tel2 = repetiteur.telephone2
            if tel2 == "":
                tel2 = tel1
            repetiteur.user = user
            repetiteur.save()
            registered = True
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page Mon Profil
            return HttpResponseRedirect('consulter_profil')
        else:
            nom_util = request.POST.get('username')
            for util in User.objects.all():
                if util.username == nom_util:
                    errUser = "Un utilisateur avec ce nom existe déjà."
            err1 = user_form.errors
            err2 = repetiteur_form.errors
    else:
        user_form = UserForm()
        repetiteur_form = RepetiteurForm()
    content = {
        'registered':registered,
        'errUser':errUser,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':repetiteur_form,
    }
    return render(request, 'utilisateurs/enregistrement_prof.html', content)


# se connecter à son compte

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            listClient = []
            listRep = []
            if user.is_active:
                clients = Client.objects.all()
                profs = Repetiteur.objects.all()
                user_actif = username
                
                for cli in clients:
                    listClient.append(cli.user.username)
                for rep in profs:
                    listRep.append(rep.user.username)

                if user_actif in listClient:
                    if user.is_authenticated:
                        logout(request)
                    login(request, user)
                    return HttpResponseRedirect('bienvenue')
                elif user_actif in listRep:
                    if user.is_authenticated:
                        logout(request)
                    login(request, user)
                    return HttpResponseRedirect('consulter_profil')
                else:
                    msg1 = messages.info(request, "cet utilisateur ne correspond pas à un compte Parent/Élève ou Enseignant !")
                content1 = {
                    'msg1':msg1
                }
                return render(request, 'utilisateurs/connexion.html', content1)
            else:
                return HttpResponse("L'utilisateur est désactivé")
        else:
            msg = messages.info(request, "votre Nom d'utilisateur ou votre Mot de passe est incorrect, veuillez réessayer !")
            content = {
                'msg':msg
            }
            return render(request, 'utilisateurs/connexion.html', content)
    else:
        return render(request, 'utilisateurs/connexion.html')



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



# afficher la liste de tous les répétiteurs en enregistrés sur la plateforme

@login_required(login_url='connexion')
def liste_repetiteurs(request):
    return render(request, 'utilisateurs/liste_repetiteurs.html')


# fonction permettant de se déconnecter

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')