from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Apiculteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Rucher(models.Model):
    apiculteurs = models.ManyToManyField(Apiculteur, related_name="ruchers")
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.localisation}"


class Ruche(models.Model):
    rucher = models.ForeignKey(Rucher, on_delete=models.CASCADE, related_name="ruches")
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)  # ex : "Dadant", "Langstroth"
    date_installation = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} (Rucher: {self.rucher.nom})"


class Cadre(models.Model):
    ruche = models.ForeignKey(Ruche, on_delete=models.CASCADE, related_name="cadres")
    numero = models.IntegerField()  # Numéro de cadre pour repérer l'emplacement dans la ruche
    
    def __str__(self):
        return f"Cadre {self.numero} (Ruche: {self.ruche.nom})"


class Mesure(models.Model):
    cadre = models.ForeignKey(Cadre, on_delete=models.CASCADE, related_name="mesures")
    date = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(blank=True, null=True)
    humidite = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Date {self.date} Mesure {self.temperature} (Cadre: {self.cadre.numero} - Ruche: {self.cadre.ruche.nom})"

class TemperatureReading(models.Model):
    hive_id = models.CharField(max_length=50)
    id_capteur= models.CharField(max_length=50)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ruche {self.hive_id} - Capteur : {self.id_capteur} : {self.temperature}°C"