from django.db import models
from django.contrib.auth.models import User


class Componente(models.Model):
    TIPO_COMPONENTE = (
        (1, 'Activo'),
        (2, 'Excipiente'),
    )

    responsable = models.ForeignKey(User, related_name='componentes', verbose_name='Responsable')
    nombre_comercial = models.CharField(max_length=50, unique=True, verbose_name='Nombre Comercial')
    iupac = models.CharField(max_length=50, unique=True, verbose_name='IUPAC')
    unii = models.CharField(max_length=25, unique=True, verbose_name='UNII')
    formula = models.CharField(max_length=50, verbose_name='Formula')
    peso_molecular = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Peso Molecular')
    biodisponibilidad = models.CharField(max_length=25, blank=True, null=True, verbose_name='Biodisponibilidad')
    union_proteica = models.CharField(max_length=25, blank=True, null=True, verbose_name='Union Proteica')
    metabolismo = models.CharField(max_length=25, blank=True, null=True, verbose_name='Metabolismo')
    vida_media = models.CharField(max_length=25, blank=True, null=True, verbose_name='Vida Media')
    excrecion = models.CharField(max_length=25, blank=True, null=True, verbose_name='Excrecion')
    via_admon = models.CharField(max_length=50, verbose_name='Via de Administracion')
    tipo = models.PositiveSmallIntegerField(choices=TIPO_COMPONENTE, verbose_name='Tipo')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    fecha_firma = models.DateTimeField(auto_now=True, verbose_name='Fecha Firma')
    firma = models.CharField(max_length=255, blank=True, null=True, verbose_name='Firma Electronica')

    class Meta:
        app_label = 'main'
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'

    def __str__(self):
        return '%s - %s' % (self.unii, self.nombre_comercial)
