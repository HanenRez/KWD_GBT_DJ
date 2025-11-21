from django.contrib import admin
from .models import Niveau, Animation
from .forms import NiveauForm, AnimationForm   # important !




# 2. Enregistrez le modèle dans l'admin en utilisant le formulaire personnalisé
@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    form = NiveauForm # Utilisez le formulaire que vous avez défini ci-dessus
    list_display = ('id', 'nom', 'personnage', 'ordre')
    search_fields = ('nom', 'personnage')

@admin.register(Animation)
class AnimationAdmin(admin.ModelAdmin):
    form = AnimationForm # Utilisez le formulaire que vous avez défini ci-dessus
    list_display = ('id','titre','niveau', 'actif', 'ordre')
    search_fields = ('titre','niveau')



