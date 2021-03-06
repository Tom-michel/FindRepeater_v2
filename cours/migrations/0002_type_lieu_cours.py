# Generated by Django 4.0.1 on 2022-04-11 21:53

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0002_alter_client_classe_alter_coursens_classes'),
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Lieu_Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', multiselectfield.db.fields.MultiSelectField(choices=[('Individuel', 'Individuel'), ('En groupe', 'En groupe')], max_length=20)),
                ('lieux', multiselectfield.db.fields.MultiSelectField(choices=[('Chez le prof', 'Chez le prof'), ("Chez l'apprenant", "Chez l'apprenant"), ('En ligne', 'En ligne')], max_length=38)),
                ('repetiteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.repetiteur')),
            ],
        ),
    ]
