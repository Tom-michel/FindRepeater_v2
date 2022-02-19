from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
import os

# Create your models here.



# creation la classe Utilisateur

def renommer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_profile/{}.{}".format(instance.user.username, ext)
        return os.path.join(upload_to, filename)


class Utilisateur(models.Model):
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)
    LANGUE = [
        ('fançais','fançais'),('anglais','anglais'),('bilingue','bilingue')
    ]
    langue = models.CharField(max_length=200, null=True, choices=LANGUE, default='fançais')
    telephone1 = models.CharField(max_length=200, null=True)
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=CASCADE)
    photoProfil = models.ImageField(upload_to=renommer_image, blank=True) 
    # s'inscrire sur la platefoerme
    def inscrire():
        pass
    
    # se connecter à son compte
    def connecter():
        pass
    
    # pour que la classe ne crée pas une table dans la BD
    class Meta:
        abstract = True



# creation de la classe Client(élève/parent d'élève) qui est un Utilisateur

class Client(Utilisateur):
    def __str__(self):
        return self.user.username

    # rechercher un Repetiteur
    def rechercher(self, matiere, classe, ville, quartier):
        pass

    # consulter le profil d'un Repetiteur
    def consulterProfil(sel, repetiteur):
        pass



# creation de la classe Repetiteur qui est un Utilisateur

class Repetiteur(Utilisateur):
    CIVILITE = [
        ('monsieur','monsieur'),('mademoiselle','mademoiselle'),('madame','madame')
    ]
    civilite = models.CharField(max_length=200, null=True, choices=CIVILITE, default='Monsieur')
    age = models.IntegerField(null=True)
    telephone2 = models.CharField(max_length=200, blank=True)
    niveauEtude = models.CharField(max_length=200, null=True) 

    def __str__(self):
        info = self.civilite+" "+self.user.username
        return info
   
    # s'inscrire : redefinir la methdode inscrire() de Utilisateur
    def inscrire():
        pass

    # modifier son profil (deja inscrit)
    def modifierProfil(self):
        pass