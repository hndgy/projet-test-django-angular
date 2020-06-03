from django.db import models

# Create your models here.
class Etudiant(models.Model):
    num = models.CharField(max_length = 7, unique=True, default="")
    prenom = models.CharField(max_length=25, unique=True, null=False, default = "")
    nom = models.CharField(max_length=25, unique=True, null=False, default = "")

class Promo(models.Model):
    nomPromo = models.CharField(max_length=50, null = False)
    listeEtu = models.ManyToManyField(Etudiant)
