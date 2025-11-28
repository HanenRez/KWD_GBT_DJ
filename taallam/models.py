from django.db import models
from django.utils.text import slugify

class acceuil(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    personnage = models.CharField(max_length=100, blank=True)
    # ImageField OK si tu utilises django-svg-image-form-field
    illustration = models.ImageField(upload_to='acceuil_illustrations/', blank=True,null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)
 

    def __str__(self):
        return self.nom

class niveau(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    personnage = models.CharField(max_length=100, blank=True)
    # ImageField OK si tu utilises django-svg-image-form-field
    illustration = models.ImageField(upload_to='niveaux_illustrations/', blank=True,null=True)
    ordre = models.PositiveIntegerField(default=1)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)

    def __str__(self):
        return self.nom

