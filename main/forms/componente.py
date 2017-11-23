from main.forms import FieldSetModelFormMixin
from main.models.componente import Componente


class ComponenteForm(FieldSetModelFormMixin):
    class Meta:
        model = Componente
        fields = [
            'id', 'nombre_comercial', 'iupac', 'unii', 'formula', 'peso_molecular', 'biodisponibilidad',
            'union_proteica', 'metabolismo', 'vida_media', 'excrecion', 'via_admon', 'tipo'
        ]
