# Generated by Django 5.1.2 on 2024-10-30 05:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('date_installation', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive_id', models.CharField(max_length=50)),
                ('id_capteur', models.CharField(max_length=50)),
                ('temperature', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apiculteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mesure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('humidite', models.FloatField(blank=True, null=True)),
                ('cadre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesures', to='hello.cadre')),
            ],
        ),
        migrations.AddField(
            model_name='cadre',
            name='ruche',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cadres', to='hello.ruche'),
        ),
        migrations.CreateModel(
            name='Rucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('apiculteurs', models.ManyToManyField(related_name='ruchers', to='hello.apiculteur')),
            ],
        ),
        migrations.AddField(
            model_name='ruche',
            name='rucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ruches', to='hello.rucher'),
        ),
    ]