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
    return render(request, 'utilisateurs/index.html')



# page affiché après inscription du client

@login_required(login_url='connexion')
def bienvenue(request):
    return render(request, 'utilisateurs/bienvenue.html') 



# crer son compte (profil) parent/eleve

def enregistrement(request):
    registered = False
    err1 = " "
    err2 = " "
    if request.method == 'POST':

        # récuper les infos du user
        user_form = UserForm()
        user_form.username = request.POST.get('username')
        username = user_form.username
        user_form.first_name = request.POST.get('first_name')
        user_form.last_name = request.POST.get('last_name')
        user_form.email = request.POST.get('email')
        user_form.password1 = request.POST.get('password1')
        password = user_form.password1
        user_form.password2 = request.POST.get('password2')
        user_form = UserForm(data=request.POST)

        type_user = request.POST.get('type_user')

        if type_user == 'enseignant':
            
            # enregistrer l'enseigant
            repetiteur_form = RepetiteurForm()
            #repetiteur_form.civilite = request.POST.get('civilite')
            repetiteur_form.age = request.POST.get('age')
            repetiteur_form.telephone = request.POST.get('telephone')
            repetiteur_form.photoProfil = request.POST.get('photoProfil')
            repetiteur_form.niveauEtude = request.POST.get('niveauEtude')
            repetiteur_form.ville = request.POST.get('ville')
            repetiteur_form.quartier = request.POST.get('quartier')
            #repetiteur_form.langue = request.POST.get('langue')
            repetiteur_form = RepetiteurForm(data=request.POST)
            if user_form.is_valid() and repetiteur_form.is_valid():
                user = user_form.save()
                user.save()
                repetiteur = repetiteur_form.save(commit=False)
                repetiteur.user = user
                repetiteur.save()
                registered = True
                
                # connecter le user
                user_log = authenticate(username=username, password=password)
                login(request, user_log)
                # le renvoyer vers la page Mon Profil
                return HttpResponseRedirect('consulter_profil')
            else:
                err1 = user_form.errors
                err2 = repetiteur_form.errors
        else:

            # enregistrer le client (élève/parent)
            client_form = ClientForm(data=request.POST)
            #client_form.civilite = request.POST.get('civilite')
            client_form.age = request.POST.get('age')
            client_form.telephone = request.POST.get('telephone')
            client_form.photoProfil = request.POST.get('photoProfil')
            #client_form.langue = request.POST.get('langue')
            client_form = ClientForm(data=request.POST)
            if user_form.is_valid() and client_form.is_valid():
                user = user_form.save()
                user.save()
                client = client_form.save(commit=False)
                client.user = user
                client.save()
                registered = True

                # connecter le user
                user_log = authenticate(username=username, password=password)
                login(request, user_log)
                return HttpResponseRedirect('bienvenue')
            else:
                err1 = user_form.errors
                err2 = client_form.errors
    else:
        user_form = UserForm()
        repetiteur_form = RepetiteurForm()
    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':repetiteur_form,
    }
    return render(request, 'utilisateurs/enregistrement.html', content)


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
                    login(request, user)
                    return HttpResponseRedirect('bienvenue')
                elif user_actif in listRep:
                    login(request, user)
                    return HttpResponseRedirect('consulter_profil')
                else:
                    msg1 = messages.info(request, "cet utilisateur ne correspond pas à un compte Parent/Élève ou Enseignant !")
                content1 = {
                    'msg1':msg1
                }
                return render(request, 'utilisateurs/conexion.html', content1)
            else:
                return HttpResponse("L'utilisateur est désactivé")
        else:
            msg = messages.info(request, "votre Nom d'utilisateur ou votre Mot de passe est incorrect, veuillez réessayer SVP !")
            content = {
                'msg':msg
            }
            return render(request, 'utilisateurs/conexion.html', content)
    else:
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



# afficher la liste de tous les répétiteurs en enregistrés sur la plateforme

@login_required(login_url='connexion')
def liste_repetiteurs(request):
    return render(request, 'utilisateurs/liste_repetiteurs.html')


# fonction permettant de se déconnecter

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')