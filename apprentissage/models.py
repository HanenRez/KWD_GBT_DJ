from django.db import models

class Niveau(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    personnage = models.CharField(max_length=100)
    illustration = models.ImageField(upload_to='niveaux/', blank=True, null=True)
    ordre = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nom
1

class Animation(models.Model):
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    fichier_svg = models.FileField(upload_to='animations/')
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    ordre = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.titre