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

    listC  = Client.objects.all()
    listCli = []
    for cli in listC:
        listCli.append(cli.user.username)
    content = {'listRep':listRep, 'listCli':listCli}
    return render(request, 'utilisateurs/index.html', content)



# page affiché après inscription du client

@login_required(login_url='connexion')
def bienvenue(request):
    listC  = Client.objects.all()
    content1 = {'listC':listC}

    if request.method == "POST":
        typeRech = request.POST.get('typeRech')
        
        if typeRech == "1":

            # renvoyer tous les professeurs
            repList = Repetiteur.objects.all()
            coursList = Cours.objects.all()
            repAff = []
            coursAff = []
            coursAffTemp = []
            for rep in repList:
                repAff.append(rep)
                for c in coursList:
                    if c.repetiteur.id == rep.id:
                        coursAff.append(c)
                        coursAffTemp.append(c.matiere.intitule)

            # liste des matieres sans doublons
            coursAffInti = []
            for cour in coursAffTemp:
                if cour not in coursAffInti:
                    coursAffInti.append(cour)
            content2 = {
                'repAff':repAff,
                'coursList':coursList,
                'coursAff':coursAff,
                'coursAffInti':coursAffInti,
            }
            return render(request, 'utilisateurs/liste_repetiteurs.html', content2)

    return render(request, 'utilisateurs/bienvenue.html', content1)



# créer son compte (profil) parent/eleve

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



# créer son compte (profil) Enseignant

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
                    if user.is_authenticated:
                        logout(request)
                    login(request, user)
                    return HttpResponseRedirect('admin')
                #     msg1 = messages.info(request, "cet utilisateur ne correspond pas à un compte Parent/Élève ou Enseignant !")
                # content1 = {
                #     'msg1':msg1
                # }
                # return render(request, 'utilisateurs/connexion.html', content1)
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




# modifier son profil (le prof)

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
        
        if rep_form.is_valid() and user_form.is_valid():
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



# modifier son profil (le client)

@login_required(login_url='connexion')
def modifier_profil_cli(request, id_c, id_u):
    err = ''
    err2 = ''
    cliList = Client.objects.all()

    # identifier un client spécifique par son id
    client = Client.objects.get(id=id_c)
    
    # identifier le user associé à ce client, par son id
    for u in User.objects.all():
        if u.id == client.user.id:
            user = User.objects.get(id=id_u)
    
    # remplir le formulaire avec les info du client
    cli_form = ClientForm(instance=client)
    user_form = UserForm(instance=user)
    if request.method == "POST":
        cli_form = ClientForm(data=request.POST, instance=client)
        user_form = UserForm(data=request.POST, instance=user)
        
        if cli_form.is_valid() and user_form.is_valid():
            cli = cli_form.save()
            cli.save()

            use = user_form.save()
            use.save()
            client_cli = cli_form.save(commit=False)
            client_cli.user = use
            client_cli.save()

            # connecter le user
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page Bienvenue
            return HttpResponseRedirect('../../bienvenue')
        else:
            err = cli_form.errors
            err2 = user_form.errors
    content = {
        'err':err,
        'err2':err2,
        'cli_form':cli_form,
        'user_form':user_form,
        'cliList':cliList,
    }

    return render(request, 'utilisateurs/modifier_profil_cli.html', content)



# voir un profil (par le client)

def voir_profil(request, id_r, id_u):
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()

    # identifier un répétiteur spécifique par son id
    rep = Repetiteur.objects.get(id=id_r)
    
    # identifier le user associé à ce répétiteur, par son id
    for u in User.objects.all():
        if u.id == rep.user.id:
            use = User.objects.get(id=id_u)
    
    coursL = []
    for c in coursList:
        if c.repetiteur.user.id == rep.user.id:
            coursL.append(c)
    n = len(coursL)
    content = {
        'rep':rep,
        'use':use,
        'repList':repList,
        'coursL':coursL,
        'n':n,
    }
    return render(request, 'utilisateurs/voir_profil.html', content)



# afficher la liste des répétiteurs disponibles (après une recherche)

@login_required(login_url='connexion')
def profs_compatibles(request, id_cli):
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()

    # identifier un client spécifique par son id
    client = Client.objects.get(id=id_cli)

    repComp = []
    coursComp = []
    coursCompU = []
    coursCompUTemp = []
    for rep in repList:
        if rep.langue == client.langue and rep.ville:
            for cou in coursList:
                if cou.repetiteur.id == rep.id and cou.classe == client.classe:
                    repComp.append(rep)
                    for c in coursList:
                        if c.repetiteur.id == rep.id:
                            coursComp.append(c)
                            coursCompUTemp.append(c.matiere.intitule)
                    break

    for cour in coursCompUTemp:
        if cour not in coursCompU:
            coursCompU.append(cour)

    content = {
        'client':client,
        'repList':repList,
        'coursList':coursList,
        'repComp':repComp,
        'coursCompU':coursCompU,
        'coursComp':coursComp,
    }

    return render(request, 'utilisateurs/profs_compatibles.html', content)



# rechercher un repetiteurs

# @login_required(login_url='connexion')
def recherche_repetiteur(request):
    return render(request, 'utilisateurs/recherche_repetiteur.html')



# afficher la liste de tous les répétiteurs en enregistrés sur la plateforme

def liste_repetiteurs(request):
    return render(request, 'utilisateurs/liste_repetiteurs.html')


# fonction permettant de se déconnecter

@login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')