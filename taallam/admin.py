from django.contrib import admin
from .models import acceuil, niveau
from .forms import acceuilForm, niveauForm  # important !
# Register your models here.



# 2. Enregistrez le modèle dans l'admin en utilisant le formulaire personnalisé
@admin.register(acceuil)
class acceuilAdmin(admin.ModelAdmin):
    form = acceuilForm # Utilisez le formulaire que vous avez défini ci-dessus
    list_display = ('id', 'nom', 'personnage', 'slug')
    search_fields = ('nom', 'personnage')


@admin.register(niveau)
class niveauAdmin(admin.ModelAdmin):
    form = niveauForm # Utilisez le formulaire que vous avez défini ci-dessus
    list_display = ('id', 'nom', 'personnage', 'ordre', 'slug')
    search_fields = ('nom', 'personnage')

