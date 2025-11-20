from django.shortcuts import render, get_object_or_404
from .models import Niveau, Animation

def accueil(request):
    return render(request, 'accueil.html')



def liste_niveaux(request):
    niveaux = Niveau.objects.all().order_by('ordre')
    return render(request, "liste_niveaux.html", {"niveaux": niveaux})

def detail_niveau(request, niveau_id):
    niveau = get_object_or_404(Niveau, id=niveau_id)
    animations = Animation.objects.filter(niveau=niveau).order_by('titre')

    return render(request, "detail_niveau.html", {
        "niveau": niveau,
        "animations": animations
    })

