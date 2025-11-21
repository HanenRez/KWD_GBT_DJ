from django.db import models
from django.core.validators import FileExtensionValidator
 


class Niveau(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    personnage = models.CharField(max_length=100, blank=True)

    # ImageField OK si tu utilises django-svg-image-form-field
    illustration = models.ImageField(upload_to='niveaux_illustrations/', blank=True,null=True)
    illustration2 = models.ImageField(upload_to='niveaux_illustrations/', blank=True,null=True)

    audio = models.FileField(upload_to='audios/', blank=True, null=True)
    audio2 = models.FileField(upload_to='audios/', blank=True, null=True)
    ordre = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.personnage or self.nom

class Animation(models.Model):
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200, blank=True)
    # ImageField OK si tu utilises django-svg-image-form-field
    fichier_svg = models.ImageField(upload_to='animations_svg/')
    audio = models.FileField(upload_to='audios/', blank=True, null=True)
    ordre = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.titre