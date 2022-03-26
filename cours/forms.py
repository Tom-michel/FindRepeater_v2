from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Cours, Matiere, Classe



class CoursForm(forms.ModelForm):
    class Meta():
        model = Cours
        fields = [
            'jour',
            # 'heure_début',
            # 'duree',
            'matiere',
            'classe',
            'repetiteur'
        ]

class MatiereFrom(forms.ModelForm):
    class Meta():
        model = Matiere
        fields = ['intitule']

class ClasseFrom(forms.ModelForm):
    class Meta():
        model = Classe
        fields = ['niveau']