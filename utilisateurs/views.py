from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CoursEnsForm, UserForm, ClientForm, RepetiteurForm, PersonneForm
from cours.forms import Type_Lieu_Cours_Form
from django.contrib.auth.models import User
from .models import CoursEns, Repetiteur, Client, Personne
from cours.models import Cours, Type_Lieu_Cours

# Create your views here.


# enregistrrment multiple

def personne(request):
    persForm = PersonneForm()
    persList = Personne.objects.all()
    nb = [1,2]
    if request.method == 'POST':
        persForm = PersonneForm(data=request.POST)
        person = persForm.save()
        person.save()
        
        context = {
            'persList':persList,
            'persForm':persForm,'nb':nb
        }
        return render(request, 'utilisateurs/personne.html', context)
    context = {
            'persList':persList,
            'persForm':persForm,
            'nb':nb
        }
    return render(request, 'utilisateurs/personne.html', context)




# test du multiselectfiedl

def testMult(request):
    cform = CoursEnsForm()
    if request.method == 'POST':
        # intitule = request.POST.get('intitule')
        # classes = request.POST.get('classes')
        # coursE = CoursEns(intitule=intitule, classes=classes)
        # coursE.save()
        cform = CoursEnsForm(data=request.POST)
        coursE = cform.save()
        coursE.save()
        context = {'coursE':coursE}
        return render(request, 'utilisateurs/testMult.html', context)
        # return HttpResponseRedirect('/')

    coursEns = CoursEns.objects.all()
    context = {'coursEns':coursEns, 'cform':cform}
    return render(request, 'utilisateurs/testMult.html', context)


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
    context = {'listRep':listRep, 'listCli':listCli}
    return render(request, 'utilisateurs/index.html', context)



# page affiché après inscription du client

@login_required(login_url='connexion')
def bienvenue(request):
    listC  = Client.objects.all()
    context1 = {'listC':listC}
    return render(request, 'utilisateurs/bienvenue.html', context1)



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
    context = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':client_form,
        'util':util,
    }
    return render(request, 'utilisateurs/enregistrement.html', context)



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
    context = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':repetiteur_form,
        'util':util,
    }
    return render(request, 'utilisateurs/enregistrement_prof.html', context)


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
                # context1 = {
                #     'msg1':msg1
                # }
                # return render(request, 'utilisateurs/connexion.html', context1)
            else:
                return HttpResponse("L'utilisateur est désactivé")
        else:
            msg = messages.info(request, "votre Adresse mail ou votre Mot de passe est incorrect, veuillez réessayer !")
            context = {
                'msg':msg
            }
            return render(request, 'utilisateurs/connexion.html', context)
    else:
        return render(request, 'utilisateurs/connexion.html')



# consulter son profil

@login_required(login_url='connexion')
def consulter_profil(request):
    coursList = Cours.objects.all()
    repList = Repetiteur.objects.all()
    tlList = Type_Lieu_Cours.objects.all()

    # formulaire pour ajout de types_lieux_cours (via un modal)
    # tl_form = Type_Lieu_Cours_Form()
    # if request.method == 'POST':
    #     tl_form = Type_Lieu_Cours_Form(data=request.POST)
    #     if tl_form.is_valid():
    #         type_lieux = tl_form.save()
    #         type_lieux.save()
    #         tlList = Type_Lieu_Cours.objects.all()
    #         tlTab = []
    #         for tl in tlList:
    #             tlTab.append(tl.repetiteur.user.id)
    #         context = {'coursList':coursList, 'repList':repList, 'tlList':tlList, 'tlTab':tlTab, 'tl_form':tl_form}
    #         return render(request, 'utilisateurs/consulter_profil.html', context)
            
    tlTab = []
    for tl in tlList:
        tlTab.append(tl.repetiteur.user.id)

    context = {'coursList':coursList, 'repList':repList, 'tlList':tlList, 'tlTab':tlTab}
    return render(request, 'utilisateurs/consulter_profil.html', context)




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
        rep_form = RepetiteurForm(request.POST, request.FILES, instance=repetiteur)
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
    context = {
        'err':err,
        'err2':err2,
        'rep_form':rep_form,
        'user_form':user_form,
        'repList':repList,
    }
    return render(request, 'utilisateurs/modifier_profil.html', context)



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
    context = {
        'err':err,
        'err2':err2,
        'cli_form':cli_form,
        'user_form':user_form,
        'cliList':cliList,
    }

    return render(request, 'utilisateurs/modifier_profil_cli.html', context)



# voir un profil (par le client)

@login_required(login_url='connexion')
def voir_profil(request, id_r, id_u):
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()
    tlList  =Type_Lieu_Cours.objects.all()

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

    typLie = []
    for tl in tlList:
        if tl.repetiteur.user.id == rep.user.id:
            typLie.append(tl)

    context = {
        'rep':rep,
        'use':use,
        'repList':repList,
        'tlList':tlList,
        'coursL':coursL,
        'n':n,
        'typLie':typLie,
    }
    return render(request, 'utilisateurs/voir_profil.html', context)



