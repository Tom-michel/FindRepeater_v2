from django.contrib import admin
from .models import Repetiteur
from .models import Client
from .models import CoursEns
from .models import Personne

# Register your models here.


admin.site.register(Repetiteur)
admin.site.register(Client)
admin.site.register(CoursEns)
admin.site.register(Personne)