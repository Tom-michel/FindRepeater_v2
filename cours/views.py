from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utilisateurs.views import *
from .forms import *

# Create your views here.




# afficher la liste de tous les cours enseignés par les enseignats de la plateforme

def liste_cours(request):
    return render(request, 'cours/liste_cours.html')



# ajouter un cours

@login_required(login_url='connexion')
def ajouter_cours(request):
    err = ''
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
            err = cours_form.errors

    content = {
        'err':err,
        'cours_form':cours_form,
        'coursList':coursList,
    }
    return render(request, 'cours/ajouter_cours.html', content)




# modifier un cours

@login_required(login_url='connexion')
def modifier_cours(request, id_c):
    err = ''
    coursList = Cours.objects.all()

    # identifier un cours par son id
    coursM = Cours.objects.get(id=id_c)

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



# ajouter une matière

@login_required(login_url='connexion')
def ajouter_matiere(request):
    mat_form = MatiereFrom()
    if request.method == 'POST':
        mat_form = MatiereFrom(data=request.POST)
        if mat_form.is_valid():
            matList = Matiere.objects.all()
            mat = request.POST.get('intitule')
            for m in matList:
                if m.intitule == mat:
                    msg = messages.info(request, "Cette matière existe déja dans la liste des matière")
                    content1 = {'msg':msg, 'mat_form':mat_form}
                    return render(request, 'cours/ajouter_matiere.html', content1)
                else:
                    matiere = mat_form.save()
                    matiere.save()
                    return HttpResponseRedirect('ajouter_cours')
    content2 = {'mat_form':mat_form}
    return render(request, 'cours/ajouter_matiere.html', content2)



# ajouter une classe

@login_required(login_url='connexion')
def ajouter_classe(request):
    classe_form = ClasseFrom()
    if request.method == 'POST':
        classe_form = ClasseFrom(data=request.POST)
        if classe_form.is_valid():
            classeList = Classe.objects.all()
            clas = request.POST.get('niveau')
            for c in classeList:
                if c.niveau == clas:
                    msg = messages.info(request, "Cette classe existe déja dans la liste des classes")
                    content1 = {'msg':msg, 'classe_form':classe_form}
                    return render(request, 'cours/ajouter_classe.html', content1)
                else:
                    classe = classe_form.save()
                    classe.save()
                    return HttpResponseRedirect('ajouter_cours')
    content2 = {'classe_form':classe_form}
    return render(request, 'cours/ajouter_classe.html', content2)