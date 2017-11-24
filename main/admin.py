from django.contrib import admin


# Register your models here.
from main.models import Componente, ComponenteAuditoria


class ComponenteAdmin(admin.ModelAdmin):
    pass


class ComponenteAuditoriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Componente, ComponenteAdmin)
admin.site.register(ComponenteAuditoria, ComponenteAuditoriaAdmin)
