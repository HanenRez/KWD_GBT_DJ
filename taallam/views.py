from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe
import os

from .models import acceuil, niveau


def home(request):
    """
    Vue détaillée d'un niveau (page 'Sinan'-like).
    On lit les deux SVG (illustration2 = décor, illustration = personnage)
    et on renvoie leur contenu inline (si possible) pour interactivité JS.
    """
    niveaux=niveau.objects.all().order_by('id')
    svgacceuil = acceuil.objects.get(id=1)
    
    

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

    
    svg_perso = read_svg_file(svgacceuil.illustration)    # personnage (au premier plan)

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
        "svgaccueil": svgacceuil,
        "svg_perso": svg_perso,
        "niveaux":niveaux,
        # "test_svg": test_svg,
    }
    return render(request, "home.html", context)

def moughamarati(request, slug):
    """
    Vue détaillée d'un niveau (page 'Sinan'-like).
    On lit les deux SVG (illustration2 = décor, illustration = personnage)
    et on renvoie leur contenu inline (si possible) pour interactivité JS.
    """
    
    svgniveau = niveau.objects.get(slug=slug)

    

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

   
    svg_machhad = read_svg_file(svgniveau.illustration)    # personnage (au premier plan)
                                 # slug dans url et nom template

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
        "svgniveau": svgniveau,
        "svg_machhad": svg_machhad,
        # "test_svg": test_svg,
    }
    return render(request, f"{svgniveau.slug}.html", context)