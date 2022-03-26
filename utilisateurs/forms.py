from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Client, Repetiteur



# formulaire pour l'iscrition du client en rassemblant de 2 formulaires :
        # User (fourni par django)
        # Client (notre classe créée dans models.py)

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
class RepetiteurForm(forms.ModelForm):
    class Meta():
        model = Repetiteur
        fields = [
            'civilite',
            'age',
            'telephone1',
            'telephone2',
            'photoProfil',
            'niveauEtude',
            'profession',
            'ville',
            'quartier',
            'langue'
        ]
class ClientForm(forms.ModelForm):
    class Meta():
        model = Client
        fields = [
            'classe',
            'ville',
            'quartier',
            'telephone1',
            'langue'
        ]