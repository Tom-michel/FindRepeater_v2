from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utilisateurs.views import *
from .forms import *

# Create your views here.



# types de cours

def types_lieux(request):
    err = " "
    coursList = Cours.objects.all()
    repList = Repetiteur.objects.all()
    tlList = Type_Lieu_Cours.objects.all()

    # formulaire pour ajout de types_lieux_cours (via un modal)
    tl_form = Type_Lieu_Cours_Form()
    if request.method == 'POST':
        tl_form = Type_Lieu_Cours_Form(data=request.POST)
        if tl_form.is_valid():
            type_lieux = tl_form.save()
            type_lieux.save()
            tlList = Type_Lieu_Cours.objects.all()
            return HttpResponseRedirect('../../consulter_profil')
            # context = {'coursList':coursList, 'repList':repList, 'tlList':tlList, 'tl_form':tl_form}
            # return render(request, '../../consulter_profil', context)
        else:
            err = messages.info(request, "Choisir au moins un type et un lieu !")

    context = {'err':err,'coursList':coursList, 'repList':repList, 'tlList':tlList, 'tl_form':tl_form}
    return render(request, 'cours/types_lieux.html', context)


# modifier les types de cours

def modifier_types_lieux(request, id_tl):
    err = " "
    coursList = Cours.objects.all()
    repList = Repetiteur.objects.all()
    tlList = Type_Lieu_Cours.objects.all()

    # identifier un type_lieu par son id
    tl = Type_Lieu_Cours.objects.get(id=id_tl)

    tl_form = Type_Lieu_Cours_Form(instance=tl)

    if request.method == "POST":
        tl_form = Type_Lieu_Cours_Form(data=request.POST, instance=tl)
        if tl_form.is_valid():
            cours = tl_form.save()
            cours.save()

            tlList = Type_Lieu_Cours.objects.all()
            return HttpResponseRedirect('../../consulter_profil')
        else:
            err = messages.info(request, "Choisir au moins un type et un lieu !")
    context = {
        'err':err,
        'tl_form':tl_form,
        'coursList':coursList,
        'repList':repList,
        'tlList':tlList,
    }

    return render(request, 'cours/types_lieux.html', context)


# afficher la liste de tous les cours enseignés par les enseignats de la plateforme

def liste_cours(request):
    return render(request, 'cours/liste_cours.html')



# ajouter un cours

@login_required(login_url='connexion')
def ajouter_cours(request):
    err = ''
    repList = Repetiteur.objects.all()
    coursList = Cours.objects.all()
    cours_form = CoursForm()
    if request.method == 'POST':
        cours_form = CoursForm(data=request.POST)
        if cours_form.is_valid():
            cours = cours_form.save()
            cours.save()
            coursList = Cours.objects.all()
            return HttpResponseRedirect('../../consulter_profil')
        else:
            # err = cours_form.errors
            err = messages.info(request, "Choisir au moins 1 classe !")

    content = {
        'err':err,
        'cours_form':cours_form,
        'coursList':coursList,
        'repList':repList,
    }
    return render(request, 'cours/ajouter_cours.html', content)




# modifier un cours

@login_required(login_url='connexion')
def modifier_cours(request, id_c):
    err = ''
    coursList = Cours.objects.all()
    repList = Repetiteur.objects.all()

    # identifier un cours par son id
    coursM = Cours.objects.get(id=id_c)

    id_coursM = coursM.id

    # remplir le formulaire avec les infos du cours precedent
    cours_form = CoursForm(instance=coursM)

    if request.method == "POST":
        cours_form = CoursForm(data=request.POST, instance=coursM)
        if cours_form.is_valid():
            cours = cours_form.save()
            cours.save()

            coursList = Cours.objects.all()
            return HttpResponseRedirect('../../consulter_profil')
        else:
            err = cours_form.errors
    content = {
        'err':err,
        'cours_form':cours_form,
        'coursList':coursList,
        'repList':repList,
        'coursM':coursM,
    }
    return render(request, 'cours/ajouter_cours.html', content)




# supprimer un cours

@login_required(login_url='connexion')
def supprimer_cours(request, id_c):
    cours = Cours.objects.get(id=id_c)
    if request.method == 'POST':
        cours.delete()
        return HttpResponseRedirect('../../consulter_profil')
    content = {'cours':cours}
    return render(request, 'cours/supprimer_cours.html', content)



# ajouter une matière par le prof lors de l'ajout d'un cours

@login_required(login_url='connexion')
def ajouter_matiere(request):
    mat_form = MatiereFrom()
    if request.method == 'POST':
        mat_form = MatiereFrom(data=request.POST)
        if mat_form.is_valid():
            matList = Matiere.objects.all()
            mat = request.POST.get('intitule')
            existe = False
            for m in matList:
                if m.intitule == mat:
                    existe = True
            if existe:
                msg = messages.info(request, "Cette matière existe déja dans la liste des matière")
                content1 = {'msg':msg, 'mat_form':mat_form}
                return render(request, 'cours/ajouter_matiere.html', content1)
            else:
                matiere = mat_form.save()
                matiere.save()
                return HttpResponseRedirect('ajouter_cours')
    content2 = {'mat_form':mat_form}
    return render(request, 'cours/ajouter_matiere.html', content2)




