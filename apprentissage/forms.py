from django import forms
from django_svg_image_form_field import SvgAndImageFormField
from .models import Niveau

class NiveauForm(forms.ModelForm):
    class Meta:
        model = Niveau
        fields = "__all__"

        # Spécifiez le champ de formulaire personnalisé pour le champ 'illustration'
        field_classes = {
            'illustration': SvgAndImageFormField,
        }