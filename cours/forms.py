from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Cours, Matiere, Type_Lieu_Cours



class CoursForm(forms.ModelForm):
    class Meta():
        model = Cours
        fields = [
            'matiere',
            'classes',
            'repetiteur'
        ]

class MatiereFrom(forms.ModelForm):
    class Meta():
        model = Matiere
        fields = ['intitule']

class Type_Lieu_Cours_Form(forms.ModelForm):
    class Meta():
        model = Type_Lieu_Cours
        fields = [
            'repetiteur',
            'types',
            'lieux'
        ]