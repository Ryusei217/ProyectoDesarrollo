import decimal
import json

from django.core import signing
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
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


class ComponenteList(OTPRequiredMixin, TemplateView):
    template_name = 'componentes/list.html'


class ComponenteCreate(OTPRequiredMixin, CreateView):
    model = Componente
    template_name = 'componentes/create.html'
    success_url = reverse_lazy('componente_create')
    form_class = ComponenteForm

    def post(self, request, *args, **kwargs):
        password = request.POST.get('password', '')
        form = ComponenteForm(request.POST)
        componente = form.save(commit=False)

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            with transaction.atomic():
                # asignamos el usuario y firmamos el componente
                componente.responsable = user
                componente.save()
                serialized = componente.to_dict()
                componente.firma = signing.dumps(serialized, salt=password)
                componente.save()
                messages.add_message(request, messages.SUCCESS, 'Componente creado de forma correcta')
                return redirect('componente_list')

        return render(request, 'componentes/create.html', {'form': form})


class ComponenteUpdate(OTPRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'componentes/update.html'
    success_url = reverse_lazy('componente_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        password = request.POST.get('password', '')
        form = ComponenteForm(request.POST, instance=self.object)
        componente = form.save(commit=False)

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            with transaction.atomic():
                # asignamos el usuario y firmamos el componente
                componente.responsable = user
                componente.save()
                serialized = componente.to_dict()
                componente.firma = signing.dumps(serialized, salt=password)
                componente.save()
                messages.add_message(request, messages.WARNING, 'Componente editado de forma correcta')
                return redirect('componente_list')

        return render(request, 'componentes/update.html', {'form': form})


class ComponenteDelete(OTPRequiredMixin, TemplateView):
    def post(self, request):
        componente_id = request.POST.get('id', 0)
        componente = Componente.objects.get(pk=componente_id)
        if componente:
            componente.delete()
            return JsonResponse({'result': 'OK', 'message': 'Componente eliminado'})

        return JsonResponse({'result': 'ERROR', 'message': 'Componente inválido'}, status=404)
