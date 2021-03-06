from email.policy import default
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
import os
# from cours.models import MY_CLASSES

# Create your models here.


MY_CHOICES = (('Ecole primaire','Ecole primaire'),
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


# creation la classe Utilisateur

class Personne(models.Model):
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)
    LANGUE = [
        ('français','français'),('anglais','anglais'),('français et anglais','français et anglais'),('autre','autre')
    ]
    langue = models.CharField(max_length=200, null=True, choices=LANGUE, default='fançais')
    telephone1 = models.CharField(max_length=200, null=True)
    
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

class Client(Personne):
    # classe = models.ForeignKey(Classe, null=True, on_delete=models.SET_NULL)
    classe = models.CharField(max_length=200, null=True, choices=MY_CHOICES)

    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Eleve {self.user.username}'



# creation de la classe Repetiteur qui est un Utilisateur

def renommer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    listExt = ['png', 'jpg', 'tif', 'bmp', 'jpeg', 'gif']
    if instance.user.username:
        noms = instance.user.last_name.split(' ')
        prenoms = instance.user.first_name.split(' ')
        n = ""
        p = ""
        nom_image = ""
        for nom in noms:
            n += ("_"+nom)
        for prenom in prenoms:
            p += ("_"+prenom)
        idUser = instance.user.id
        nom_image = (str(idUser)+n+p)
        # filename = "photo_profile/{}.{}".format(instance.user.username, ext)
        filename = "photo_profile/{}.{}".format(nom_image, "png")
        return os.path.join(upload_to, filename)


class Repetiteur(Personne):

    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Repetiteur')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rep')

    CIVILITE = [
        ('Mr','Mr'),('Mme','Mme')
    ]
    civilite = models.CharField(max_length=200, null=True, choices=CIVILITE, default='Mr')
    age = models.IntegerField(null=True)
    telephone2 = models.CharField(max_length=200, blank=True)
    niveauEtude = models.CharField(max_length=200, null=True) 
    profession = models.CharField(max_length=200, null=True)

    
    photoProfil = models.ImageField(default='default_img.jpg', upload_to='image/photo_profile', null=True, blank=True)
    # photoProfil = models.ImageField(upload_to=renommer_image, blank=True)

    def __str__(self):
        return f'Prof {self.user.username}'
