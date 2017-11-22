from perfiles.forms import PerfilForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class PerfilEditarView(SuccessMessageMixin, UpdateView):
    template_name = 'perfiles/editar.html'
    form_class = PerfilForm
    model = User
    success_url = '/profile/'
    success_message = _('Profile updated successfully')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super(PerfilEditarView, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user