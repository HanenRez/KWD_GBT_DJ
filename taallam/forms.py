from django import forms
from django_svg_image_form_field import SvgAndImageFormField
from .models import acceuil, niveau

class acceuilForm(forms.ModelForm):
    class Meta:
        model = acceuil
        fields = "__all__"

        # Spécifiez le champ de formulaire personnalisé pour le champ 'illustration'
        field_classes = {
            'illustration': SvgAndImageFormField,
        }

class niveauForm(forms.ModelForm):
    class Meta:
        model = niveau
        fields = "__all__"

        # Spécifiez le champ de formulaire personnalisé pour le champ 'illustration'
        field_classes = {
            'illustration': SvgAndImageFormField,
        }