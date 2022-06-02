# Generated by Django 4.0.1 on 2022-05-07 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utilisateurs', '0006_alter_client_langue_alter_repetiteur_langue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repetiteur',
            name='photoProfil',
            field=models.ImageField(blank=True, default='default_img.jpg', null=True, upload_to='photo_profile'),
        ),
        migrations.AlterField(
            model_name='repetiteur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]