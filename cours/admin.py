from django.contrib import admin
from .models import Classe, Matiere, Cours, Type_Lieu_Cours

# Register your models here.

admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Cours)
admin.site.register(Type_Lieu_Cours)