# ajouter une matière par le prof lors de la modification d'un cours

@login_required(login_url='connexion')
def ajouter_matiere_rep_modif(request, id_c):
    mat_form = MatiereFrom()
    if request.method == 'POST':
        mat_form = MatiereFrom(data=request.POST)
        if mat_form.is_valid():
            matList = Matiere.objects.all()
            mat = request.POST.get('intitule')
            existe = False
            for m in matList:
                if m.intitule == mat:
                    existe = True
            if existe:
                msg = messages.info(request, "Cette matière existe déja dans la liste des matière")
                content1 = {'msg':msg, 'mat_form':mat_form}
                return render(request, 'cours/ajouter_matiere.html', content1)
            else:
                matiere = mat_form.save()
                matiere.save()
                return HttpResponseRedirect('../modifier_cours/'+id_c)
    content2 = {'mat_form':mat_form}
    return render(request, 'cours/ajouter_matiere.html', content2)



# ajouter une classe par le prof lors de l'ajout d'un cours

@login_required(login_url='connexion')
def ajouter_classe(request):
    classe_form = ClasseFrom()
    if request.method == 'POST':
        classe_form = ClasseFrom(data=request.POST)
        if classe_form.is_valid():
            classeList = Classe.objects.all()
            clas = request.POST.get('niveau')
            existe = False
            for c in classeList:
                if c.niveau == clas:
                    existe = True
            if existe:
                msg = messages.info(request, "Cette classe existe déja dans la liste des classes")
                content1 = {'msg':msg, 'classe_form':classe_form}
                return render(request, 'cours/ajouter_classe.html', content1)
            else:
                classe = classe_form.save()
                classe.save()
                return HttpResponseRedirect('ajouter_cours')
    content2 = {'classe_form':classe_form}
    return render(request, 'cours/ajouter_classe.html', content2)



# ajouter une classe par le prof lors de la modification d'un cours

@login_required(login_url='connexion')
def ajouter_classe_rep_modif(request, id_c):
    classe_form = ClasseFrom()
    if request.method == 'POST':
        classe_form = ClasseFrom(data=request.POST)
        if classe_form.is_valid():
            classeList = Classe.objects.all()
            clas = request.POST.get('niveau')
            existe = False
            for c in classeList:
                if c.niveau == clas:
                    existe = True
            if existe:
                msg = messages.info(request, "Cette classe existe déja dans la liste des classes")
                content1 = {'msg':msg, 'classe_form':classe_form}
                return render(request, 'cours/ajouter_classe.html', content1)
            else:
                classe = classe_form.save()
                classe.save()
                return HttpResponseRedirect('../modifier_cours/'+id_c)
    content2 = {'classe_form':classe_form}
    return render(request, 'cours/ajouter_classe.html', content2)



# ajouter un classe par le client lors de son inscription

def ajouter_classe_cli(request):
    classe_form = ClasseFrom()
    if request.method == 'POST':
        classe_form = ClasseFrom(data=request.POST)
        if classe_form.is_valid():
            classeList = Classe.objects.all()
            clas = request.POST.get('niveau')
            existe = False
            for c in classeList:
                if c.niveau == clas:
                    existe = True
            if existe:
                msg = messages.info(request, "Cette classe existe déja dans la liste des classes")
                content1 = {'msg':msg, 'classe_form':classe_form}
                return render(request, 'cours/ajouter_classe.html', content1)
            else:
                classe = classe_form.save()
                classe.save()
                return HttpResponseRedirect('../../enregistrement')
    content2 = {'classe_form':classe_form}
    return render(request, 'cours/ajouter_classe.html', content2)



# ajouter une classe par un client de de la modification de son compte

def ajouter_classe_cli_Modif(request):
    cliList = Client.objects.all()
    repList = Repetiteur.objects.all()
    classe_form = ClasseFrom()
    if request.method == 'POST':
        classe_form = ClasseFrom(data=request.POST)
        if classe_form.is_valid():
            classeList = Classe.objects.all()
            clas = request.POST.get('niveau')
            id_cli = request.POST.get('id_cli')
            id_use = request.POST.get('id_use')
            existe = False
            for c in classeList:
                if c.niveau == clas:
                    existe = True
            if existe:
                msg = messages.info(request, "Cette classe existe déja dans la liste des classes")
                content1 = {'msg':msg, 'classe_form':classe_form}
                return render(request, 'cours/ajouter_classe.html', content1)
            else:
                classe = classe_form.save()
                classe.save()
                return HttpResponseRedirect('../../modifier_profil_cli/'+id_cli+'/'+id_use)
    content2 = {'classe_form':classe_form, 'cliList':cliList, 'repList':repList}
    return render(request, 'cours/ajouter_classe.html', content2)
