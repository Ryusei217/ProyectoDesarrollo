from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from two_factor.views import OTPRequiredMixin

from main.models import ComponenteAuditoria


class ComponenteAuditoriaJson(OTPRequiredMixin, BaseDatatableView):
    model = ComponenteAuditoria
    columns = ['id', 'componente.nombre_comercial', 'componente.unii', 'accion', 'fecha']
    order_columns = ['id', 'componente.nombre_comercial', 'componente.unii', 'accion', 'fecha']


class ComponenteAuditoriaList(OTPRequiredMixin, TemplateView):
    template_name = 'componentes_auditoria/list.html'
