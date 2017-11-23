from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django_datatables_view.base_datatable_view import BaseDatatableView
from two_factor.views import OTPRequiredMixin

from main.forms import ComponenteForm
from main.models import Componente


class PeriodoCreate(OTPRequiredMixin, CreateView):
    model = Componente
    template_name = 'componentes/create.html'
    success_url = reverse_lazy('periodos_nuevo')
    form_class = ComponenteForm

    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        nuevo_periodo = form.save(commit=False)

        messages.add_message(request, messages.WARNING, 'Componente creado de forma correcta')
        nuevo_periodo.save()
        return redirect('periodos_lista')


class ComponenteJson(OTPRequiredMixin, BaseDatatableView):
    model = Componente
    columns = ['id', 'estado', 'fecha_inicio', 'fecha_fin', 'mes', 'annio', 'empresa.nombre', 'acciones']
    order_columns = ['id', 'estado', 'fecha_inicio', 'fecha_fin', 'mes', 'annio', 'empresa.nombre', '']

    def render_column(self, row, column):
        if column == 'acciones':
            if row.estado == 1:
                return '<button id="editar" type="button" class="btn btn-warning">' \
                       ' <i class="fa fa-pencil"></i> ' \
                       '</button>' \
                       '<button id="eliminar" type="button" class="btn btn-danger">' \
                       ' <i class="fa fa-trash"></i> ' \
                       '</button>' \
                       '<button id="cerrar" type="button" class="btn btn-primary">' \
                       ' <i class="fa fa-chevron-circle-down"></i> ' \
                       '</button>'
            else:
                return '<button id="editar" type="button" class="btn btn-warning">' \
                       ' <i class="fa fa-pencil"></i> ' \
                       '</button>' \
                       '<button id="eliminar" type="button" class="btn btn-danger">' \
                       ' <i class="fa fa-trash"></i> ' \
                       '</button>' \
                       '<button id="abrir" type="button" class="btn btn-success">' \
                       '<i class="fa fa-chevron-circle-up"></i>' \
                       ' </button>'
        else:
            return super(ComponenteJson, self).render_column(row, column)


class MasterContractActions(OTPRequiredMixin, TemplateView):
    template_name = 'conponentes/list.html'