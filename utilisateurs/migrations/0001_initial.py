# Generated by Django 4.0.1 on 2022-03-21 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utilisateurs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repetiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=200, null=True)),
                ('quartier', models.CharField(max_length=200, null=True)),
                ('langue', models.CharField(choices=[('fançais', 'fançais'), ('anglais', 'anglais'), ('bilingue', 'bilingue')], default='fançais', max_length=200, null=True)),
                ('telephone1', models.CharField(max_length=200, null=True)),
                ('civilite', models.CharField(choices=[('Mr', 'Mr'), ('Mme', 'Mme')], default='Mr', max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('telephone2', models.CharField(blank=True, max_length=200)),
                ('niveauEtude', models.CharField(max_length=200, null=True)),
                ('profession', models.CharField(max_length=200, null=True)),
                ('photoProfil', models.ImageField(blank=True, upload_to=utilisateurs.models.renommer_image)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=200, null=True)),
                ('quartier', models.CharField(max_length=200, null=True)),
                ('langue', models.CharField(choices=[('fançais', 'fançais'), ('anglais', 'anglais'), ('bilingue', 'bilingue')], default='fançais', max_length=200, null=True)),
                ('telephone1', models.CharField(max_length=200, null=True)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilisateurs.classe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
