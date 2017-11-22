from django import forms
from django.contrib.auth.models import User



class PerfilForm(forms.ModelForm):
    # fields para perfil
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
