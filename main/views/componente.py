from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from django_datatables_view.base_datatable_view import BaseDatatableView
from two_factor.views import OTPRequiredMixin

from main.forms import ComponenteForm
from main.models import Componente


class ComponenteJson(OTPRequiredMixin, BaseDatatableView):
    model = Componente
    columns = ['id', 'unii', 'iupac', 'nombre_comercial', 'tipo']
    order_columns = ['id', 'unii', 'iupac', 'nombre_comercial', 'tipo']

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


class ComponenteList(OTPRequiredMixin, TemplateView):
    template_name = 'componentes/list.html'


class ComponenteCreate(OTPRequiredMixin, CreateView):
    model = Componente
    template_name = 'componentes/create.html'
    success_url = reverse_lazy('componente_list')
    form_class = ComponenteForm

    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        componente = form.save(commit=False)

        messages.add_message(request, messages.WARNING, 'Componente creado de forma correcta')
        componente.save()
        return redirect('componente_list')


class ComponenteUpdate(OTPRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'componentes/update.html'
    success_url = reverse_lazy('componente_lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComponenteForm(request.POST, instance=self.object)
        componente = form.save(commit=False)

        messages.add_message(request, messages.WARNING, 'Componente editado de forma correcta')
        componente.save()
        return redirect('componente_lista')


class ComponenteDelete(OTPRequiredMixin, TemplateView):
    def post(self, request):
        componente_id = request.POST.get('id', 0)
        componente = Componente.objects.get(pk=componente_id)
        if componente:
            componente.delete()
            return JsonResponse({'result': 'OK', 'message': 'Componente eliminado'})

        return JsonResponse({'result': 'ERROR', 'message': 'Componente inválido'}, status=404)
