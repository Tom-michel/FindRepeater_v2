from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, ClientForm, RepetiteurForm
from django.contrib.auth.models import User
from .models import Repetiteur, Client
from cours.models import Cours

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



# crer son compte (profil) parent/eleve

def enregistrement(request):
    registered = False
    err1 = " "
    err2 = " "
    util = " "
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
            util = username
    else:
        user_form = UserForm()
        client_form = ClientForm()
    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':client_form,
        'util':util,
    }
    return render(request, 'utilisateurs/enregistrement.html', content)

def enregistrement_prof(request):
    registered = False
    err1 = " "
    err2 = " "
    util = " "
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
            err1 = user_form.errors
            err2 = repetiteur_form.errors
            util = username
    else:
        user_form = UserForm()
        repetiteur_form = RepetiteurForm()
    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':repetiteur_form,
        'util':util,
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
    coursList = Cours.objects.all()
    coursTemp = Cours.objects.all()
    cours = []
    for c in coursTemp:
        cours.append(c.repetiteur.user.id)

    repList = Repetiteur.objects.all()

    content = {'coursList':coursList, 'cours':cours,'repList':repList}
    return render(request, 'utilisateurs/consulter_profil.html', content)




# modifier son profil

@login_required(login_url='connexion')
def modifier_profil(request, id_r, id_u):
    err = ''
    err2 = ''
    repList = Repetiteur.objects.all()

    # identifier un répétiteur spécifique par son id
    repetiteur = Repetiteur.objects.get(id=id_r)
    
    # identifier le user associé à ce répétiteur, par son id
    for u in User.objects.all():
        if u.id == repetiteur.user.id:
            user = User.objects.get(id=id_u)
    
    # remplir le formulaire avec les info du répétiteur
    rep_form = RepetiteurForm(instance=repetiteur)
    user_form = UserForm(instance=user)
    if request.method == "POST":
        rep_form = RepetiteurForm(data=request.POST, instance=repetiteur)
        user_form = UserForm(data=request.POST, instance=user)
        
        if rep_form.is_valid() and user_form.is_valid:
            rep = rep_form.save()
            rep.save()

            use = user_form.save()
            use.save()
            repetit = rep_form.save(commit=False)
            repetit.user = use
            repetit.save()

            # connecter le user
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page Mon Profil
            return HttpResponseRedirect('../../consulter_profil')
        else:
            err = rep_form.errors
            err2 = user_form.errors
    content = {
        'err':err,
        'err2':err2,
        'rep_form':rep_form,
        'user_form':user_form,
        'repList':repList,
    }
    return render(request, 'utilisateurs/modifier_profil.html', content)



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