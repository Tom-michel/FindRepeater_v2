from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.



# ajouter un cours

def ajouter_cours(request):
    return render(request, 'cours/ajouter_cours.html')




# modifier un cours

def modifier_cours(request):
    return render(request, 'cours/modifier_cours.html')




# supprimer un cours

def supprimer_cours(request):
    return render(request, 'cours/supprimer_cours.html')
