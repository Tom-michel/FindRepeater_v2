from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
from utilisateurs.models import Repetiteur

# Create your models here.



# creation de la classe Classe

class Classe(models.Model):
    niveau = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.niveau



# creation de la classe Matiere

class Matiere(models.Model):
    intitule = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.intitule



# creation de la classe cours

class Cours(models.Model):
    JOURS = [
        ('lundi','lundi'),('mardi','mardi'),('mercredi','mercredi'),('jeudi','jeudi'),
        ('vendredi','vendredi'),('samedi','samedi'),('dimanche','dimanche')
    ]
    jour = models.CharField(max_length=200, null=True, choices=JOURS, default='lundi')
    
    HEURES_DEBUT = [
        ('7H','7H'),('8H','8H'),('9H','9H'),('10H','10H'),('11H','11H'),('12H','12H'),('13H','13H'),
        ('14H','14H'),('15H','15H'),('16H','16H'),('17H','17H'),('18H','18H')
    ]
    heure_début = models.CharField(max_length=200, null=True, choices=HEURES_DEBUT, default='7H')
    
    DUREE = [
        ('1H','1H'),('1H30','1H30'),('2H','2H'),('2H30','2H30'),('3H','3H')
    ]
    duree = models.CharField(max_length=200, null=True, choices=DUREE, default='2H')

    # un Cours a une seulle Matiere
    matiere = models.ForeignKey(Matiere, null=True, on_delete=models.CASCADE)

    # un Cours concerne une seule Classe
    classe = models.ForeignKey(Classe, null=True, on_delete=models.SET_NULL)

    # un Cours est dispensé par un seul Repetiteur
    repetiteur = models.ForeignKey(Repetiteur, null=True, on_delete=models.CASCADE)

    def __str__(self):
        info = self.matiere.intitule+" "+self.classe.niveau
        return info