# afficher la liste des répétiteurs disponibles (après une recherche)

@login_required(login_url='connexion')
def profs_compatibles(request, id_cli):
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()

    # identifier un client spécifique par son id
    client = Client.objects.get(id=id_cli)

    listRepe = []
    nb = 0
    for rep in repList:
        if rep.langue == client.langue and rep.ville == client.ville:
            for cours in coursList:
                if cours.repetiteur.id == rep.id and client.classe in cours.classes:
                    listRepe.append(rep)
                    break
    nb = len(listRepe)
    context = {'coursList':coursList, 'repList':repList, 'listRepe':listRepe, 'nb':nb}    

    return render(request, 'utilisateurs/profs_compatibles.html', context)



# page pour rechercher un repetiteurs

# @login_required(login_url='connexion')
def recherche_repetiteur(request):
    rech = False
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()
    if request.method == "POST":
        rech = True
        typeRech = request.POST.get('typeRech')

        listCours = []
        listCoursRep = []

        if typeRech == "1":
            return liste_repetiteurs(request)
        elif typeRech == "2":
            nb = 0
            matiere = request.POST.get('matiere2')
            ville = request.POST.get('ville2')
            for cours in coursList:
                if cours.matiere.intitule == matiere and cours.repetiteur.ville == ville and cours.repetiteur not in listCoursRep:
                    listCours.append(cours)
                    listCoursRep.append(cours.repetiteur)
            nb = len(listCours)
            context = {'rech':rech, 'coursList':coursList, 'listCours':listCours, 'nb':nb}
        elif typeRech == "3":
            nb = 0
            classe = request.POST.get('classe3')
            ville = request.POST.get('ville3')
            for cours in coursList:
                if classe in cours.classes and cours.repetiteur.ville == ville and cours.repetiteur not in listCoursRep:
                    listCours.append(cours)
                    listCoursRep.append(cours.repetiteur)
            nb = len(listCours)
            context = {'rech':rech, 'coursList':coursList, 'listCours':listCours, 'nb':nb}
        elif typeRech == "4":
            nb = 0
            matiere = request.POST.get('matiere4')
            classe = request.POST.get('classe4')
            ville = request.POST.get('ville4')
            for cours in coursList:
                if cours.matiere.intitule == matiere and classe in cours.classes and cours.repetiteur.ville == ville and cours.repetiteur not in listCoursRep:
                    listCours.append(cours)
                    listCoursRep.append(cours.repetiteur)
            nb = len(listCours)
            context = {'rech':rech, 'coursList':coursList, 'listCours':listCours, 'nb':nb}
        elif typeRech == "5":
            nb = 0
            matiere = request.POST.get('matiere5')
            classe = request.POST.get('classe5')
            ville = request.POST.get('ville5')
            quartier = request.POST.get('quartier5')
            for cours in coursList:
                if cours.matiere.intitule == matiere and classe in cours.classes and cours.repetiteur.ville == ville and cours.repetiteur.quartier == quartier and cours.repetiteur not in listCoursRep:
                    listCours.append(cours)
                    listCoursRep.append(cours.repetiteur)
            nb = len(listCours)
            context = {'rech':rech, 'coursList':coursList, 'listCours':listCours, 'nb':nb}

        return render(request, 'utilisateurs/recherche_repetiteur.html', context)


    coursL = []
    classeL = []
    for c in coursList:
        if c.matiere.intitule not in coursL:
            coursL.append(c.matiere.intitule)
        for clas in c.classes:
            if clas not in classeL:
                classeL.append(clas)
    villeL = []
    quartierL = []
    for rep in repList:
        if rep.ville not in villeL:
            villeL.append(rep.ville)
        if rep.quartier not in quartierL:
            quartierL.append(rep.quartier)
        
    listR = Repetiteur.objects.all()
    listRep = []
    for rep in listR:
        listRep.append(rep.user.username)

    listC  = Client.objects.all()
    listCli = []
    for cli in listC:
        listCli.append(cli.user.username)
    context = {'coursL':coursL, 'villeL':villeL, 'classeL':classeL, 'quartierL':quartierL, 'rech':rech, 'listCli':listCli, 'listRep':listRep}

    return render(request, 'utilisateurs/recherche_repetiteur.html', context)



# afficher les résultats de recherche

def resultat_recherche(request):
    return render(request, 'utilisateurs/resultat_recherche.html')


# afficher la liste de tous les répétiteurs en enregistrés sur la plateforme

def liste_repetiteurs(request):
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()
    nbRep = 0
    nbRep = repList.count()

    listR = Repetiteur.objects.all()
    listRep = []
    for rep in listR:
        listRep.append(rep.user.username)

    listC  = Client.objects.all()
    listCli = []
    for cli in listC:
        listCli.append(cli.user.username)
    
    context = {
        'repList':repList,
        'coursList':coursList,
        'nbRep':nbRep, 'listCli':listCli, 'listRep':listRep
    }
    return render(request, 'utilisateurs/liste_repetiteurs.html', context)


# fonction permettant de se déconnecter

@login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')