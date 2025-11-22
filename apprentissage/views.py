from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils.safestring import mark_safe
import os

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



def detail_niveau_full(request, niveau_id):
    """
    Vue détaillée d'un niveau (page 'Sinan'-like).
    On lit les deux SVG (illustration2 = décor, illustration = personnage)
    et on renvoie leur contenu inline (si possible) pour interactivité JS.
    """
    niveau = get_object_or_404(Niveau, id=niveau_id)
    animations = Animation.objects.filter(niveau=niveau).order_by('ordre', 'titre')

    def read_svg_file(field):
        # field is a FileField (may be None)
        if not field:
            return None
        # si on a le chemin système (ex: en dev), on peut lire le fichier
        # field.path fonctionne si MEDIA_ROOT + file stocké localement
        try:
            path = field.path
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return mark_safe(f.read())  # rendre safe pour insertion inline
        except Exception:
            # fallback: ne pas planter; on affichera via <img>
            return None

    svg_decor = read_svg_file(niveau.illustration2)   # décor (arrière-plan)
    svg_perso = read_svg_file(niveau.illustration)    # personnage (au premier plan)

    # Si tu veux tester localement avec le fichier que tu as uploadé dans /mnt/data,
    # on peut aussi lire ce fichier directement (exemple de test rapide) :
    # test_svg = None
    # try:
    #     test_path = "/mnt/data/Rais.svg"
    #     with open(test_path, 'r', encoding='utf-8') as f:
    #         test_svg = mark_safe(f.read())
    # except:
    #     test_svg = None

    context = {
        "niveau": niveau,
        "animations": animations,
        "svg_decor": svg_decor,
        "svg_perso": svg_perso,
        # "test_svg": test_svg,
    }
    return render(request, "detail_niveau_full.html", context)


def page_sinan(request, niveau_id):
    niveau = get_object_or_404(Niveau, id=niveau_id)
    animations = Animation.objects.filter(niveau=niveau).order_by("ordre")

    def read_svg(field):
        try:
            path = field.path
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return mark_safe(f.read())
        except:
            return None
        return None

    context = {
        "niveau": niveau,
        "animations": animations,
        "svg_decor": read_svg(niveau.illustration2),
        "svg_perso": read_svg(niveau.illustration),
    }

    return render(request, "page_sinan.html", context)
