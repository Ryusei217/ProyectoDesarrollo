from django.contrib.auth.models import User
from django.db import models

from main.models import Componente


class ComponenteAuditoria(models.Model):
    TIPO_ACCION = (
        (1, 'Creado'),
        (2, 'Editado'),
        (3, 'Eliminado'),
    )

    componente = models.ForeignKey(Componente, related_name='pistas_auditoria', verbose_name='Componente')
    usuario = models.ForeignKey(User, related_name='componentes_auditoria', verbose_name='Usuario')
    contenido = models.TextField(verbose_name='Contenido')
    firma = models.TextField(verbose_name='Firma Electrónica')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    descripcion = models.TextField(verbose_name='Descripcion')
    accion = models.SmallIntegerField(choices=TIPO_ACCION, verbose_name='Accion')

    class Meta:
        app_label = 'main'
        verbose_name = 'Auditoria de Componente'
        verbose_name_plural = 'Auditoria de Componentes'

    def __str__(self):
        return '%s' % self.componente
