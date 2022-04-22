from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
from utilisateurs.models import Repetiteur, Classe

# Create your models here.


# creation de la classe Matiere

class Matiere(models.Model):
    intitule = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.intitule



# creation de la classe cours

from multiselectfield import MultiSelectField

MY_CLASSES = (('Ecole primaire','Ecole primaire'),
              ('6e','6e'),
              ('5e','5e'),
              ('4e','4e'),
              ('3e','3e'),
              ('Seconde','Seconde'),
              ('Premiere','Premiere'),
              ('Terminale','Terminale'),
              ('Licence 1', 'Licence 1'),
              ('Licence 2', 'Licence 2'),
              ('Licence 3', 'Licence 3'))

class Cours(models.Model):
    
    # un Cours a une seulle Matiere
    matiere = models.ForeignKey(Matiere, null=True, on_delete=models.CASCADE)

    # un Cours concerne au moins une Classe
    classes = MultiSelectField(choices=MY_CLASSES)

    # un Cours est dispensé par un seul Repetiteur
    repetiteur = models.ForeignKey(Repetiteur, null=True, on_delete=models.CASCADE)

    def __str__(self):
        info = self.matiere.intitule
        return info



# creation de la classe Type/Lieu du cours

MY_TYPES = (('Individuel','Individuel'),
            ('En groupe','En groupe'))
MY_LIEUX = (("Chez le prof","Chez le prof"),
            ("Chez l'apprenant","Chez l'apprenant"),
            ("En ligne","En ligne"),
            ("Autre lieu","Autre lieu"))

class Type_Lieu_Cours(models.Model):
    repetiteur = models.ForeignKey(Repetiteur, null=True, on_delete=models.CASCADE)
    types = MultiSelectField(choices=MY_TYPES)
    lieux = MultiSelectField(choices=MY_LIEUX)
    
    



