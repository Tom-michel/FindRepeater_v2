from django.contrib import admin
from .models import Repetiteur
from .models import Client
from .models import CoursEns

# Register your models here.


admin.site.register(Repetiteur)
admin.site.register(Client)
admin.site.register(CoursEns)