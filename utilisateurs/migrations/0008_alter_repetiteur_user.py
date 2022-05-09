# Generated by Django 4.0.1 on 2022-05-07 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utilisateurs', '0007_alter_repetiteur_photoprofil_alter_repetiteur_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repetiteur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Repetiteur', to=settings.AUTH_USER_MODEL),
        ),
    ]
