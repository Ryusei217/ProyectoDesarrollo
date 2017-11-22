from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil', verbose_name='Usuario')

    class Meta:
        app_label = 'main_app'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        return '%s' % self.usuario
