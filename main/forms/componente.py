from django import forms

from main.forms import FieldSetModelFormMixin
from main.models.componente import Componente


class ComponenteForm(FieldSetModelFormMixin):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña (Firmar)')

    class Meta:
        model = Componente
        fields = [
            'id', 'nombre_comercial', 'iupac', 'unii', 'formula', 'peso_molecular', 'biodisponibilidad',
            'union_proteica', 'metabolismo', 'vida_media', 'excrecion', 'via_admon', 'tipo'
        ]


class ComponenteUpdateForm(ComponenteForm):
    descripcion = forms.CharField(widget=forms.Textarea, label='Motivo de la Edicion')
